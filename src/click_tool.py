import click


@click.group()
def cli():
    """Невеликий CLI на click."""


@cli.command()
@click.option("--name", required=True, help="Ім'я, яке потрібно вивести.")
def say(name):
    """Виводить ім'я, якщо воно не починається з літери p/P."""
    if name.lower().startswith("p"):
        click.echo("Ім'я не підходить.")
    else:
        click.echo(name)


if __name__ == "__main__":
    cli()
