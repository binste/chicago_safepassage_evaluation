"""Runs all Jupyter notebooks in given folders. Folder names (one or multiple)
can be passed as arguments to the script and can be provided relative to the
folder which contains all notebooks (e.g. "notebooks").
Notebooks are run with their enclosing folder as working directory.

Example
-------
If you want to run all Jupyter notebooks in "notebooks/0_prepare_data", run:

$ python run_ipynb.py 0_prepare_data
"""
import sys
from pathlib import Path

import nbformat
from nbconvert.preprocessors import CellExecutionError, ExecutePreprocessor


def validate_input(input_args):
    """Extracts folder names from passed arguments and makes sure that
    they are valid.

    Parameters
    ----------
    input_args : iterable
        All input arguments with the first one being the script name
        (i.e. sys.argv)

    Returns
    -------
    list
        All valid folder names
    """
    # Stops execution of script if no folders are given
    if len(input_args) == 1:
        raise Exception('You need to specify either one or multiple folders ' +
                        f'inside "./{str(notebooks_path)}" to run')
    # If folders are given, first check if they exist, else stop
    folders = [Path(f) for f in input_args[1:]]
    for f in folders:
        if not (notebooks_path / f).is_dir():
            raise Exception(
                f'Folder "{str(notebooks_path / f)}" does not exist.')
    return folders


def run_notebook(nb_wd, nb_path):
    """Runs a given notebook and saves it

    Executes the passed notebook with nb_wd as the working directory.
    If an error occurs during the execution, a message is raised to the user
    and the notebook is saved anyway, including the traceback.

    Parameters
    ----------
    nb_wd : Path or str
        Path to the folder which should be used as a working directory for
        the execution of the notebook

    nb_path : Path or str
        Full path to the notebook which should be run.

    Returns
    -------
    Nothing
    """
    if not isinstance(nb_wd, Path):
        nb_wd = Path(nb_wd)
    if not isinstance(nb_path, Path):
        nb_path = Path(nb_path)
    with nb_path.open() as f:
        nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)

    # Configure notebook execution mode
    # Timeout = None means no restriction on runtime of cells
    ep = ExecutePreprocessor(timeout=None, kernel_name='python3')

    # The code for the following error handling is taken from the
    # official nbconvert documentation:
    # https://nbconvert.readthedocs.io/en/latest/execute_api.html
    try:
        # Run notebook
        out = ep.preprocess(nb, {'metadata': {'path': str(nb_wd)}})
    except CellExecutionError:
        out = None
        msg = f'Error executing the notebook "{str(nb_path)}".\n\n'
        msg += 'See the notebook for the traceback.\n'
        print(msg)
        raise
    finally:
        # Save it. Includes tracebacks should an error have occured.
        with nb_path.open('wt') as f:
            nbformat.write(nb, f)
    return


if __name__ == '__main__':
    # Set path to root directory of notebooks
    notebooks_path = Path('notebooks')
    # Validate input and get folder names
    folders = validate_input(sys.argv)
    # Get sorted list of all notebooks to run
    print('-' * 20)
    print('The following notebooks will be executed in order:')
    print('-' * 20)
    notebooks = []
    for f in folders:
        nb_found = sorted([
            x for x in (notebooks_path / f).iterdir() if x.suffix == '.ipynb'
        ])
        print('\n'.join(str(x) for x in nb_found))
        notebooks.append([f, nb_found])
        print('-' * 20)

    # Run notebooks
    for nb_wd, nb_paths in notebooks:
        for nb_p in nb_paths:
            print(f'Run {str(nb_p)}')
            run_notebook(notebooks_path / nb_wd, nb_p)
        print('-' * 20)
