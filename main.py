BOOK_PATH = 'books/frankenstein.txt'

def main():
    with open(BOOK_PATH) as f:
        print(f.read())


if __name__ == '__main__':
    main()
