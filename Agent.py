import random
from builtins import abs, open, float
import Tweet


class Agent:
    def __init__(self):
        self.opinion_rating = random.uniform(-1, 1)
        self.friendship_values = {}

    def initialise_friendship_values(self, population):
        """
        Set a friendship rating for all other agents.  Agents with similar opinions are more likely to have a higher friendship rating
        :param population: List
        :return: None
        """
        for agent in population:
            if agent is not self:
                # TODO: Initialise friendship ratings randomly or from a seed i.e not based on opinion
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

        if self.opinion_rating * tweet.opinion_rating > 0:
            """
            Agents agree, so increase friendship rating and move opinion rating further the same direction 
            based on friendship rating.  Higher friendship rating = greater affect on opinion
            """
        else:
            """
            Agents disagree, so decrease friendship rating and move opinion rating further in opposite direction to
            the tweeter.
            """

        x = (self.opinion_rating + ((friendship_rating + 1) / 2) * tweet.opinion_rating) / 2
        y = self.opinion_rating + (friendship_rating + 1) * opinion_difference
        pass




