class Session:
    def __init__(self, name, duration, premium_session, id = None):
        self.id = id
        self.name = name
        self.duration = duration
        self.premium_session = premium_session
