import re

word_counts = dict[str, int]()


def count_words(text: str, counts: dict[str, int]) -> None:
    for word in re.findall(r"\w+", text):
        lowercase_word = word.lower()

        if lowercase_word not in counts:
            counts[lowercase_word] = 0

        counts[lowercase_word] += 1


with open("tekstdostatystyki.txt") as file:
    for line in file.readlines():
        count_words(line, word_counts)

for word in sorted(word_counts.keys()):
    print(f"{word}: {word_counts[word]} razy")
