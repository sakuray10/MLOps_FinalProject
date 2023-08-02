import pytest
from click.testing import CliRunner
from main import main


def test():
    results = main()
    assert int(results[-2]) in [0, 1]

if __name__ == "__main__":
    test()