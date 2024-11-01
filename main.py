BOOK_PATH = 'books/frankenstein.txt'


def count_word(text):
    return len(text.split())


def count_characters(text):
    lowercased = text.lower()
    characters = {}

    for ch in lowercased:
        if ch in characters:
            characters[ch] += 1
        else:
            characters[ch] = 1

    return characters


def main():
    with open(BOOK_PATH) as f:
        file_contents = f.read()
        words = count_word(file_contents)
        characters = count_characters(file_contents)

        print(words)
        print(characters)


if __name__ == '__main__':
    main()
