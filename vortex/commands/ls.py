import click
import json
import os

@click.command()
@click.argument('name')
def cli(name):
    with open(os.getenv('APPDATA')+"/vortexcli/vortex.json") as f:
        cmds = json.load(f)
    if name in cmds:
        os.system(f'cd {cmds[name]}')
        os.system('powershell ls')
    else:
        click.echo("No warp point with that name exists!")