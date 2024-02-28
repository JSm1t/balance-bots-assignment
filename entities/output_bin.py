class OutputBin:
    number: int
    microchips: list[int]

    def __init__(self, number) -> None:
        self.microchips = []
        self.number = number

    def assign_microchip(self, microchip_value):
        self.microchips.append(microchip_value)
