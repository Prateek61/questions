from typer.testing import CliRunner
from main import app

runner = CliRunner()

def test_parse():
    result = runner.invoke(app, ["parse", "rawquestions/CT501-OOP/1", "--show", "--remove-tags"])
    print(result.stdout)

if __name__ == "__main__":
    test_parse()
