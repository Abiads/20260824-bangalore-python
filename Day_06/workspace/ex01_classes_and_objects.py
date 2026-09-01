from vinutils import line

line()
class Book:
    def __init__(self):
        # self is the reference of the newly 
        # created object
        self.title = 'Let us C'     # in the newly constructed object, attribute title is added
        self.author = 'Y Kanitkar'  # in the newly constructed object, attribute author is added
        print('Book object instantiated!')


def main():
    b1 = Book()     # reference of the newly constructed object is assigned to b1
    b2 = Book()     # reference of the newly constructed object is assigned to b2

    # both b1 and b2 have attributes title and author
    
    # print(f'{id(b1) = }')
    # print(f'{type(b1) = }')
    # print(f'{dir(b1) = }')
    print(b1.title, b1.author, sep=", ")
    print(b2.title, b2.author, sep=", ")


main()
