
from typing import Dict, Optional
import heapq


class Node:
    def __init__(
        self,
        char: Optional[str],
        freq: int,
        left=None,
        right=None
    ):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    # Allows nodes with equal frequencies in the heap
    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoder:
    def __init__(self):
        self.root = None
        self.codes = {}

    def build_tree(self, frequencies: Dict[str, int]) -> Node:
        if not frequencies:
            raise ValueError("Frequency dictionary cannot be empty")

        if any(freq <= 0 for freq in frequencies.values()):
            raise ValueError("Frequencies must be positive")

        heap = [
            Node(char, freq)
            for char, freq in frequencies.items()
        ]
        heapq.heapify(heap)

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            merged = Node(
                None,
                left.freq + right.freq,
                left,
                right
            )

            heapq.heappush(heap, merged)

        self.root = heap[0]
        return self.root

    def generate_codes(self) -> Dict[str, str]:
        if self.root is None:
            raise ValueError("Build the Huffman tree first")

        self.codes = {}

        def traverse(node, code):
            if node.char is not None:
                self.codes[node.char] = code or "0"
                return

            traverse(node.left, code + "0")
            traverse(node.right, code + "1")

        traverse(self.root, "")
        return self.codes


# Example usage
frequencies = {
    'A': 5,
    'B': 9,
    'C': 12,
    'D': 13,
    'E': 16,
    'F': 45
}

coder = HuffmanCoder()

coder.build_tree(frequencies)
codes = coder.generate_codes()

print("Huffman Codes:")
for char, code in sorted(codes.items()):
    print(f"{char}: {code}")
