BOOK_PATH = 'books/frankenstein.txt'


def count_word(text):
    return len(text.split())


def main():
    with open(BOOK_PATH) as f:
        file_contents = f.read()
        words = count_word(file_contents)

        print(words)


if __name__ == '__main__':
    main()
