import pytest
from mathinterpreter.calculate import calculate


class TestCalculate:

    def test_numbers(self):
        value = calculate("51.2")
        assert value == "51.2"

    def test_expression(self):
        value = float(calculate("0 + 10/3"))
        pytest.approx(value, 3.33, 2)
