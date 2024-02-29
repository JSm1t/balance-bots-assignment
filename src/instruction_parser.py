from src.executor import Executor


class InstructionParser:
    def __init__(self, executor: Executor, filename="input.txt") -> None:
        self.filename = filename
        self.executor = executor

    def parse(self):
        with open(self.filename, "r", encoding="UTF-8") as file:
            print("--- Started parsing lines ---")

            while line := file.readline():
                sanitized_line = line.replace("\n", "")

                words_per_line = sanitized_line.split(" ")

                if not words_per_line:
                    continue

                # Instruction for bot
                if words_per_line[0] == "bot":
                    self.executor.assign_bot_instruction(
                        bot_number=words_per_line[1],
                        low_instruction_type=words_per_line[5],
                        low_instruction_number=words_per_line[6],
                        high_instruction_type=words_per_line[10],
                        high_instruction_number=words_per_line[11],
                    )

                    continue

                # Value assignment to bot
                if words_per_line[0] == "value":
                    self.executor.assign_microchip_value(
                        bot_number=words_per_line[5], value_number=words_per_line[1]
                    )

                    continue

                print("--- Could not parse line: ---")
                print(line)
                print("--- End line ---")

            print("--- Finished parsing lines ---")
