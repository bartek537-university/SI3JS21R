import bisect


class WeightedTreeNode[T]:
    def __init__(self, value: T, weight: int):
        self.value = value
        self.weight = weight
        self.left: WeightedTreeNode[T] | None = None
        self.right: WeightedTreeNode[T] | None = None

    def __str__(self):
        return f"<{self.value}({self.weight})>"


class HfCodeFactory:
    def __init__(self, text: str):
        self._text = text
        self._letter_counts = HfCodeFactory._count_letters(text)
        self._code: WeightedTreeNode[str | None] | None = None

    @staticmethod
    def _count_letters(text: str) -> list[tuple[str, int]]:
        letter_counts: dict[str, int] = {}

        for letter in text:
            if letter not in letter_counts:
                letter_counts[letter] = 0
            letter_counts[letter] += 1

        return list(letter_counts.items())

    @staticmethod
    def _weight_selector[V](node: WeightedTreeNode[V]) -> int:
        return node.weight

    def build(self) -> None:
        leaves: list[WeightedTreeNode[str | None]] = [
            WeightedTreeNode(letter, count) for letter, count in self._letter_counts
        ]
        leaves.sort(key=lambda leaf: leaf.weight)

        while len(leaves) > 1:
            a, b = leaves.pop(0), leaves.pop(0)

            compound_leaf = WeightedTreeNode(None, a.weight + b.weight)
            compound_leaf.left = a
            compound_leaf.right = b

            bisect.insort(leaves, compound_leaf, key=lambda leaf: leaf.weight)

        self._code = leaves[0]

    @property
    def code(self) -> WeightedTreeNode[str | None]:
        return self._code


def code_tree_to_code_table(code_tree: WeightedTreeNode[str | None]) -> dict[str, str]:
    result_code_table: dict[str, str] = {}

    def _to_code_table(code: str, tree: WeightedTreeNode[str | None]) -> None:
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
    def decode(text: str, code_tree: WeightedTreeNode[str | None]) -> str:
        message = ""

        current_node = code_tree
        for bit in text:
            current_node = current_node.right if bit == "1" else current_node.left

            if current_node.left is None and current_node.right is None:
                message += current_node.value
                current_node = code_tree

        return message


message_to_encode = "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"

hf_code_tree_factory = HfCodeFactory(message_to_encode)
hf_code_tree_factory.build()

abcde_code_tree = hf_code_tree_factory.code
abcde_code_table = code_tree_to_code_table(abcde_code_tree)

print(abcde_code_table)

encoded_message = Encoder.encode(message_to_encode, abcde_code_table)
print(encoded_message)

decoded_message = Decoder.decode(encoded_message, abcde_code_tree)
print(decoded_message)

print(decoded_message == message_to_encode)
