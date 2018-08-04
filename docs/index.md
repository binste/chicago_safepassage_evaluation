---
title: Introduction
---
**ATTENTION**: This is a work in progress and subject to major changes.


This website is one of two parts of my master thesis (2018) at the University of Zurich and presents an evaluation of the effect of Chicago's Safe Passage program on crime.

If you want to follow along with the analysis in a more interactive way, click on [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binste/chicago_safepassage_evaluation/master?filepath=notebooks%2F5_analysis%2F1.0-binste-analyze-crime-results-census-block-level.ipynb){:target="_blank"}, which will allow you to reproduce the final steps in order to obtain the figures used on this website - directly in your browser without any setup needed. If you want to rerun the estimation or even start out from the raw data files, visit the [GitHub repository](https://github.com/binste/chicago_safepassage_evaluation){:target="_blank"} for instructions.

## Crime in Chicago
Chicago notoriously suffers from very high numbers of crimes, where a vast part of the incidents happen in poor neighborhoods on the South and West Sides.[^1] Figure 1 shows, that even though there was a welcome downwards trend for a few years, for both property and violent crimes, this started to inverse around 2014/2015.
{% comment %}
Do the crimes need further definition?
{% endcomment %}

<small>*Figure 1 - Evolution of violent- and property-crime counts over time*</small>
{% include yearly_violent_trend.html %}
<small>*The definition of violent and property crimes follows the [National Incident-Based Reporting System (NIBRS)](http://gis.chicagopolice.org/clearmap_crime_sums/crime_types.html){:target="_blank"} of the Federal Bureau of Investigation (FBI).*<br />
*This is a replication of Figure A.2 in McMillen et al. (2017)[^8]*<br />
*Data source: [Crimes - 2001 to present, Chicago Data Portal; accessed January 25, 2018](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2){:target="_blank"}*</small>

If we looked at a more detailed categorization of violent crimes, we see that the number of homicides in 2017 is even on a higher level than in 2006.

<small>*Figure 2 - Evolution of violent-crime counts over time by subcategories*</small>
{% include violent_FBI.html %}
<small>*Data source: [Crimes - 2001 to present, Chicago Data Portal; accessed January 25, 2018](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2){:target="_blank"}*<br />
*The definition of violent crimes as well as the sub categories follows the [National Incident-Based Reporting System (NIBRS)](http://gis.chicagopolice.org/clearmap_crime_sums/crime_types.html){:target="_blank"} of the Federal Bureau of Investigation (FBI).*</small>

To put it into more graspable numbers: In 2017, on average, every 13 hours a person was murdered and every 2 hours and 30 minutes someone was shot.[^2]

Let us now zoom a bit more into the intra-year and intra-day variation of violent crimes with the figure below.

Note that, if you want to see the intra-day variation in the lower part of the figure calculated with data only for one year, you can select a single year by clicking on a square corresponding to that year in the upper figure. The lower heatmap will adapt accordingly.

<small>*Figure 3 - Intra-year and intra-day variation in violent crimes*</small>
{% include violent_trend.html %}
<small>*Data source: [Crimes - 2001 to present, Chicago Data Portal; accessed January 25, 2018](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2){:target="_blank"}*<br />
*The definition of violent crimes follows the [National Incident-Based Reporting System (NIBRS)](http://gis.chicagopolice.org/clearmap_crime_sums/crime_types.html){:target="_blank"} of the Federal Bureau of Investigation (FBI).*</small>

In the upper heatmap we can again clearly see the decline in violent crime until 2014. Furthermore, a seasonal pattern shows where crime rates are relatively higher in the summer compared to the winter months. The lower visualization depicts the intra-day variation by month. There is a strong increase in crimes starting in the late afternoon, when children are starting to leave their schools. A similar pattern exists for property crimes.

## Chicago's Safe Passage program
Due to Chicago's high crime rate and as incidents regularly include students, the City of Chicago launched the Safe Passage program in 2009 for initially 35 schools. The program has the goal of keeping the students safe on their way to school and thereby enabling them to focus more on their studies.[^10] This should eventually result in reduced crime counts as well as an increase in school attendance in the affected neighborhoods.

To ensure the safety of the children, guards, which are mostly residents from the respective neighborhoods, are posted along various routes to the participating schools, right before and after schooling hours[^3]. They are hired by local community organizations and trained in de-escalation strategies and safety protocols. However, they do not carry any weapons or have special authority.[^8]

Since 2009, the Safe Passage program was heavily expanded. The biggest extensions happened in the school years of 2013-2014 and 2014-2015, where more than 90 schools were added to the program. This happened in response to a large school closure of around 50 schools, which let to many students having to travel farther and some of them where required to cross gang boundaries on their way to school.

In the school year 2016-2017, more than 1,300 Safe Passage workers guarded around 75,000 students.[^4] The costs associated with the program for that school year amounted to $17.8 million.[^9] New Safe Passage routes are added almost every year and focus primarily on areas with especially high crime counts.

## Motivation and research question
Because of the graveness of Chicago's crime problem as well as the fact that a considerable amount of tax payer money is spent on the program, information about the effectiveness of the program arguably is of great importance. This analysis tries to answer the following question: Does Chicago's Safe Passage program reduce crime along the guarded routes during operational hours?

## Contribution
Officials from the City of Chicago have mentioned declines in crime from 20% up to 32% due to the program, they did however not publish any details on such an analysis.[^5]<sup>,</sup>[^6]<sup>,</sup>[^7] In the school year 2015-2016, 30% less school students were shot compared to the school year of 2011-2012.[^9] The question remains in how far this decline in crime, which we already saw in the figures above (at least up to 2014), can be attributed to the Safe Passage program or if it is due to other factors.

The working paper "Do More Eyes on the Street Reduce Crime? Evidence from Chicago’s Safe Passage Program" by Daniel McMillen, Ignacio Sarmiento-Barbieri, and Ruchi Singh from June 22, 2017[^8] tries to address this issue by providing a thorough analysis of the Safe Passage program. They find a reduction in violent crime counts along Safe Passage routes of around 14%, however no significant effect could be detected for property crimes. As the authors did so far neither make their code nor all of the data public, I took the opportunity to try to replicate one of their main specifications, where they aggregate crime counts on the level of census blocks. A direct comparison of descriptive figures, tables, and the main results can be obtained by clicking on the "launch binder" badge at the beginning of the page. The results and the estimation themselves will also be further described on the following page. For a more detailed overview of the literature I refer to the Appendix.{% comment %}
TODO: Add link? Should this remark be in here?
{% endcomment %}

Next to trying to replicate the findings of McMillen et al. (2017)[^8], this project aims at providing a publicly available analysis of the Safe Passage program, which others can easily build upon and scrutinize. Furthermore it serves as an example for the second part of my master thesis, which is [A Basic Guide to Reproducible Research](https://binste.github.io/basic_reproducibility_guide/).

[Continue to the section on "Estimation strategy and results"](./estimation_and_results.md)

# References

[^1]: [Chicago’s Murder Problem - New York Times; May 27, 2016](https://www.nytimes.com/interactive/2016/05/18/us/chicago-murder-problem.html){:target="_blank"}
[^2]: [2017 Chicago Shot Clock - HeyJackass.com](https://heyjackass.com/2017-chicago-shot-clock/){:target="_blank"}
[^3]: [Is Safe Passage Safe from Budget Cuts? - southsideweekly.com; April 19, 2017 ](https://southsideweekly.com/is-safe-passage-safe-from-budget-cuts/){:target="_blank"}
[^4]: [CPS Expands Safe Passage to Serve 142 Schools this Year - CPS Press Release; September 4, 2016](http://cps.edu/News/Press_releases/Pages/PR1_09_04_2016.aspx){:target="_blank"}
[^5]: [Nineteen Community-Based Safe Passage Vendors Chosen To Lead Work At Welcoming Schools this Fall - CPS Press Release; June 24, 2013](https://cps.edu/News/Press_releases/Pages/PR1_06_24_2013.aspx){:target="_blank"}
[^6]: [CPS Expands Safe Passage to Serve 142 Schools this Year - CPS Press Release; September 4, 2016](https://cps.edu/News/Press_releases/Pages/PR1_09_04_2016.aspx){:target="_blank"}
[^7]: [CPS Says Crime Down by One-Third Along Safe Passage Routes - ChicagoTonight.wttw.com; May 26, 2017](https://chicagotonight.wttw.com/2017/05/26/cps-says-crime-down-one-third-along-safe-passage-routes){:target="_blank"}
[^8]: [Do More Eyes on the Street Reduce Crime? Evidence from Chicago’s Safe Passage Program; June 22, 2017](https://ignaciomsarmiento.github.io/assets/Safe_Passage_WP.pdf){:target="_blank"}
[^9]: [CPS says students safer now than five years ago - Chicago Sun-Times; September 22, 2016](https://www.pressreader.com/usa/chicago-sun-times/20160922/281582355105718){:target="_blank"}
[^10]: [In Chicago, Campaign to Provide Safe Passage on Way to School - The New York Times; August 26, 2013](https://www.nytimes.com/2013/08/27/education/in-chicago-campaign-to-provide-safe-passage-on-way-to-school.html){:target="_blank"}
