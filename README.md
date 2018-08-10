# Chicago's Safe Passage Program to Prevent Crime: Is It Worth the Dime?
**ATTENTION**: This is a work in progress and subject to major changes.


This repository contains the code and data for an analysis of the effect of Chicago's Safe Passage program on violent crime counts along the guarded routes. The before mentioned program aims at keeping the students safe on their way to school. An introduction on the topic and a summary of the results can be found on the corresponding [website](https://binste.github.io/chicago_safepassage_evaluation/).

The policy evaluation is one of two parts of my master thesis (2018) at the University of Zurich under the supervision of [Prof. Pietro Biroli](https://sites.google.com/site/pietrobiroli/home). The second one is [A Basic Guide to Reproducible Research](https://binste.github.io/basic_reproducibility_guide/), where this analysis serves as an example.

The empirical approach chosen for this analysis follows one of the specifications in the working paper ["Do More Eyes on the Street Reduce Crime? Evidence from Chicago’s Safe Passage Program"](https://ignaciomsarmiento.github.io/assets/Safe_Passage_WP.pdf) by Daniel McMillen, Ignacio Sarmiento-Barbieri, and Ruchi Singh from June 22, 2017. It is an attempt to replicate their main finding of a significant reduction in violent crime due to the Safe Passage program.

For a more detailed description of the data used, the empirical strategy as well as its limitations, see the Appendix (XXX).

## Replicate analysis
### Figures for website and comparison to McMillen et al. (2017)
By clicking on the badge below, you can replicate the figures used on the website analysis directly in your browser without any setup required and compare the results to the ones of McMillen et al. (2017).

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binste/chicago_safepassage_evaluation/master?filepath=notebooks%2F5_analysis%2F1.0-binste-analyze-crime-results-census-block-level.ipynb)


### Run analysis on your own machine
#### If just want to try out some things in a self-contained and isolated environment
Due to resource constraints on the above used service, to run the estimations of the poisson regressions or even start out from the raw data files, you need to do this on your local machine. However, this is rather convenient with the amazing tool repo2docker. It will copy the repository on your own computer and setup everything for you in an isolated environment (using Docker).

1. Install the [Docker Community Edition](https://store.docker.com/search?type=edition&offering=community) for your operating system
2. Set the available memory for Docker to 4GB.
    * On Mac this can be set by clicking on the Docker symbol in the status bar -> Preferences -> Advanced
2. Install repo2docker: `pip install jupyter-repo2docker`
    * The easiest way to get pip is to install a recent version of Python. Else, see the [official installation guide](https://pip.pypa.io/en/stable/installing/).
3. Build and launch docker image of GitHub repository:
    * `jupyter-repo2docker https://github.com/binste/chicago_safepassage_evaluation`
4. After it run through, there is an URL which will lead you to a Jupyter notebook server in the root directory of the project.

However, if you are not familiar with Docker, it is not straightforward to save any changes you make to a notebook etc.

#### If you want to continue working on this project
If you want to continue working on this project, your best option might be to clone the repository by running
```bash
git clone https://github.com/binste/chicago_safepassage_evaluation
```
And then install and activate the conda environment by running
```bash
conda env create -f environment.yml
source activate speval
```

This will give you the exact same Python version as well as the same package versions for the main packages used.

I was not able to test this approach on a Windows machine, whereas the Docker approach mentioned above will work their too.

### Data
For a detailed description of all data sources used, see the section "Data" in the Appendix (XXX).

With the exception of the crime dataset, all raw data files are provided under `data/raw`. The crime dataset is over 1.5 GB and could therefore not be hosted on GitHub. However, the notebook in the folder `0_download_data` will by default download it for you and put it in the correct folder. More on the exact order of execution in the next section The information on crimes should not change much for the years used in this analysis and therefore a download from the original source should work.

### Order of execution
To reconstruct the results starting out from the raw data, run all notebooks in the `notebooks` folders in order of their numbering. No other scripts have to be run apart from the notebooks. Should you want to run the whole pipeline with one command you can do this using the Python script `run_ipynb.py` which resides in the root folder of the project. Note however, that this will not give you much of an indication on the progress of the computations, you'll only see the name of the notebook currently processed. In the "Home" view of Jupyter notebook (where you can open files), click on the top right on "New" -> "Terminal". Now you should be able to run the following command to rerun the whole analysis from the raw data files to the end results:

```bash
python run_ipynb.py 0_download_data 1_prepare_data 2_crime_database 3_match 4_combine_for_analysis 5_analysis
```

This can take up to multiple hours, depending on your hardware.

### Hardware
I used a MacBook Pro (macOS High Sierra 10.13.5) 3.1 GHz Intel Core i5 with 16 GB RAM to develop the project. No graphic card is needed. The end results were also tested and replicated in a Docker container, as explained above.
