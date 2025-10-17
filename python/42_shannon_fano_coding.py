import math
from typing import Final


class TreeNode[T]:
    def __init__(self, value: T):
        self.value = value
        self.left: TreeNode[T] | None = None
        self.right: TreeNode[T] | None = None


class SFCodeTreeFactory:
    LETTER_VALUE_KEY: Final[int] = 0
    LETTER_COUNT_KEY: Final[int] = 1

    @staticmethod
    def _count_letters(text: str) -> list[tuple[str, int]]:
        letter_counts: dict[str, int] = {}

        for letter in text:
            if letter not in letter_counts:
                letter_counts[letter] = 0
            letter_counts[letter] += 1

        return list(letter_counts.items())

    def __init__(self, text: str):
        self._text = text
        self._letter_counts = SFCodeTreeFactory._count_letters(text)
        self._code_tree: TreeNode[str | None] = TreeNode(None)

    def _get_splitter_position(self, start: int, end: int) -> int:
        if end - start < 2:
            raise ValueError("Not enough values to split.", end - start)

        letters_to_split = self._letter_counts[start:end]
        minimum_counts_delta: tuple[int, float] = (-1, math.inf)

        left_count_total = 0
        right_count_total = sum([count for letter, count in letters_to_split])

        for index, (letter, count) in enumerate(letters_to_split[:-1]):
            left_count_total += count
            right_count_total -= count

            current_counts_delta = abs(left_count_total - right_count_total)
            if current_counts_delta < minimum_counts_delta[1]:
                minimum_counts_delta = (index + 1, current_counts_delta)

        return minimum_counts_delta[0] + start

    def _create_code_tree(self, start: int, end: int, result: TreeNode[str | None]) -> None:
        if end - start < 1:
            return
        if end - start < 2:
            result.value = self._letter_counts[start][SFCodeTreeFactory.LETTER_VALUE_KEY]
            return

        splitter_position = self._get_splitter_position(start, end)

        result.left = TreeNode(None)
        result.right = TreeNode(None)

        self._create_code_tree(start, splitter_position, result.left)
        self._create_code_tree(splitter_position, end, result.right)

    def build(self) -> None:
        self._letter_counts.sort(key=lambda count: count[SFCodeTreeFactory.LETTER_COUNT_KEY], reverse=True)
        self._create_code_tree(0, len(self._letter_counts), self._code_tree)

    @property
    def code_tree(self) -> TreeNode[str]:
        return self._code_tree


def code_tree_to_code_table(code_tree: TreeNode[str | None]) -> dict[str, str]:
    result_code_table: dict[str, str] = {}

    def _to_code_table(code: str, tree: TreeNode[str | None]) -> None:
        if tree.left is None and tree.right is None:
            result_code_table[tree.value] = code
            return

        if tree.left is not None:
            _to_code_table(code + "0", tree.left)
        if tree.right is not None:
            _to_code_table(code + "1", tree.right)

    _to_code_table("", code_tree)

    return result_code_table


class Encoder:
    @staticmethod
    def encode(text: str, code_table: dict[str, str]) -> str:
        return "".join([code_table[letter] for letter in text])


class Decoder:
    @staticmethod
    def decode(text: str, code_tree: TreeNode[str | None]) -> str:
        message = ""

        current_node = code_tree
        for bit in text:
            current_node = current_node.right if bit == "1" else current_node.left

            if current_node.value is not None:
                message += current_node.value
                current_node = code_tree

        return message


message_to_encode = "wyrewolwerowany rewolwerowiec wyrewolwerował wyrewolwerowanego rewolwerowca"

sf_code_tree_factory = SFCodeTreeFactory(message_to_encode)
sf_code_tree_factory.build()

abcde_code_tree = sf_code_tree_factory.code_tree
abcde_code_table = code_tree_to_code_table(abcde_code_tree)

print(abcde_code_table)

encoded_message = Encoder.encode(message_to_encode, abcde_code_table)
print(encoded_message)

decoded_message = Decoder.decode(encoded_message, abcde_code_tree)
print(decoded_message)

print(decoded_message == message_to_encode)
