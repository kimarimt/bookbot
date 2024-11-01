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


def generate_report(text):
    num_words = count_word(text)
    characters = sorted(
        count_characters(text).items(),
        key=lambda item: item[1],
        reverse=True)

    print(f'--- Begin report of {BOOK_PATH} ---')
    print(f'{num_words} words found in the document\n')

    for ch, freq in characters:
        if ch.isalpha():
            print(f'The \'{ch}\' character was found {freq} times')

    print('----------------- END REPORT -----------------')


def main():
    with open(BOOK_PATH) as f:
        file_contents = f.read()
        generate_report(file_contents)


if __name__ == '__main__':
    main()
