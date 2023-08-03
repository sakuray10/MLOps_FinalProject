import pytest
import click
from click.testing import CliRunner
from main import predict

# test function for github actions
def test():
    runner = CliRunner()
    text = "This is a good review"
    results = runner.invoke(predict, ['--text', text])
    results = results.output.split(":")
    results = results[1].split("}")
    print(results[0])
    assert int(results[0]) in [0, 1]

if __name__ == "__main__":
    test()