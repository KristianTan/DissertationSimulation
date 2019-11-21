from Agent import Agent
from Tweet import Tweet

class Environment:
    def __init__(self, initial_population_size):
        self.population = [Agent() for i in range(initial_population_size)]


    def tweet(self, agent):
        """
        Method to simulate a particular agent tweeting
        :param agent: Agent
        :return: None
        """
        tweet = Tweet(agent)
        for agent in self.population:
            agent.tweet_response(tweet)
        pass


    def run(self):
        """
        Loop to simulate time steps
        :return: None
        """
        while True:
            for agent in self.population:
                # TODO: call agent update function
                if agent.send_tweet():
                    self.tweet(agent)
                pass