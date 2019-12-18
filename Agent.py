import random
from builtins import abs, open, float
import Tweet


class Agent:
    def __init__(self):
        self.opinion_rating = random.uniform(-1, 1)
        self.friendship_values = {}

    def initialise_friendship_values(self, population):
        # TODO: Refactor this to return a dict, and call it from the constructor
        """
        Set a friendship rating for all other agents.  Agents with similar opinions are more likely to have a higher friendship rating
        :param population: List
        :return: None
        """
        for agent in population:
            if agent is not self:
                lower, upper = -1, 1
                # Get the difference in opinion ratings
                opinion_difference = abs(self.opinion_rating - agent.opinion_rating)
                # Get a value, bigger difference in opinion = smaller friendship rating, and vice versa
                friendship_value = abs(1 - opinion_difference)

                # If agents are differing in opinion, negative friendship rating
                if self.opinion_rating * agent.opinion_rating < 0:
                    friendship_value *= -1

                self.friendship_values[agent] = friendship_value

    @staticmethod
    def check_send_tweet():
        """
        Return true if this agent is going to tweet this time step
        :return: boolean
        """
        return random.randint(0, 10) is 0

    def tweet_response(self, tweet):
        """
        Update opinion rating based off opinion value of tweet and friendship value of sender.
        Update friendship rating based off opinion rating of tweet
        :param tweet: Tweet
        :return: None
        """
        opinion_difference = self.opinion_rating - tweet.opinion_rating
        print(opinion_difference)

