import Agent


class Tweet:
    def __init__(self, sender):
        self.sender = sender
        self.opinion_rating = sender.opinion_rating
