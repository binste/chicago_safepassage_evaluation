 # Chicago's Safe Passage Program to Prevent Crime: Is It Worth the Dime?<!-- omit in toc -->

**ATTENTION**: This is a work in progress and subject to major changes.

- [Overview](#overview)
- [Software environment](#software-environment)
- [Hardware](#hardware)
- [Data](#data)
- [Order of execution](#order-of-execution)
- [Analysis notebooks](#analysis-notebooks)

## Overview
This repository contains an example project for [A Basic Guide to Reproducible Research](https://binste.github.io/basic_reproducibility_guide/). It is an analysis of the effect of Chicago's Safe Passage program on crime counts. The program aims at keeping students safe on their way to school by posting civilian guards along various routes to the participating schools. The empirical approach chosen for the analysis follows one of the specifications in the working paper ["Do More Eyes on the Street Reduce Crime? Evidence from Chicago’s Safe Passage Program"](https://ignaciomsarmiento.github.io/assets/Safe_Passage_WP.pdf) by Daniel McMillen, Ignacio Sarmiento-Barbieri, and Ruchi Singh from June 22, 2017, and is an attempt to replicate their findings. For more information on the replication, as well as an introduction on the topic and a summary of the analysis and the results, see the corresponding [website](https://binste.github.io/basic_reproducibility_guide/example_project/introduction).

This policy evaluation is part of my master thesis (2018) at the University of Zurich under the supervision of [Prof. Pietro Biroli](https://sites.google.com/site/pietrobiroli/home).

## Software environment
The data preparation was done in Python using Jupyter notebooks. R was used for the estimation of the Poisson regression. Details on the exact versions as well as additional packages can be found in the [`environment.yml`](environment.yml) file. As an operating system, macOS High Sierra 10.13.5 was used.

> **Note**: This repository is [repo2docker](https://github.com/jupyter/repo2docker) compatible.

## Hardware
The analysis was developed on a 3.1 GHz Intel Core i5 with 16 GB RAM. However, a reproduction of the results was tested and worked with only XXX GB RAM in a Docker container (see [this section](#run-it-in-a-docker-container) for details).

## Data
With the exception of the crime dataset, all raw data files are provided under `data/raw`. The crime dataset is over 1.5 GB and could therefore not be hosted on GitHub. However, the notebook in the folder `0_download_data` will by default download it for you and put it in the correct folder. The information on crimes should not change much for the years used in this analysis and therefore a download from the original source should work.

Some of the processed datasets are included. However, the dataset used to estimate the Poisson regressions (`est_df`) could, due to its size, not be uploaded to GitHub. It will be reproduced if you follow the order of execution explained in the following section.

For a detailed description of all data sources used, see the section "Data" in the Appendix (XXX).

## Order of execution
To reconstruct the results starting out from the raw data, run all notebooks in the `notebooks` folders in order of their numbering. No other scripts have to be run apart from the notebooks. The `src` folder does contain scripts with only functions, which are imported by the notebooks.

Should you want to run the whole pipeline with one command you can do this using the Python script `run_ipynb.py` which resides in the root folder of the project. Note however, that this will not give you much of an indication on the progress of the computations, you'll only see the name of the notebook currently processed. In the "Home" view of Jupyter notebook (where you can open files), click on the top right on "New" -> "Terminal". Now you should be able to run the following command to rerun the whole analysis from the raw data files to the end results:
```bash
python run_ipynb.py 0_download_data 1_prepare_data 2_set_up_crime_database 3_match_datasets 4_combine_for_analysis 5_analysis
```
This can take up to multiple hours, depending on your hardware.

## Analysis notebooks
As the analysis notebooks are probably of the most interest, as they produce the main figures and results, the main two are briefly described in the following. They can be found in the folder `notebooks/5_analysis`.

| Notebook | Description |
| -------- | ----------- |
| `0.0-binste-estimation-poisson.ipynb` | Estimates all the Poisson regressions for both violent and property crimes and saves models as well as results into the folder `model`. [![nbviewer](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/binste/chicago_safepassage_evaluation/blob/master/notebooks/5_analysis/0.0-binste-estimation-poisson.ipynb)|
| `1.0-binste-analyze-crime-results-census-block-level.ipynb` | Replicates Figure 3, Figure A.2, Table 1, and Table 10 (column 3 and 7) from McMillen et al. (2017) and compares them to the originals. The notebook also produces additional figures for the website. [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binste/chicago_safepassage_evaluation/master?filepath=notebooks%2F5_analysis%2F1.0-binste-analyze-crime-results-census-block-level.ipynb) [![nbviewer](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/binste/chicago_safepassage_evaluation/blob/master/notebooks/5_analysis/1.0-binste-analyze-crime-results-census-block-level.ipynb)|

> **Tip**: To view static versions of the Jupyter notebooks in your browser, you can paste their URL into [Jupyter nbviewer](http://nbviewer.jupyter.org/).