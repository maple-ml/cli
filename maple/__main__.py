import subprocess
import shutil
import click
import sys
import os

def maple_log(string=None, *args):
    if string:
        print(f"maple >>> {string}", *args)
    else:
        print()

cwd = os.getcwd()

@click.group()
def maple():
    pass

@maple.command()
@click.option("--quiet", "-Q", default=False, is_flag=True, help="Runs quietly")
@click.option("--run", "-R", default=False, is_flag=True, help="Runs GeometryDash.exe after dll is copied")
@click.option("--copy", "-C", is_flag=True, help="Whether to copy the dll to the mods director near GeometryDash.exe")
@click.option("--path", "-P", "gdpath", help="Path to Geometry Dash (in place of %GDPATH%)")
@click.option("--dll", "-D", "dllpath", help="Path to the dll (optional)", default="cinnamon")
def build(quiet, run, copy, gdpath=None, dllpath="cinnamon.dll"):
    args = ""
    
    maple_log("Building cinnamon. Please wait...")
    maple_log() # space
    
    args += " -- /verbosity:quiet /p:WarningLevel=1" if quiet else ""
    
    code = os.system(f"cmake --build build32 --config Release {args}")
    
    if code != 0:
        maple_log("Build failed.")
        maple_log("Exiting")
        return exit(1)
    
    if copy and (os.getenv("GDPATH") or gdpath):
        # cmd line arg has higher priority if both
        path = gdpath if gdpath else os.getenv("GDPATH")
        
        built_dllpath = cwd + f"/build32/Release/{dllpath}"
    
        maple_log(f"Copying .dll file to {path}...")
        #os.remove(path + f"mods/{dllpath}")
        shutil.move(built_dllpath, path + f"/mods/{dllpath}")
        maple_log("Done!")
        
    
    if run and (os.getenv("GDPATH") or gdpath):
        path = gdpath if gdpath else os.getenv("GDPATH")
        
        maple_log("Starting game...")
        subprocess.call([path + "/GeometryDash.exe"], cwd=path)
        maple_log("Game started.")
    elif run:
        maple_log("%GDPATH% or --path must be defined to run the game.")

# command for creating bindings
@maple.command()
def bind():
    if not os.path.exists("vanilla") or not os.path.exists("vanilla/vanilla/main.py"):
        maple_log("Couldn't find the bindings directory, are you in the right directory?")
        return exit(1)

    maple_log("Creating bindings...")

    code = os.system(f"{sys.executable} vanilla/vanilla/main.py")
    
    if code == 0:
        # success
        maple_log("Done! Bindings generated successfully.")
    else:
        maple_log("Failed to create bindings.")
        exit(code)


if __name__ == "__main__":
    maple()
