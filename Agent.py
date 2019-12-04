import random
from builtins import abs, open, float

import Tweet


def map_value(value, input_min, input_max, output_min, output_max):
    """
    Takes a value and maps it between a given range
    :param value: Float
    :param input_min: Float
    :param input_max: Float
    :param output_min: Float
    :param output_max: Float
    :return: Float
    """
    input_range = input_max - input_min
    output_range = output_max - output_min

    # Convert the left range into a 0-1 range (float)
    value_scaled = float(value - input_min) / float(input_range)

    # Convert the 0-1 range into a value in the right range.
    return output_min + (value_scaled * output_range)


def check_send_tweet():
    """
    Return true if this agent is going to tweet this time step
    :return: boolean
    """
    return random.randint(0, 10) is 0


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
                lower, upper = -1, 1
                # Get the difference in opinion ratings
                opinion_difference = abs(self.opinion_rating - agent.opinion_rating)
                # Get a value to adjust upper and lower bounds by, bigger difference = smaller adjustment, and vice versa
                adjustment = abs(1 - opinion_difference)

                # Agents more likely to have higher friendship rating with others that share their opinion
                if self.opinion_rating * agent.opinion_rating > 0 or self.opinion_rating == agent.opinion_rating:
                    upper += adjustment
                    lower += adjustment
                else:
                    upper -= adjustment
                    lower -= adjustment

                friendship_value = random.uniform(lower, abs(upper))
                self.friendship_values[agent] = map_value(friendship_value, -1, 2, -1, 1)

    def tweet_response(self, tweet):
        """
        Update friendship values and opinion rating based off tweet
        :param tweet: Tweet
        :return: None
        """
        pass

