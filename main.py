from functools import reduce

from src.instruction_parser import InstructionParser
from src.executor import Executor

executor = Executor()

InstructionParser(executor=executor, filename="./input.txt").parse()

output_bins = executor.get_all_outputs()

microchips_for_comparison = [
    output.microchips[0] for output in output_bins if output.number in [0, 1, 2]
]
multiplied_values = reduce(lambda x, y: x * y, microchips_for_comparison)

print(f"--- PART 2 answer: {multiplied_values} ---")
