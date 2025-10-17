from abc import ABC, abstractmethod


class TreeNode[T]:
    def __init__(self, value: T):
        self.value = value
        self.left: TreeNode[T] | None = None
        self.right: TreeNode[T] | None = None

    def __str__(self):
        return f"<{self.value}>"


class WeightedTreeNode[T](TreeNode[T]):
    def __init__(self, value: T, weight: int):
        super().__init__(value)
        self.weight = weight

    def __str__(self):
        return f"<{self.value}({self.weight})>"


class CodingFactory(ABC):
    @staticmethod
    def _count_letters(text: str) -> list[tuple[str, int]]:
        letter_counts: dict[str, int] = {}

        for letter in text:
            if letter not in letter_counts:
                letter_counts[letter] = 0
            letter_counts[letter] += 1

        return list(letter_counts.items())

    @abstractmethod
    def build(self) -> TreeNode[str]:
        pass


class Encoder:
    @staticmethod
    def _coding_tree_to_coding_table(coding_tree: TreeNode[str | None]) -> dict[str, str]:
        coding_table: dict[str, str] = {}

        def m_to_coding_table(node: TreeNode[str | None], current_code: str) -> None:
            if node.left is None and node.right is None:
                coding_table[node.value] = current_code
                return

            if node.left is not None:
                m_to_coding_table(node.left, current_code + "0")
            if node.right is not None:
                m_to_coding_table(node.right, current_code + "1")

        m_to_coding_table(coding_tree, "")
        return coding_table

    @staticmethod
    def encode(clear_text: str, coding_tree: TreeNode[str | None]) -> str:
        coding_table = Encoder._coding_tree_to_coding_table(coding_tree)
        return "".join([coding_table[letter] for letter in clear_text])


class Decoder:
    @staticmethod
    def decode(encoded_text: str, coding_tree: TreeNode[str | None]) -> str:
        decoded_message = ""

        node = coding_tree
        for bit in encoded_text:
            node = node.right if bit == "1" else node.left

            if node.left is None and node.right is None:
                decoded_message += node.value
                node = coding_tree

        return decoded_message
