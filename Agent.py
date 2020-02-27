import random
from builtins import abs
import pandas


def limit_values(value, upper=1, lower=-1):
    return max(min(upper, value), lower)


class Agent:
    def __init__(self, id):
        self.opinion_rating = random.uniform(-1, 1)
        self.friendship_values = {}
        self.id = "agent" + str(id)

    def initialise_friendship_values(self, population):
        """
        Set a random friendship rating for all other agents and create a csv to store logs
        :param population: List
        :return: None
        """
        for agent in population:
            if agent is not self:
                self.friendship_values[agent.id] = random.uniform(-1, 1)

        # Output initial data and column titles to a csv
        data = {'opinion_rating': self.opinion_rating}

        for key in self.friendship_values:
            data[key] = self.friendship_values[key]

        data_frame = pandas.DataFrame(data=data, index=[0])
        data_frame.to_csv('logs/' + str(self.id) + '.csv', header=True, mode='w', index=False)

    def tweet_response(self, tweet):
        """
        Update opinion rating based off opinion value of tweet and friendship value of sender.
        Update friendship rating based off opinion rating of tweet
        :param tweet: Tweet
        :return: None
        """
        DEFAULT_MODIFIER = 0.01
        friendship_rating = self.friendship_values.get(tweet.sender.id)

        # Decide whether to increase or decrease values based on tweet values.
        opinion_multiplier = -1 if (friendship_rating < 0 < tweet.opinion_rating) or (tweet.opinion_rating < 0 < friendship_rating) else 1
        friendship_multiplier = -1 if (tweet.opinion_rating < 0 < self.opinion_rating) or (self.opinion_rating < 0 < tweet.opinion_rating) else 1

        opinion_modifier = DEFAULT_MODIFIER * opinion_multiplier
        friendship_modifier = DEFAULT_MODIFIER * friendship_multiplier

        updated_friendship_value = limit_values(friendship_rating + friendship_modifier)
        self.friendship_values.update({tweet.sender.id: updated_friendship_value})
        self.opinion_rating = limit_values(self.opinion_rating + opinion_modifier)

    def output_data(self):
        data = {'opinion_rating': self.opinion_rating}

        for key in self.friendship_values:
            data[key] = self.friendship_values[key]

        data_frame = pandas.DataFrame(data=data, index=[0])
        data_frame.to_csv('logs/' + str(self.id) + '.csv', header=False, mode='a', index=False)
        print(data_frame)

