class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            return self.items.pop() # if parameter on pop is empty it automatically will delete the last element inside of a list
    
    def peek(self):
        if self.items == []:
            print("Stack is empty")
        else:
            return self.items[-1]
    
    def display(self):
        print(self.items)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        self.items.pop(0)

    def peek(self):
        return self.items[0]  

    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False
    
class Document:
    def __init__(self, name):
        self.name = name
        # TODO: gunakan Stack untuk menyimpan halaman
        # self.page = Stack()
        self.pages = Stack()

    def addPage(self, page):
        self.pages.push(page)


    def printPage(self):
        if self.pages.is_empty():
            print("Halaman kosong")
        else:
            print(self.pages.pop())
        # TODO: ambil satu halaman dari document
        

    def isEmpty(self):
        if self.pages.is_empty():
            return True
        else:
            return False

class PrintQueue:
    def __init__(self):
        # TODO: gunakan Queue untuk menyimpan document
        self.documents = Queue()

    def addDocument(self, document):
        self.documents.enqueue(document)
        

    def printDocument(self):
        # TODO:
        # 1. Ambil document paling depan dari queue
        # 2. Keluarkan document tersebut dari antrean
        # 3. Cetak seluruh halaman dalam document dengan konsep LIFO
        doc = self.documents.peek()
        self.documents.dequeue()

        while not doc.isEmpty():
            doc.printPage()
        


doc1 = Document("Tugas")
doc1.addPage("Halaman 1")
doc1.addPage("Halaman 2")
doc1.addPage("Halaman 3")

# doc1.printPage()
print("\n")

doc2 = Document("Tugas2")
doc2.addPage("Halaman 1")
doc2.addPage("Halaman 2")
doc2.addPage("Halaman 3")

# doc2.printPage()
print("\n")

printQueue = PrintQueue()
printQueue.addDocument(doc1)
printQueue.addDocument(doc2)
printQueue.printDocument()

  
# s1 = Stack()

# # s1.push(10)
# # s1.push(20)
# # s1.push(30)
# # s1.display()

# # print(s1.peek())
# # s1.display()

# s1.peek()
# # s1.display()