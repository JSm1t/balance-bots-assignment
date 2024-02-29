import argparse
from functools import reduce

from src.instruction_parser import InstructionParser
from src.executor import Executor

parser = argparse.ArgumentParser(
    description="Parses and executes a set of instructions and prints the results",
)

parser.add_argument(
    "--filename",
    help="the filename of the set of instructions to parse",
    default="input.txt",
)

args = parser.parse_args()

executor = Executor()

InstructionParser(executor=executor, filename=args.filename).parse()

output_bins = executor.get_all_outputs()

microchips_for_comparison = [
    output.microchips[0] for output in output_bins if output.number in [0, 1, 2]
]
multiplied_values = reduce(lambda x, y: x * y, microchips_for_comparison)

print(f"--- PART 2 answer: {multiplied_values} ---")
