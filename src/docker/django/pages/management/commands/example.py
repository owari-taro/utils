#import djclick as click
import djclick as click

@click.option("--name","-n",type=str,default="django taro!!!!",help="what's your name????")
@click.command(help="this is a django test")
def cmd(name:str):
    print(name,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")