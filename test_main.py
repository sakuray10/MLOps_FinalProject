import pytest
from click.testing import CliRunner
from main import predict

def test():
    results = predict("this is a good review!")
    print(results)
    assert int(results[-2]) in [0, 1]

if __name__ == "__main__":
    test()