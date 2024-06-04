import uuid
"""place class, inherited by derived classes"""


class Places:
    def __init__(self, name, price, description):
        self.id = str(uuid.uuid4())
        self.name = name
        self.price = price
        self.description = description
