import click
import os
import json
import PyInquirer

@click.command()
@click.argument('name')
@click.argument('location', default=os.getcwd(), type=click.UNPROCESSED)
def cli(name, location):
    """Set a warp point"""
    if not os.path.exists(os.getenv('APPDATA')+"/vortexcli/"):
        #make a file if it doesn't exist
        os.makedirs(os.getenv('APPDATA')+"/vortexcli/")
        with open(os.getenv('APPDATA')+"/vortexcli/vortex.json", 'w') as f:
            pass
        with open(os.getenv('APPDATA')+"/vortexcli/vortex.json", 'w') as f:
            json.dump({}, f, indent=4)

    with open(os.getenv('APPDATA')+"/vortexcli/vortex.json", 'r') as f:
        data = json.load(f)
    if name in data:
        preference=PyInquirer.prompt([
            {
                'type': 'confirm',
                'name': 'overwrite',
                'message': 'This warp point already exists. Overwrite?',
                'default': False
            }
        ])
        if preference['overwrite']:
            pass
        else:
            click.echo("Warp point not set")
            return

    data[name] = location
    with open(os.getenv('APPDATA')+"/vortexcli/vortex.json", 'w') as f:
        json.dump(data, f, indent=4)
    click.echo(f'{name} has been set to {location}!')

    