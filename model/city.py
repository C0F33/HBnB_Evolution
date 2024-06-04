import uuid


class city(state):
    def __init__(self, name, state_id):
        self.id = str(uuid.uuid4())
        self.name = name
        self.state_id = state_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        return self.__dict__.copy()
