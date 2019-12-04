from builtins import range, KeyboardInterrupt, str

from Agent import Agent
from Tweet import Tweet


class Environment:
    def __init__(self, initial_population_size):
        self.population = [Agent() for i in range(initial_population_size)]
        # TODO: initialise friendship values
        for agent in self.population:
            agent.initialise_friendship_values(self.population)

    def tweet(self, agent):
        """
        Method to simulate a particular agent tweeting
        :param agent: Agent
        :return: None
        """
        tweet = Tweet(agent)
        for agent in self.population:
            agent.tweet_response(tweet)

    def run(self):
        """
        Loop to simulate time steps until ctrl + c is pressed
        :return: None
        """
        try:
            while True:
                for agent in self.population:
                    # TODO: call agent update function
                    if agent.check_send_tweet():
                        self.tweet(agent)
        except KeyboardInterrupt:
            # TODO: Output data somewhere? Unless data is outputted as simulation is running
            print('Simulation ended')
