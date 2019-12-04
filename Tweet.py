import Agent


class Tweet:
    def __init__(self, sender):
        self.sender = sender
        # TODO: Should this be the same as the senders?  Or modified in some way?
        self.opinion_rating = sender.opinion_rating
