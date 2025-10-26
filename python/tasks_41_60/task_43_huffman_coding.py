import bisect

from python.tasks_41_60.coding_algorithms import CodingFactory, Decoder, Encoder, TreeNode, WeightedTreeNode


class HuffmanCodingFactory(CodingFactory):
    def __init__(self, text: str):
        self._text = text
        self._letter_counts = CodingFactory._count_letters(text)

    def build(self) -> TreeNode[str]:
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

        return leaves[0]


message_to_encode = "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"
print(f"Encoding message `{message_to_encode}`...")

huffman_coding_factory = HuffmanCodingFactory(message_to_encode)
message_coding_tree = huffman_coding_factory.build()

encoded_message = Encoder.encode(message_to_encode, message_coding_tree)
print(f"Encoded message: `{encoded_message}`")

decoded_message = Decoder.decode(encoded_message, message_coding_tree)
print(f"Decoded message: `{decoded_message}`")

is_recoding_success = decoded_message == message_to_encode
print(f"Recoding {"succeeded" if is_recoding_success else "failed"}.")
