import click
import json
import os
import PyInquirer

@click.command()
@click.argument('name', default=None)
def cli(name):
    """
    Remove a warp point
    """
    try:
        with open(os.getenv('APPDATA')+"/vortexcli/vortex.json", 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        click.echo("No warp points have been set!")
        return

    if name is None:
                name=PyInquirer.prompt([
                    {
                        'type': 'list',
                        'name': 'name',
                        'message': 'Which warp point do you want to remove?',
                        'choices': list(data.keys())
                    }
                ])['name']

    if name in data:
        del data[name]
    else:
        click.echo("No warp point with that name exists!")
        exit()          
    with open(os.getenv('APPDATA')+"/vortexcli/vortex.json", 'w') as f:
        json.dump(data, f, indent=4)
    click.echo(f'{name} has been removed from the list!')
