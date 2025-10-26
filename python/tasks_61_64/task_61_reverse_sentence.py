class Sentence:
    def __init__(self, text: str):
        self.text = text

    def __str__(self):
        return self.text

    def reversed(self) -> str:
        return ' '.join(reversed(self.text.split(' ')))


sentence = Sentence("Jestem studentem. Jestem studentem.")
print(sentence)
print(sentence.reversed())
