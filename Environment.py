from builtins import range, KeyboardInterrupt
from random import randint

from Agent import Agent
from Tweet import Tweet


class Environment:
    def __init__(self, initial_population_size):
        self.population = [Agent() for i in range(initial_population_size)]
        for agent in self.population:
            agent.initialise_friendship_values(self.population)

    def tweet(self, sender):
        """
        Method to simulate a particular agent tweeting
        :param sender: Agent
        :return: None
        """
        tweet = Tweet(sender)
        for agent in self.population:
            if agent is not sender:
                agent.tweet_response(tweet)

    def run(self):
        """
        Loop to simulate time steps until ctrl + c is pressed
        :return: None
        """
        try:
            while True:
                self.tweet(self.select_tweeter())
        except KeyboardInterrupt:
            # TODO: Output data somewhere? Unless data is outputted as simulation is running
            print('Simulation ended')

    def select_tweeter(self):
        return self.population[randint(0, len(self.population) - 1)]
