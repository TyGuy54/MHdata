import click
from MHFUdata.sql.build import build_database

@click.command()
def main():
    build_database()
    click.echo(click.style('Finished Making Database', fg='green'))

if __name__ == "__main__":
    main()