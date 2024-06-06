import uuid


class State:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.id = uuid.uuid4()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
