"""Module to ensure that the python venv has been installed correctly

Uses `tomllib` to parse the `pyproject.toml` package and attempt to 
import all required dependenceis.
"""

import importlib
import tomllib
import re

from time import perf_counter

def main():

    pyproject_toml = "./pyproject.toml"

    # Some packages have slightly different string names for the import... will need
    # to update this manually every time some package breaks this script...
    replace_packages = {
        'ipython':'IPython',
        'netcdf4':'netCDF4',
        'scikit-learn':'sklearn'
        }

    with open(pyproject_toml,'rb') as f:

        data = tomllib.load(f)

    num_errors = 0

    print("Verifying project dependencies...")
    for dep in sorted(data['project']['dependencies']):

        pkg = re.split(r'[<>=]',dep)[0]

        if pkg in replace_packages:
            pkg = replace_packages[pkg]

        try:
            importlib.import_module(pkg)
            print(f"  [✓] Package: `{pkg}` imported successfully!")
        except ImportError:
            print(f"  [X] Error importing package: `{pkg}`")
            num_errors += 1

    print("\n")
    if num_errors > 0:
        print("!"*60)
        print("There were errors importing some packages.")
        print("Run the command `uv sync` and then try again...")
        print("!"*60)
    else:
        
        print("-"*60)
        print("All dependencies imported successfully!")

if __name__ == '__main__':
    start_time = perf_counter()
    print("="*60)
    print("Beginning Verification Script...")
    print("-"*60)
    main()
    end_time = perf_counter()
    elapsed = end_time - start_time
    print("\n")
    print(f"Verification Script Complete in {elapsed:.2f} seconds.")
    print("="*60)
