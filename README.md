# Chicago's Safe Passage Program to Prevent Crime: Is It Worth the Dime?
**ATTENTION**: This is a work in progress and subject to major changes.


This repository contains an analysis of the effect of Chicago's Safe Passage program on violent crime counts along the guarded routes. The before mentioned program aims at keeping the students safe on their way to school. The policy evaluation is one of two parts of my master thesis (2018) at the University of Zurich under the supervision of [Prof. Pietro Biroli](https://sites.google.com/site/pietrobiroli/home). The second one is [A Basic Guide to Reproducible Research](https://binste.github.io/basic_reproducibility_guide/), where this analysis serves as an example.

The empirical approach chosen for this analysis follows one of the specifications in a paper called ["Do More Eyes on the Street Reduce Crime? Evidence from Chicago’s Safe Passage Program"](https://ignaciomsarmiento.github.io/assets/Safe_Passage_WP.pdf) by Daniel McMillen, Ignacio Sarmiento-Barbieri, and Ruchi Singh from June 22, 2017. It can therefore be seen as an attempt to replicate some of their main findings.

Head over to the [website](https://binste.github.io/chicago_safepassage_evaluation/) of this project, to get an introduction into the topic and a summary of the results.

For a more detailed description of the data used, the empirical strategy as well as its limitations, see the Appendix (XXX)

## Replicate analysis
Using the two badges below, you can replicate the last stages of the analysis directly in your browser without any setup required.


Main figures and results: [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binste/chicago_safepassage_evaluation/master?filepath=notebooks%2F5_analysis%2F0.0-binste-replication-of-crime-results-McMillen-et-al-2017-census-block-level.ipynb)


Additional figures: [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binste/chicago_safepassage_evaluation/master?filepath=notebooks%2F5_analysis%2F1.0-binste-additional-figures-website.ipynb)


### Repo2docker
Due to resource constraints on the above used service, to run the whole analysis starting out from the raw data files, you can use the amazing tool repo2docker. It will copy the repository on your own computer and setup everything for you in an isolated environment (using docker).

1. Install the [Docker Community Edition](https://store.docker.com/search?type=edition&offering=community)
2. Install repo2docker: `pip install jupyter-repo2docker`
3. Build and launch docker image of GitHub repository: `jupyter-repo2docker https://github.com/binste/chicago_safepassage_evaluation`
4. After it run through, there is an URL which will lead you to a Jupyter notebook server in the root directory of the project.

If it does not work, go into Docker preferences and increase resources. XXX what do I have?

### Workflow
You should now be able to run all the notebooks in the folder `notebooks`. The notebook in the folder `0_download_data` will by default only download the crime dataset, as all others are already provided. The crime dataset is over 1.5 GB and could therefore not be hosted on GitHub. However, it should not change much for the years used in this analysis and therefore a download from the original source should work.

The notebooks can be run in order of their numbers. To run a whole folder at a time, you can use the Python script `run_ipynb.py` which resides in the root folder of the project. In the "Home" view of Jupyter notebook (where you can open files), click on the top right on "New" -> "Terminal". Now you should be able to run the following command to rerun the whole analysis from the raw data files to the end results:

```bash
python run_ipynb.py 0_download_data 1_prepare_data 2_crime_database 3_match 4_combine_for_analysis 5_analysis
```

This can take up to multiple hours, depending on your hardware!

I used a MacBook Pro 3.1 GHz Intel Core i5 with 16 GB RAM.