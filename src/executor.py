from src.entities.bot import Bot
from src.entities.output_bin import OutputBin


class Executor:
    def __init__(self) -> None:
        self.bots_by_number: dict[str, Bot] = {}
        self.output_bins_by_number: dict[str, OutputBin] = {}

    def get_all_bots(self) -> list[Bot]:
        return list(self.bots_by_number.values())

    def get_all_outputs(self) -> list[OutputBin]:
        return list(self.output_bins_by_number.values())

    def assign_bot_instruction(
        self,
        bot_number: str,
        low_instruction_type: str,
        low_instruction_number: str,
        high_instruction_type: str,
        high_instruction_number: str,
    ):
        executing_bot = self.get_or_create_bot(bot_number)

        low_instruction_target = self.get_or_create_target(
            low_instruction_number, low_instruction_type
        )

        high_instruction_target = self.get_or_create_target(
            high_instruction_number, high_instruction_type
        )

        executing_bot.assign_instruction(
            low_instruction=low_instruction_target.assign_microchip,
            high_instruction=high_instruction_target.assign_microchip,
        )

    def assign_microchip_value(
        self,
        bot_number: str,
        value_number: str,
    ):
        executing_bot = self.get_or_create_bot(bot_number)

        executing_bot.assign_microchip(int(value_number))

    def get_or_create_target(self, target_number: str, entity_type: str = "bot"):
        if entity_type == "bot":
            return self.get_or_create_entity(target_number, Bot, self.bots_by_number)

        if entity_type == "output":
            return self.get_or_create_entity(
                target_number, OutputBin, self.output_bins_by_number
            )

        raise Exception(f"Failed to create entity for target_type: {entity_type}")

    def get_or_create_entity(
        self, target_number: str, entity: type[Bot] | type[OutputBin], database: dict
    ) -> Bot | OutputBin:
        if existing_entity := database.get(target_number):
            return existing_entity

        new_entity = entity(int(target_number))

        database[target_number] = new_entity

        return new_entity

    def get_or_create_bot(self, target_number: str) -> Bot:
        return self.get_or_create_entity(target_number, Bot, self.bots_by_number)  # type: ignore
