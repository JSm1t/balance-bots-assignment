from instruction_parser import InstructionParser

bots, output_bins = InstructionParser(filename="./input.txt").parse()

for output_bin in output_bins:
    print(f"output {output_bin.number} has microchips {output_bin.microchips}")
