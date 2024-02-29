from pytest_mock import MockerFixture

from src.entities.bot import Bot


class TestAssignInstruction:
    def test_assign_instruction_bot_has_2_chips(self, mocker: MockerFixture):
        test_bot = Bot(0)
        test_bot.microchips = [3, 2]

        low_instruction_mock = mocker.Mock()
        high_instruction_mock = mocker.Mock()

        test_bot.assign_instruction(
            low_instruction=low_instruction_mock, high_instruction=high_instruction_mock
        )

        low_instruction_mock.assert_called_once_with(2)
        high_instruction_mock.assert_called_once_with(3)

        assert test_bot.microchips == []

    def test_assign_instruction_bot_has_not_2_chips(self, mocker: MockerFixture):
        test_bot = Bot(0)
        test_bot.microchips = [1]

        low_instruction_mock = mocker.Mock()
        high_instruction_mock = mocker.Mock()

        test_bot.assign_instruction(
            low_instruction=low_instruction_mock, high_instruction=high_instruction_mock
        )

        low_instruction_mock.assert_not_called()
        high_instruction_mock.assert_not_called()

        assert test_bot.microchips == [1]


class TestAssignMicrochip:
    def test_assign_microchip_bot_gets_2_chips(self, mocker: MockerFixture):
        test_bot = Bot(0)
        test_bot.microchips = [3]

        low_instruction_mock = mocker.Mock()
        high_instruction_mock = mocker.Mock()

        test_bot.instructions = [(low_instruction_mock, high_instruction_mock)]

        test_bot.assign_microchip(5)

        low_instruction_mock.assert_called_once_with(3)
        high_instruction_mock.assert_called_once_with(5)

        assert test_bot.microchips == []
        assert test_bot.instructions == []

    def test_assign_instruction_bot_has_not_2_chips(self, mocker: MockerFixture):
        test_bot = Bot(0)
        test_bot.microchips = []

        low_instruction_mock = mocker.Mock()
        high_instruction_mock = mocker.Mock()

        test_bot.instructions = [(low_instruction_mock, high_instruction_mock)]

        test_bot.assign_microchip(5)

        low_instruction_mock.assert_not_called()
        high_instruction_mock.assert_not_called()

        assert test_bot.microchips == [5]
        assert len(test_bot.instructions) == 1

    def test_assign_instruction_bot_gets_2_chips_no_instructions(self):
        test_bot = Bot(0)
        test_bot.microchips = [4]

        test_bot.assign_microchip(2)

        assert test_bot.microchips == [4, 2]
