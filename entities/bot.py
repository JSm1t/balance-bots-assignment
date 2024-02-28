from typing import Callable


class Bot:
    number: int
    instructions: list[tuple]
    microchips: list[int]

    def __init__(self, number) -> None:
        self.number = number
        self.instructions = []
        self.microchips = []

    def assign_instruction(
        self,
        low_instruction: Callable[[int], None],
        high_instruction: Callable[[int], None],
    ) -> None:
        self.instructions.append((low_instruction, high_instruction))

        self.check_microchips()

    def assign_microchip(self, microchip_value: int) -> None:
        self.microchips.append(microchip_value)

        self.check_microchips()

    def check_microchips(self):
        if len(self.microchips) > 1:
            self.execute_next_instruction()

    def execute_next_instruction(self) -> None:
        if not self.instructions:
            print(f"No instructions available for bot {self.number}")

            return

        instruction_to_execute = self.instructions.pop(0)

        self.microchips.sort()

        print(f"bot {self.number} is comparing microchips {self.microchips}")

        instruction_to_execute[0](self.microchips[0])
        instruction_to_execute[1](self.microchips[1])

        self.microchips = []
