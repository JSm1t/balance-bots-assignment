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
                    self.parse_and_assign_bot_instruction(
                        bot_number=words_per_line[1],
                        low_instruction_type=words_per_line[5],
                        low_instruction_number=words_per_line[6],
                        high_instruction_type=words_per_line[10],
                        high_instruction_number=words_per_line[11],
                    )

                    continue

                # Value assignment to bot
                if words_per_line[0] == "value":
                    self.parse_and_assign_value_instruction(
                        bot_number=words_per_line[5], value_number=words_per_line[1]
                    )

                    continue

                print("--- Could not parse line: ---")
                print(line)
                print("--- End line ---")

            print("--- Finished parsing lines ---")

        return self.bots_by_number.values(), self.output_bins_by_number.values()

    def parse_and_assign_bot_instruction(
        self,
        bot_number: str,
        low_instruction_type: str,
        low_instruction_number: str,
        high_instruction_type: str,
        high_instruction_number: str,
    ):
        executing_bot = self.get_or_assign_bot(bot_number)

        low_instruction_target = self.get_or_assign_target(
            low_instruction_number, low_instruction_type
        )

        high_instruction_target = self.get_or_assign_target(
            high_instruction_number, high_instruction_type
        )

        executing_bot.assign_instruction(
            low_instruction=low_instruction_target.assign_microchip,
            high_instruction=high_instruction_target.assign_microchip,
        )

    def parse_and_assign_value_instruction(
        self,
        bot_number: str,
        value_number: str,
    ):
        executing_bot = self.get_or_assign_bot(bot_number)

        executing_bot.assign_microchip(int(value_number))

    def get_or_assign_target(
        self, target_number: str, entity_type: str = "bot"
    ) -> Bot | OutputBin:
        if entity_type == "bot":
            return self.get_or_assign_bot(target_number)

        if entity_type == "output":
            if existing_output := self.output_bins_by_number.get(target_number):
                return existing_output

            new_output = OutputBin(target_number)

            self.output_bins_by_number[target_number] = new_output

            return new_output

        raise Exception(f"Failed to create entity for target_type: {entity_type}")

    def get_or_assign_bot(self, target_number: str):
        if existing_bot := self.bots_by_number.get(target_number):
            return existing_bot

        new_bot = Bot(int(target_number))

        self.bots_by_number[target_number] = new_bot

        return new_bot
