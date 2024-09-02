import click
import sys
import json

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help', 'help'])

@click.command()
@click.argument('input', type=click.File('r'), default=sys.stdin)
@click.option(
    "--indent",
    prompt="indentation level: ",
    help="indentation level (2, 4, 8 spaces)"
)
@click.option(
    "--sort",
    help="boolean"
)
@click.option(
    "--file",
    prompt="json file to read: ",
    help="file with content in json format"
)
def cli(input, indent, sort, file):
    """
    command line tool that will format JSON data. 
    The tool will take JSON input as stdin and output formatted JSON to stdout. 
    The tool will also support a --file option that will allow the user to specify a file to read JSON from.
    Examples:\n
    echo '{"json":"obj"}' | python jsoncli.py --indent 4 --sort false\n

    python jsoncli.py --file mp_films.json --sort true --indent 2
    """
    click.echo(f"indent: {indent}, sort: {sort}, file: {file}")
    if not file is None:
        with open(file, 'r') as reader:
            content = reader.read()
    else:    
        content = input.read()
    click.echo(content)

    json_val = json.loads(content)
    i_indent = int(indent)
    b_sort = (sort == "true") or (sort == "True")
    print(json.dumps(json_val, sort_keys=b_sort, indent=i_indent))

if __name__ == '__main__':
    cli()
