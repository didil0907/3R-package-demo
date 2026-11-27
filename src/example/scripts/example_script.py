"""CLI script for the example package. This will be called on the command line"""

import click

from example.demo_module import build_pyramid


@click.command()
@click.option(
    "--height",
    type=int,
    prompt="Pyramid height",
    help="Number of levels for the pyramid",
)
@click.version_option()
def example_cli(height):
    """Print a star pyramid with the specified height."""
    click.echo(build_pyramid(height))