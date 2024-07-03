def main(file: str):
    with open(file) as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_count = count_chars(file_contents)

    print(f"--- Begin report about {file} ---", end="\n\n")
    print(f"{word_count} words found in the document", end="\n\n")
    for item in char_count:
        print(f"The letter {item["letter"]} was found {item["count"]} times")
    print("\n--- End of report ---")


def count_words(contents: str):
    words = contents.split()

    return len(words)


def count_chars(contents: str):
    chars = {}

    for char in contents:
        if char.lower() not in chars:
            chars[char.lower()] = 1
        else:
            chars[char.lower()] += 1

    chars_cleaned = []

    for item in chars:
        if item.isalpha():
            chars_cleaned.append({"letter": item, "count": chars[item]})

    chars_cleaned.sort(key=on_sort, reverse=True)

    return chars_cleaned


def on_sort(d: dict):
    return d["count"]


if __name__ == "__main__":
    main("books/frankenstein.txt")
