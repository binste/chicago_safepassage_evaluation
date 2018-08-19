 # Chicago's Safe Passage Program to Prevent Crime: Is It Worth the Dime?<!-- omit in toc -->
- [Overview](#overview)
- [Software environment](#software-environment)
- [Hardware](#hardware)
- [Data](#data)
- [Order of execution](#order-of-execution)
- [Analysis notebooks](#analysis-notebooks)
- [How to run it](#how-to-run-it)
    - [Run it in a conda environment](#run-it-in-a-conda-environment)
    - [Run it in a Docker container](#run-it-in-a-docker-container)

## Overview
This repository contains an example project for [A Basic Guide to Reproducible Research](https://binste.github.io/basic_reproducibility_guide/). It is an analysis of the effect of Chicago's Safe Passage program on crime counts. The program aims at keeping students safe on their way to school by posting civilian guards along various routes to the participating schools. The empirical approach chosen for the analysis follows one of the specifications in the working paper ["Do More Eyes on the Street Reduce Crime? Evidence from Chicago’s Safe Passage Program"](https://ignaciomsarmiento.github.io/assets/Safe_Passage_WP.pdf) by Daniel McMillen, Ignacio Sarmiento-Barbieri, and Ruchi Singh from June 22, 2017. The analysis aims to replicate some of their results. For more information on the replication, as well as an introduction on the topic and a summary of the analysis and the results, see the corresponding [website](https://binste.github.io/basic_reproducibility_guide/example_project/introduction).

This policy evaluation is part of my master thesis (2018) at the University of Zurich under the supervision of [Prof. Pietro Biroli](https://sites.google.com/site/pietrobiroli/home).

## Software environment
The data preparation was done in Python using Jupyter notebooks. R was used for the estimation of the Poisson regression. Details on the exact versions as well as additional packages can be found in the [`environment.yml`](environment.yml) file, which can also be used to recreate the conda environment used to create this analysis. As an operating system, macOS High Sierra 10.13.5 was used.

## Hardware
The analysis was developed on a 3.1 GHz Intel Core i5 with 16 GB RAM. However, a reproduction of the results was tested and worked with only 10 GB RAM in a Docker container.

## Data
With the exception of the crime dataset, all raw data files are provided under `data/raw`. The crime dataset is over 1.5 GB and could therefore not be hosted on GitHub. However, the notebook in the folder `0_download_data` will by default download it for you and put it in the correct folder. The information on crimes should not change much for the years used in this analysis and a download from the original source should work. Note, however, that the results still might vary slightly if you reproduce this due to the download of the crimes dataset. If you want exactly the same crimes dataset as I have, open up a GitHub issue and I can look into it.

Some of the processed datasets are included. However, the dataset used to estimate the Poisson regressions (`est_df`) could, due to its size, not be uploaded to GitHub. It will be reproduced if you follow the order of execution explained in the following section.

For a detailed description of all data sources used, see the section "Data" in the [Appendix](https://github.com/binste/chicago_safepassage_evaluation/blob/master/reports/appendix/Appendix.pdf).

## Order of execution
To reconstruct the results starting out from the raw data, run all notebooks in the `notebooks` folders in the order of their numbering. No other scripts have to be run apart from the notebooks. The `src` folder contains scripts with only functions, which are imported by the notebooks.

Should you want to run the whole pipeline with one command, you can do this using the Python script `run_ipynb.py` which resides in the root folder of the project:
```bash
python run_ipynb.py 0_download_data 1_prepare_data 2_set_up_crime_database 3_match_datasets 4_combine_for_analysis 5_analysis
```
Note however, that this will not give you much of an indication on the progress of the computations, you'll only see the name of the notebook currently processed. This can take up to multiple hours, depending on your hardware.

## Analysis notebooks
As the analysis notebooks are probably of the most interest (they produce the main figures and results), the main two are briefly described in the following. They can be found in the folder `notebooks/5_analysis`.

| Notebook | Description |
| -------- | ----------- |
| `0.0-binste-estimation-poisson.ipynb` | Estimates all the Poisson regressions for both violent and property crimes and saves models as well as results into the folder `model`. [![nbviewer](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/binste/chicago_safepassage_evaluation/blob/master/notebooks/5_analysis/0.0-binste-estimation-poisson.ipynb)|
| `1.0-binste-analyze-crime-results-census-block-level.ipynb` | Replicates Figure 3, Figure A.2, Table 1, and Table 10 (column 3 and 7) from McMillen et al. (2017) and compares them to the originals. The notebook also produces additional figures for the website. [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binste/chicago_safepassage_evaluation/master?filepath=notebooks%2F5_analysis%2F1.0-binste-analyze-crime-results-census-block-level.ipynb) [![nbviewer](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/binste/chicago_safepassage_evaluation/blob/master/notebooks/5_analysis/1.0-binste-analyze-crime-results-census-block-level.ipynb)|

> **Tip**: To view static versions of the Jupyter notebooks in your browser, you can paste their URL into [Jupyter nbviewer](http://nbviewer.jupyter.org/).

## How to run it
If you are not sure how to set up the software specified in `environment.yml` to rerun the analysis, you can use one of the following two options:

### Run it in a conda environment
Download the repository as .zip file from GitHub and unpack it or clone it using:
```bash
git clone https://github.com/binste/chicago_safepassage_evaluation
```
and then install and activate the conda environment by running:
```bash
conda env create -f environment.yml
conda activate speval
```
Now start a Jupyter notebook server in the root directory of the project:
```bash
jupyter notebook
```
See [Order of execution](#order-of-execution) on how to proceed.

This approach should give you the exact same Python and R version as well as the same versions of the main packages used. However, system dependencies might differ and I was not able to test it on a Windows machine.

### Run it in a Docker container
Should you have problems with the above approach due to your operating system, you can also run the analysis in a tested and operating-system-independent environment (using Docker). In the following, I will explain all the necessary steps and use the amazing tool repo2docker, which will copy the repository to your own computer and setup everything for you.

1. Install the [Docker Community Edition](https://store.docker.com/search?type=edition&offering=community) for your operating system
2. Set the available memory for Docker to 10 GB and the number of CPU cores to 2.
    * On Mac this can be set by clicking on the Docker symbol in the status bar -> Preferences -> Advanced
3. Install repo2docker from source to get the latest version:
    ```bash
    git clone https://github.com/jupyter/repo2docker.git
    cd repo2docker
    pip install -e .
    ```
4. Build and launch Docker image of GitHub repository:
    ```bash
    jupyter-repo2docker https://github.com/binste/chicago_safepassage_evaluation
    ```
5. After it run through, there is an URL, which will lead you to a running Jupyter notebook server. There is currently a bug with Jupyter notebooks and Docker, where the displayed URL might not work without a slight modification. To fix it, change the host name before the port to `127.0.0.1`. Example: `http://d2f78b8191fd:55484/?token=...` becomes `http://127.0.0.1:55484/?token=...`.

See [Order of execution](#order-of-execution) on how to proceed.
