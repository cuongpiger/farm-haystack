import click

from farm_haystack.cli.prompt import fetch


@click.group(short_help="Prompts related commands")
def prompt():
    pass


prompt.add_command(fetch.fetch)
