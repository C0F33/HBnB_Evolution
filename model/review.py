import uuuid

cls Review:
    def __init__(self, place_id, user_id, text, score):
        self.id = str(uuid.uuid4())
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
        self.score = score
