from typing import Literal
from entities.bot import Bot
from entities.output_bin import OutputBin


class InstructionParser:
    def __init__(self, filename="input.txt") -> None:
        self.filename = filename
        self.bots_by_number: dict[str, Bot] = {}
        self.output_bins_by_number: dict[str, OutputBin] = {}

    def parse(self):
        with open(self.filename, "r", encoding="UTF-8") as file:
            while line := file.readline():
                sanitized_line = line.replace("\n", "")

                words_per_line = sanitized_line.split(" ")

                if not words_per_line:
                    continue

                # Instruction for bot
                if words_per_line[0] == "bot":
                    executing_bot = self.get_or_assign_bot(words_per_line[1])

                    low_instruction_target_number = words_per_line[6]
                    low_instruction_target = self.get_or_assign_target(
                        low_instruction_target_number, words_per_line[5]
                    )

                    high_instruction_target_number = words_per_line[11]
                    high_instruction_target = self.get_or_assign_target(
                        high_instruction_target_number, words_per_line[10]
                    )

                    executing_bot.assign_instruction(
                        low_instruction=low_instruction_target.assign_microchip,
                        high_instruction=high_instruction_target.assign_microchip,
                    )

                    continue

                # Value assignment to bot
                if words_per_line[0] == "value":
                    executing_bot = self.get_or_assign_bot(words_per_line[5])

                    executing_bot.assign_microchip(int(words_per_line[1]))

                    continue

                print("--- Could not parse line: ---")
                print(line)
                print("--- End line ---")

            print("--- Finished parsing lines ---")

        return self.bots_by_number.values(), self.output_bins_by_number.values()

    def get_or_assign_target(
        self, target_number: str, target_type: str = "bot"
    ) -> Bot | OutputBin:
        if target_type == "bot":
            return self.get_or_assign_bot(target_number)

        if target_type == "output":
            if existing_output := self.output_bins_by_number.get(target_number):
                return existing_output

            new_output = OutputBin(target_number)

            self.output_bins_by_number[target_number] = new_output

            return new_output

        raise Exception(f"Failed to create entity for target_type: {target_type}")

    def get_or_assign_bot(self, target_number: str):
        if existing_bot := self.bots_by_number.get(target_number):
            return existing_bot

        new_bot = Bot(int(target_number))

        self.bots_by_number[target_number] = new_bot

        return new_bot
