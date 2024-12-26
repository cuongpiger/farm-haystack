import click

from farm_haystack import __version__
from farm_haystack.cli.prompt import prompt


@click.group()
@click.version_option(__version__)
def main_cli():
    pass


main_cli.add_command(prompt)


def main():
    main_cli()
