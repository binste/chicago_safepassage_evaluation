---
title: Introduction
---
**ATTENTION**: This is a work in progress and subject to major changes.


The final steps to obtain the figures used on this website can be reproduced directly in your browser without any setup needed by clicking on [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/binste/chicago_safepassage_evaluation/master?filepath=notebooks%2F5_analysis%2F1.0-binste-analyze-crime-results-census-block-level.ipynb){:target="_blank"}. If you want to rerun the estimation or even start out from the raw data files, visit the [GitHub repository](https://github.com/binste/chicago_safepassage_evaluation){:target="_blank"} for instructions.

## Crime in Chicago
Chicago notoriously suffers from a very high number of violent crimes, where a vast part of the incidents happen in poor neighborhoods on the South and West Sides.[^1] In 2017, on average every 13 hours a person was murdered in Chicago and every 2 hours and 30 minutes someone was shot[^2]. The figure below shows the evolution of violent crime over time. Although there was a decline up until 2014, since then the crime count has started to increase again.

{% include violent_FBI.html %}
<small>*Data source: [Crimes - 2001 to present, Chicago Data Portal; accessed January 25, 2018](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2){:target="_blank"}*<br />
*The the categorization of violent crimes follows the [National Incident-Based Reporting System (NIBRS)](http://gis.chicagopolice.org/clearmap_crime_sums/crime_types.html){:target="_blank"} of the Federal Bureau of Investigation (FBI).*</small>

Violent crimes are of special interest for this analysis, as they represent the crimes which should be prevented by the analyzed crime prevention program. Let us therefore zoom a bit more into the intra-year and intra-day variation of violent crimes with the figure below.

Note that, if you want to see the intra-day variation in the lower part of the figure with data only for one year, you can select a single year by clicking on a square corresponding to that year in the upper figure. The lower heatmap will adapt accordingly.

{% include violent_trend.html %}
<small>*Data source: [Crimes - 2001 to present, Chicago Data Portal; accessed January 25, 2018](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2){:target="_blank"}*<br />
*The the categorization of violent crimes follows the [National Incident-Based Reporting System (NIBRS)](http://gis.chicagopolice.org/clearmap_crime_sums/crime_types.html){:target="_blank"} of the Federal Bureau of Investigation (FBI).*</small>

In the upper heatmap we can again clearly see the decline in violent crime until 2014. Furthermore, a seasonal pattern shows where crime rates are relatively higher in the summer compared to the winter months. The lower visualization depicts the intra-day variation depending on the month. We see a strong increase in crime during the late evening hours.

## Chicago's Safe Passage program
Due to Chicago's notorious problem with crime and various incidents including students, the City of Chicago launched the Safe Passage program in 2009 for 35 schools. The goal of the program is to keep the students safe on their way to school, thereby giving them the chance to focus more on their studies.[^10] This should eventually show in reduced violent crime rates as well as an increase in school attendance.

To ensure the safety of the children, guards, which are mostly residents from the respective neighborhoods, are posted along various routes to the participating schools, right before and after schooling hours[^3]. They are hired by local community organizations and trained in de-escalation strategies and safety protocols. However, they do not carry any weapons or have special authority.[^8]

Since 2009, the Safe Passage program was heavily expanded, especially in the school years of 2013-2014 and 2014-2015 where more than 90 schools were being added to the program. This was the result of a large school closure of around 50 schools, which let to many students having to travel farther to neighboring areas which required some of them to cross gang boundaries on their way to school.

In the school year 2016-2017, more than 1,300 Safe Passage workers guarded around 75,000 students.[^4] The programs cost for that school year amounted to $17.8 million.[^9] New Safe Passage routes are added almost every year and focus on areas with high violent-crime counts.

## Motivation and research question
Because of the high crime counts together with a considerable share of tax payer money going in the direction of the program, I believe that to gain more information on the effectiveness of the program is of great importance. Officials from the City of Chicago have mentioned declines in crime from 20% up to 32% due to the program.[^5]<sup>,</sup>[^6]<sup>,</sup>[^7] In the school year 2015-2016, 30% less school students were shot compared to the school year of 2011-2012.[^9] However, in absence of a publicly available evaluation, the question remains in how far this decline in crime, which we already saw in the figures above, can be attributed to the Safe Passage program or if it is more of an independent city-wide phenomenon.

This analysis therefore aims to answer the following question: Does Chicago's Safe Passage program reduce violent crime along the guarded routes during operational hours?

Note that, to make a full evaluation of the program, one would also need to look into the claims of increased attendance rates.

## Contribution
In the spring of 2017 I started a preliminary analysis on this topic as a project for a university course. When I decided to pick it up again for my master thesis, I found the working paper "Do More Eyes on the Street Reduce Crime? Evidence from Chicago’s Safe Passage Program" by Daniel McMillen, Ignacio Sarmiento-Barbieri, and Ruchi Singh from June 22, 2017.[^8] Their analysis finds a reduction in violent crime counts along Safe Passage routes of around 14%.

My chosen analytical approach in the following closely follows their specification with census blocks as the observational unit and can be seen as an attempt to replicate some of the findings concerning the reduction in crime. A direct comparison of a few descriptive figures, tables, and the main results can be obtained by clicking on the "launch binder" badge at the beginning of the page.

[Continue to "Estimation and results"](./estimation_and_results.md)

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
