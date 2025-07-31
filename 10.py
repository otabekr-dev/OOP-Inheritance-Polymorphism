class Document:
    def __init__(self, title):
        self.title = title

    def print_preview(self):
        pass



class WordDocument(Document):
    def print_preview(self):
        return f"Word faylining ko'rinishi: '{self.title}.docx'"



class PdfDocument(Document):
    def print_preview(self):
        return f"PDF faylining ko'rinishi: '{self.title}.pdf'"



doc1 = WordDocument("document")
doc2 = PdfDocument("contract")

print(doc1.print_preview())
print(doc2.print_preview())
