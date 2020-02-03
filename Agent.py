import random
from builtins import abs, open, float
import Tweet
import pandas


class Agent:
    def __init__(self):
        self.opinion_rating = random.uniform(-1, 1)
        self.friendship_values = {}

    def initialise_friendship_values(self, population):
        """
        Set a random friendship rating for all other agents.
        :param population: List
        :return: None
        """
        for agent in population:
            if agent is not self:
                self.friendship_values[agent] = random.uniform(-1, 1)

    def tweet_response(self, tweet):
        """
        Update opinion rating based off opinion value of tweet and friendship value of sender.
        Update friendship rating based off opinion rating of tweet
        :param tweet: Tweet
        :return: None
        """
        opinion_difference = abs(self.opinion_rating - tweet.opinion_rating)
        friendship_rating = self.friendship_values.get(tweet.sender)

        x = (self.opinion_rating + ((friendship_rating + 1) / 2) * tweet.opinion_rating) / 2
        y = self.opinion_rating + (friendship_rating + 1) * opinion_difference
        pass

    def output_data(self):
        data = {'opinion_rating': self.opinion_rating,
                'friendship_values': self.friendship_values.values()}

        dataframe = pandas.DataFrame(data=data)
        dataframe.to_csv('output/agent' + str(self))
        print(dataframe)
        pass



