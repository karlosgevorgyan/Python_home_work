class Book:
    def __init__(self,id, author, title, description, chapter_count, page_count):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.chapter_count = chapter_count
        self.page_count = page_count

    def __str__(self):
        return ','.join([str(self.book_id),self.author,self.title,self.description,
                         str(self.chapter_count),str(self.page_count)])

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.book_id == other.book_id \
            and self.author == other.author \
            and self.title == other.title \
            and self.description == other.description \
            and self.chapter_count == other.chapter_count \
            and self.page_count == other.page_count

    def __ne__(self, other):
        return not self == other