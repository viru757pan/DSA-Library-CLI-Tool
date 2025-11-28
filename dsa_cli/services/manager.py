import json
import os
from dsa_cli.models.problem import Problem

DB_PATH = "storage/database.json"


class DSAManager:
    def __init__(self):
        if not os.path.exists(DB_PATH):
            os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
            with open(DB_PATH, "w") as f:
                json.dump({"problems": []}, f)

        try:
            self.load_data()
        except:
            with open(DB_PATH, "w") as f:
                json.dump({"problems": []}, f)

    def load_data(self):
        with open(DB_PATH, "r") as f:
            return json.load(f)

    def save_data(self, data):
        with open(DB_PATH, "w") as f:
            json.dump(data, f, indent=4)

    def add_problem(self, title, difficulty, tags, filepath):
        data = self.load_data()

        # validation: prevent duplicate entries
        for p in data["problems"]:
            if p["title"].lower() == title.lower():
                return False, "🚫 Problem already exists!"

        problem = Problem(title, difficulty, tags, filepath)
        data["problems"].append(problem.to_dict())
        self.save_data(data)
        return True, "✅ Problem added successfully!"

    def list_problems(self):
        data = self.load_data()
        return data["problems"]

    def search(self, keyword):
        data = self.load_data()
        return [p for p in data["problems"] if keyword.lower() in p["title"].lower() or keyword.lower() in " ".join(p["tags"]).lower()]

    def delete_problem(self, title):
        data = self.load_data()
        problems = data.get("problems", [])

        updated = [p for p in problems if p["title"].lower() != title.lower()]

        # If nothing removed
        if len(updated) == len(problems):
            return False

        # Save updated list
        data["problems"] = updated
        self.save_data(data)
        return True
