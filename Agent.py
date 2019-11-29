import random
import Tweet


class Agent:

    def __init__(self):
        self.opinion_rating = random.uniform(-1, 1)

    def tweet_response(self, tweet):
        """
        Update friendship values and opinion rating based off tweet
        :param tweet: Tweet
        :return: None
        """
        pass

    def send_tweet(self):
        """
        Return true if this agent is going to tweet this time step
        :return: boolean
        """
        return random.randint(0, 10) <= 1
