from __future__ import annotations

import math
from typing import Final

from python.coding_algorithms import CodingFactory, Decoder, Encoder, TreeNode


class ShannonFanoCodingFactory(CodingFactory):
    LETTER_VALUE_KEY: Final[int] = 0
    LETTER_COUNT_KEY: Final[int] = 1

    def __init__(self, text: str):
        self._text = text
        self._letter_counts = CodingFactory._count_letters(text)

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
                minimum_counts_delta = (index + 1 + start, current_counts_delta)

        return minimum_counts_delta[0]

    def _create_code(self, start: int, end: int, result: TreeNode[str | None]) -> None:
        if end - start < 1:
            return
        if end - start < 2:
            result.value = self._letter_counts[start][ShannonFanoCodingFactory.LETTER_VALUE_KEY]
            return

        splitter_position = self._get_splitter_position(start, end)

        result.left = TreeNode(None)
        result.right = TreeNode(None)

        self._create_code(start, splitter_position, result.left)
        self._create_code(splitter_position, end, result.right)

    def build(self) -> TreeNode[str]:
        self._letter_counts.sort(key=lambda count: count[ShannonFanoCodingFactory.LETTER_COUNT_KEY], reverse=True)

        result_coding = TreeNode[str | None](None)
        self._create_code(0, len(self._letter_counts), result_coding)
        return result_coding


message_to_encode = "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"
print(f"Encoding message `{message_to_encode}`...")

huffman_coding_factory = ShannonFanoCodingFactory(message_to_encode)
message_coding_tree = huffman_coding_factory.build()

encoded_message = Encoder.encode(message_to_encode, message_coding_tree)
print(f"Encoded message: `{encoded_message}`")

decoded_message = Decoder.decode(encoded_message, message_coding_tree)
print(f"Decoded message: `{decoded_message}`")

is_recoding_success = decoded_message == message_to_encode
print(f"Recoding {"succeeded" if is_recoding_success else "failed"}.")
