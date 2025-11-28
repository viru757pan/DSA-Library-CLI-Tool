from datetime import datetime


class Problem:
    def __init__(self, title, difficulty, tags, filepath):
        self.title = title
        self.difficulty = difficulty
        self.tags = tags
        self.filepath = filepath
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "title": self.title,
            "difficulty": self.difficulty,
            "tags": self.tags,
            "filepath": self.filepath,
            "created_at": self.created_at
        }
