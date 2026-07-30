from datetime import datetime


class HistoryService:

    def __init__(self):

        self.events = []

    def add(self, title, action):

        self.events.append({

            "title": title,

            "action": action,

            "time": datetime.now()

        })

    def recent(self):

        return self.events[-10:]

    def total(self):

        return len(self.events)
