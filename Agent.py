import random
from builtins import abs
import pandas


def limit_values(value):
    return max(min(1, value), -1)


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
        friendship_rating = self.friendship_values.get(tweet.sender.id)

        # Alter opinion rating based off tweet
        opinion_modifier = (friendship_rating / tweet.opinion_rating) / 20
        self.opinion_rating = limit_values(self.opinion_rating + opinion_modifier)

        # Alter friendship values based on opinion
        opinion_difference = abs(self.opinion_rating - tweet.opinion_rating)
        friendship_modifier = (1 - opinion_difference) / 5

        # If agents disagree, reduce friendship value
        if self.opinion_rating * tweet.opinion_rating < 0 < friendship_modifier:
            friendship_modifier *= -1
        friendship_rating += friendship_modifier

        updated_friendship_rating = {tweet.sender.id: limit_values(friendship_rating)}
        self.friendship_values.update(updated_friendship_rating)

    def output_data(self):
        data = {'opinion_rating': self.opinion_rating}

        for key in self.friendship_values:
            data[key] = self.friendship_values[key]

        data_frame = pandas.DataFrame(data=data, index=[0])
        data_frame.to_csv('logs/' + str(self.id) + '.csv', header=False, mode='a', index=False)
        print(data_frame)

