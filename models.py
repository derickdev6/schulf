from datetime import date

class Guide:
    def __init__(self, id, title, date, body, link):
        self.id = id
        self.title = title
        self.date = date
        self.body = body
        self.link = link
    
    def __str__(self):
        return f'{self.id} - {self.title}\n\t{self.date}'
        