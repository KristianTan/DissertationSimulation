import random
from builtins import abs, open, float
import Tweet
import pandas


class Agent:
    def __init__(self, id):
        self.opinion_rating = random.uniform(-1, 1)
        self.friendship_values = {}
        self.id = "agent" + str(id)

    def initialise_friendship_values(self, population):
        """
        Set a random friendship rating for all other agents.
        :param population: List
        :return: None
        """
        for agent in population:
            if agent is not self:
                self.friendship_values[agent.id] = random.uniform(-1, 1)

        # Output initial data and column titles
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
        opinion_difference = abs(self.opinion_rating - tweet.opinion_rating)
        friendship_rating = self.friendship_values.get(tweet.sender.id)

        affector = (friendship_rating / tweet.opinion_rating) / 10
        if affector < -1:
            affector += 1
        self.opinion_rating += affector

        if self.opinion_rating * tweet.opinion_rating > 0:
            """
            Agents agree, so increase friendship rating and move opinion rating further the same direction 
            based on friendship rating.  Higher friendship rating = greater affect on opinion
            """

            if friendship_rating > 0:
                # They are friends that agree so move opinion rating closer (- or +) to that of tweeter
                affector = (friendship_rating / tweet.opinion_rating) / 10
                if affector < -1:
                    affector += 1
                print(affector)
            else:
                # They agree but are not friends so increase friendship rating more
                pass

            # They agree so increase friendship rating
        else:
            """
            Agents disagree, so decrease friendship rating and move opinion rating further in opposite direction to
            the tweeter.
            """

            if friendship_rating > 0:
                # They are friends that disagree so move opinion towards theirs
                pass
            else:
                # Not friends who disagree so reduce friendship rating
                pass

            # They disagree so decrease friendship rating

        # x = (self.opinion_rating + ((friendship_rating + 1) / 2) * tweet.opinion_rating) / 2
        # y = self.opinion_rating + (friendship_rating + 1) * opinion_difference
        # pass

    def output_data(self):
        data = {'opinion_rating': self.opinion_rating}

        for key in self.friendship_values:
            data[key] = self.friendship_values[key]

        data_frame = pandas.DataFrame(data=data, index=[0])
        data_frame.to_csv('logs/' + str(self.id) + '.csv', header=False, mode='a', index=False)
        print(data_frame)



