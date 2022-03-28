from email.policy import default
import click
import json
import os
from PyInquirer import prompt
import keyboard

@click.command()
@click.option('--prompt', '-p', is_flag=True, help='Prompt for warp point')
def cli(prompt):
    """List all the things!"""
    try:
        with open(os.getenv('APPDATA')+"/vortexcli/vortex.json", 'r') as f:
            data = json.load(f)
        
        if prompt:
            val=[
                    {
                        'type': 'list',
                        'name': 'name',
                        'message': 'Where to Warp?',
                        'choices': data.keys(),
                        'filter': lambda val: val.lower()
                    },
                ]
            l=prompt(val)
            location=data[l['name']]
            keyboard.write(f'cd {location} \n')
            
        else:
            for i in data:
                print(f'{i} : {data[i]}')
        
    except FileNotFoundError:
        click.echo("No warp points have been set!")