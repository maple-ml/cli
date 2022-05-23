import click
import os

cwd = os.getcwd()

@click.group()
def maple():
    pass

@maple.command()
@click.option("--quiet", default=False)
def build(quiet):
    args = ""
    
    print("Building cinnamon. Please wait...")
    print() # space
    
    args += " -- /verbosity:quiet" if quiet else ""
    
    os.system(f"cmake --build build32 --config Release {args}")

if __name__ == "__main__":
    maple()