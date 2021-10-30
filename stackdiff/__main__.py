from stackdiff.cli import entry
from sys import argv, stdout


def cli_entry() -> None:
    exit(entry(cli_args=argv[1:], writer=stdout))


if __name__ == "__main__":
    cli_entry()
