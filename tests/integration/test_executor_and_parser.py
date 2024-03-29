from src.executor import Executor
from src.instruction_parser import InstructionParser


def test_instruction_parser():
    executor = Executor()

    InstructionParser(
        executor=executor, filename="./tests/integration/test_instructions.txt"
    ).parse()

    bots = executor.get_all_bots()
    output_bins = executor.get_all_outputs()

    bots.sort(key=lambda bot: bot.number)
    output_bins.sort(key=lambda output_bin: output_bin.number)

    assert len(bots) == 3
    assert bots[0].number == 0
    assert bots[1].number == 1
    assert bots[2].number == 2

    assert output_bins[0].number == 0
    assert output_bins[0].microchips == [5]
    assert output_bins[1].number == 1
    assert output_bins[1].microchips == [2]
    assert output_bins[2].number == 2
    assert output_bins[2].microchips == [3]
