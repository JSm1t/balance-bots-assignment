from functools import reduce
from instruction_parser import InstructionParser

bots, output_bins = InstructionParser(filename="./input.txt").parse()

microchips_for_comparison = [
    output.microchips[0] for output in output_bins if output.number in [0, 1, 2]
]
multiplied_values = reduce(lambda x, y: x * y, microchips_for_comparison)

print(f"--- PART 2 answer: {multiplied_values} ---")
