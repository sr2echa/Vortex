import click
import keyboard
import json
from fuzzyfinder import fuzzyfinder
import os
import PyInquirer

@click.command()
@click.argument('name' , default=None)
def cli(name):
    """hi i am sree"""
    try:
        with open(os.getenv('APPDATA')+"/vortexcli/vortex.json") as f:
            cmds = json.load(f)
        if name is None:
            name=PyInquirer.prompt([
                {
                    'type': 'list',
                    'name': 'name',
                    'message': 'Which warp point do you want to warp to?',
                    'choices': list(cmds.keys())
                }
            ])['name']

        if name in cmds:
            keyboard.write(f'cd {cmds[name]}')
            keyboard.press_and_release('enter')
        else:
            result = fuzzyfinder(name, cmds.keys())
            result=list(result)
            if len(result)>0:
                click.echo("Did you mean: ")
                for i in result:print(i)
            else:
                click.echo("No warp point with that name exists!")
    except FileNotFoundError:
        print("No warp points have been set!")
