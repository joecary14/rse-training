class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f'{self.title} by {self.author}'
    
book = Book('The Catcher in the Rye', 'J.D. Salinger')
print(book)
    