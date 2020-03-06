import random
from builtins import abs
import pandas


def limit_values(value, upper: float = 1, lower: float = -1):
    return max(min(upper, value), lower)


class Agent:
    def __init__(self, id, opinion_rating=None, friendship_values=None):

        if opinion_rating is not None:
            try:
                self.opinion_rating = float(opinion_rating)
            except ValueError:
                self.opinion_rating = random.uniform(-1, 1)
        else:
            self.opinion_rating = random.uniform(-1, 1)

        self.initial_friendships = friendship_values if friendship_values is not None else None
        self.friendship_values = {}
        self.id = "agent" + str(id)

    def initialise_friendship_values(self, population):
        """
        Set a random friendship rating for all other agents and create a csv to store logs
        :param population: List
        :return: None
        """
        if self.initial_friendships is None:
            for agent in population:
                if agent is not self:
                    self.friendship_values[agent.id] = random.uniform(-1, 1)
                else:
                    self.friendship_values[agent.id] = 1
        else:
            for i in range (0, len(population)):
                agent = population[i]
                if agent is not self:
                    # If friendship value is missing or is not a valid float, generate a random friendship value
                    if i < len(self.initial_friendships):
                        try:
                            self.friendship_values[agent.id] = float(self.initial_friendships[i])
                        except ValueError:
                            self.friendship_values[agent.id] = random.uniform(-1, 1)
                    else:
                        self.friendship_values[agent.id] = random.uniform(-1, 1)
                else:
                    self.friendship_values[agent.id] = 1

        # Output initial data and column titles to a csv
        data = {'opinion_rating': self.opinion_rating}

        for key in self.friendship_values:
            data[key] = self.friendship_values[key]

        data['tweeter'] = None
        data['tweet_rating'] = None
          
        data_frame = pandas.DataFrame(data=data, index=[0])
        data_frame.to_csv('logs/' + str(self.id) + '.csv', header=True, mode='w', index=False)

    def tweet_response(self, tweet):
        """
        Update opinion rating based off opinion value of tweet and friendship value of sender.
        Update friendship rating based off opinion rating of tweet
        :param tweet: Tweet
        :return: None
        """
        DEFAULT_MODIFIER = 0.001
        friendship_rating = self.friendship_values.get(tweet.sender.id)

        # Decide whether to increase or decrease values based on tweet values.
        opinion_multiplier = -1 if (friendship_rating < 0 < tweet.opinion_rating) or (tweet.opinion_rating < 0 < friendship_rating) else 1
        friendship_multiplier = -1 if (tweet.opinion_rating < 0 < self.opinion_rating) or (self.opinion_rating < 0 < tweet.opinion_rating) else 1

        # The higher the friendship rating the greater the effect on the opinion
        opinion_effector = abs(friendship_rating) / 1000

        # The closer the opinion ratings the bigger the effect on friendship ratings
        opinion_difference = abs(self.opinion_rating - tweet.opinion_rating)

        opinion_difference_squared = opinion_difference ** 2
        friendship_effector_mapped = 1 - (opinion_difference_squared / 2)
        friendship_effector = friendship_effector_mapped / 1000

        opinion_modifier = (DEFAULT_MODIFIER + opinion_effector) * opinion_multiplier
        friendship_modifier = (DEFAULT_MODIFIER + friendship_effector) * friendship_multiplier

        updated_friendship_value = limit_values(friendship_rating + friendship_modifier)
        updated_opinion_rating = limit_values(self.opinion_rating + opinion_modifier)
        self.friendship_values.update({tweet.sender.id: updated_friendship_value})
        self.opinion_rating = updated_opinion_rating

    def output_data(self, tweet):
        """
        Outputs the agent's friendship ratings and opinion rating to a CSV each iteration
        :param tweet: Tweet
        :return: None
        """
        data = {'opinion_rating': self.opinion_rating}

        for key in self.friendship_values:
            data[key] = self.friendship_values[key]

        data['tweeter'] = tweet.sender.id
        data['tweet_rating'] = tweet.opinion_rating

        data_frame = pandas.DataFrame(data=data, index=[0])
        data_frame.to_csv('logs/' + str(self.id) + '.csv', header=False, mode='a', index=False)
        print(data_frame)

