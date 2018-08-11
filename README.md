# Chicago's Safe Passage Program to Prevent Crime: Is It Worth the Dime?
**ATTENTION**: This is a work in progress and subject to major changes.


This repository contains the code and data for an analysis of the effect of Chicago's Safe Passage program on violent crime counts along the guarded routes. The before mentioned program aims at keeping the students safe on their way to school. An introduction on the topic and a summary of this analysis and the results can be found on the corresponding [website](https://binste.github.io/chicago_safepassage_evaluation/).

The policy evaluation is one of two parts of my master thesis (2018) at the University of Zurich under the supervision of [Prof. Pietro Biroli](https://sites.google.com/site/pietrobiroli/home). The second one is [A Basic Guide to Reproducible Research](https://binste.github.io/basic_reproducibility_guide/), where this analysis serves as an example.

The empirical approach chosen for this analysis follows one of the specifications in the working paper ["Do More Eyes on the Street Reduce Crime? Evidence from Chicago’s Safe Passage Program"](https://ignaciomsarmiento.github.io/assets/Safe_Passage_WP.pdf) by Daniel McMillen, Ignacio Sarmiento-Barbieri, and Ruchi Singh from June 22, 2017. It is an attempt to replicate their main finding of a significant reduction in violent crime due to the Safe Passage program.

For a more detailed description of the data used, the empirical strategy as well as its limitations, see the Appendix (XXX).

## Replicate analysis
### Figures for website and comparison to McMillen et al. (2017)
By clicking on the badge below, you can replicate the figures used on the website analysis directly in your browser without any setup required and compare the results to the ones of McMillen et al. (2017).

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binste/chicago_safepassage_evaluation/master?filepath=notebooks%2F5_analysis%2F1.0-binste-analyze-crime-results-census-block-level.ipynb)


### Run analysis on your own machine
Due to resource constraints on the above used service, to run the estimations of the poisson regressions or even start out from the raw data files, you need to do this on your local machine. You might want to choose one of the following two options, depending on your knowledge and your goal.

#### Set up a conda environment
If you want to continue working on this project, your best option might be to clone the repository:
```bash
git clone https://github.com/binste/chicago_safepassage_evaluation
```
and then install and activate the conda environment by running:
```bash
conda env create -f environment.yml
source activate speval
```
Now start a Jupyter notebook server in the root directory of the project:
```bash
jupyter notebook
```
See [Order of execution](#order-of-execution) on how to proceed.

This approach should give you the exact same Python and R version as well as the same versions of the main packages used. However, system dependencies might differ and I was not able to test it on a Windows machine. Should you experience any problem with this, you might want to try out the next approach.

#### Run it in a Docker container
If you want to rerun the analysis in an isolated and tested environment, you can use the amazing tool repo2docker. It will copy the repository on your own computer and setup everything for you in an isolated and OS independent environment (using Docker).

However, if you are not familiar with Docker, it is not straightforward to save any changes you make to a notebook etc.

1. Install the [Docker Community Edition](https://store.docker.com/search?type=edition&offering=community) for your operating system
2. Set the available memory for Docker to 4GB.
    * On Mac this can be set by clicking on the Docker symbol in the status bar -> Preferences -> Advanced
2. Install repo2docker from source to get the latest version:
    ```bash
    git clone https://github.com/jupyter/repo2docker.git
    cd repo2docker
    pip install -e .
    ```
3. Build and launch docker image of GitHub repository:
    ```bash
    jupyter-repo2docker https://github.com/binste/chicago_safepassage_evaluation
    ```
4. After it run through, there is an URL, which will lead you to a running Jupyter notebook server. There is currently a bug, where the displayed URL does not work without a slight modification. Change XXX to XXX.

See [Order of execution](#order-of-execution) on how to proceed.


### Data
For a detailed description of all data sources used, see the section "Data" in the Appendix (XXX).

With the exception of the crime dataset, all raw data files are provided under `data/raw`. The crime dataset is over 1.5 GB and could therefore not be hosted on GitHub. However, the notebook in the folder `0_download_data` will by default download it for you and put it in the correct folder. More on the exact order of execution in the next section The information on crimes should not change much for the years used in this analysis and therefore a download from the original source should work.

Some of the processed datasets are included. However, the dataset used to estimate the Poisson regressions (`est_df`) could, due to its size, not be uploaded to GitHub. It will be reproduced if you follow the order of execution explained in the following.

### Order of execution
To reconstruct the results starting out from the raw data, run all notebooks in the `notebooks` folders in order of their numbering. No other scripts have to be run apart from the notebooks. The `src` folder does contain scripts with only functions, which are imported by the notebooks. Should you want to run the whole pipeline with one command you can do this using the Python script `run_ipynb.py` which resides in the root folder of the project. Note however, that this will not give you much of an indication on the progress of the computations, you'll only see the name of the notebook currently processed. In the "Home" view of Jupyter notebook (where you can open files), click on the top right on "New" -> "Terminal". Now you should be able to run the following command to rerun the whole analysis from the raw data files to the end results:

```bash
python run_ipynb.py 0_download_data 1_prepare_data 2_crime_database 3_match 4_combine_for_analysis 5_analysis
```

This can take up to multiple hours, depending on your hardware.

### Analysis notebooks
As the analysis notebooks are probably of the most interest, as they produce the main figures and results, the main two are briefly described in the following. They can be found in the folder `notebooks/5_analysis`.

| Notebook | Description |
| -------- | ----------- |
| `0.0-binste-estimation-poisson.ipynb` | Estimates all the Poisson regressions for both violent and property crimes and saves models as well as results into the folder `model`.
| `1.0-binste-analyze-crime-results-census-block-level.ipynb` | Replicates Figure 3, Figure A.2, Table 1, and Table 10 (column 3 and 7) from McMillen et al. (2017) and compares them to the originals. The notebook also produces additional figures for the website. |



### Hardware
I used a MacBook Pro (macOS High Sierra 10.13.5) 3.1 GHz Intel Core i5 with 16 GB RAM to develop the project. No graphic card is needed. The end results were also tested and replicated in a Docker container, as explained above.
