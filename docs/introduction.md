---
title: Introduction
---
## Crime in Chicago
Chicago notoriously suffers from a very high number of crimes, where many incidents happen in poor neighborhoods on the South and West Sides.[^1] Figure 1 shows, that even though there was a welcome downwards trend for a few years, for both property and violent crimes, this started to inverse around 2014/2015.
{% comment %}
Do the crimes need further definition?
{% endcomment %}

*<font size="-1">Figure 1 - Evolution of violent- and property-crime counts over time</font>*
{% include yearly_violent_trend.html %}
*<font size="-1">The definition of violent and property crimes follows the <a href="http://gis.chicagopolice.org/clearmap_crime_sums/crime_types.html" target="_blank">National Incident-Based Reporting System (NIBRS)</a> of the Federal Bureau of Investigation (FBI).<br />
This figure is an approximate replication of Figure A.2 in McMillen et al. (2017)<br />
Data source: <a href="https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2" target="_blank">Crimes - 2001 to present, Chicago Data Portal; accessed January 25, 2018</a></font>*


If we look at a more granular view of violent crimes, we see that the number of homicides in 2017 is even on a higher level than it was in 2006.

*<font size="-1">Figure 2 - Evolution of violent-crime counts over time by subcategories</font>*
{% include violent_FBI.html %}
*<font size="-1">The definition of violent crimes as well as the sub categories follows the <a href="http://gis.chicagopolice.org/clearmap_crime_sums/crime_types.html" target="_blank">National Incident-Based Reporting System (NIBRS)</a> of the Federal Bureau of Investigation (FBI).<br />
Data source: <a href="https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2" target="_blank">Crimes - 2001 to present, Chicago Data Portal; accessed January 25, 2018</a>
</font>*

To put the graveness of the situation into more graspable numbers: In 2017, on average, every 13 hours a person was murdered and every 2 hours and 30 minutes someone was shot.[^2]

Let us change the perspective and look at the intra-year and intra-day variation of violent crimes. In the upper visualization of Figure 3, we again see the decline in crime counts until 2014. Furthermore, there is a clear seasonal pattern, where crime counts are relatively higher in the summer compared to the winter months. The lower visualization depicts the intra-day variation by month. There is a strong increase in crimes starting in the late afternoon, when children are starting to leave their schools. This is also when property crime counts are notoriously high.

Note that, if you want to see the intra-day variation in the lower part of the figure calculated with data only for one year, you can select a single year by clicking on a square corresponding to that year in the upper figure. The lower heatmap will adapt accordingly.

*<font size="-1">Figure 3 - Intra-year and intra-day variation in violent crimes</font>*
{% include violent_trend.html %}
*<font size="-1">The definition of violent crimes follows the <a href="http://gis.chicagopolice.org/clearmap_crime_sums/crime_types.html" target="_blank">National Incident-Based Reporting System (NIBRS)</a> of the Federal Bureau of Investigation (FBI).<br />
Data source: <a href="https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2" target="_blank">Crimes - 2001 to present, Chicago Data Portal; accessed January 25, 2018</a></font>*

## Chicago's Safe Passage program
Chicago's crime incidents regularly involve students. As an example, in 2012, 29 current or former students of Harper High School were shot, eight of them did not survive.[^11][^12]

>*"[I] encountered kids at Harper [High School] who wake up and they wonder whether they're going to make it out of school alive."* - Michelle Obama, 2013[^12]

Due to Chicago's crime problem and the threats many students face daily when going to and coming from school, the City of Chicago launched the Safe Passage program in 2009 for initially 35 schools. The program has the goal of keeping the students safe on their way to school and thereby enabling them to focus more on their studies.[^10]

To ensure the safety of the children, guards, which are mostly residents from the respective neighborhoods, are posted along various routes to the participating schools, right before and after schooling hours.[^3] They are hired by local community organizations and trained in de-escalation strategies and safety protocols. However, they do not carry any weapons or have special authority.[^8]

Since 2009, the Safe Passage program was heavily expanded. The biggest extensions happened in the school years of 2013-2014 and 2014-2015, where in total more than 90 schools were added to the program. This happened in response to a large school closure of around 50 schools, which let to many students having to travel farther to school and some of them where required to cross gang boundaries.

In the school year 2016-2017, more than 1,300 Safe Passage workers guarded around 75,000 students.[^4] The costs associated with the program for that school year amounted to $17.8 million.[^9] New Safe Passage routes are added almost every year and focus primarily on areas with especially high crime counts.

## Motivation and research question
Because of the graveness of Chicago's crime problem as well as the fact that a considerable amount of tax payer money is spent on the program, gaining more information on the effectiveness of the program arguably is of great importance. This analysis tries to answer the following question: Does Chicago's Safe Passage program reduce crime along the guarded routes during operational hours?

## What has been done before?
Officials from the City of Chicago have mentioned declines in crime from 20% up to 32% due to the program, they did however not publish any details on such an analysis.[^5]<sup>,</sup>[^6]<sup>,</sup>[^7] In the school year 2015-2016, 30% less school students were shot compared to the school year of 2011-2012.[^9] The question remains in how far this decline in crime, which we already partly saw in the figures above (at least up to 2014), can be attributed to the Safe Passage program or if it is due to other factors.

A more sophisticated approach was taken by Daniel McMillen, Ignacio Sarmiento-Barbieri, and Ruchi Singh in their working paper "Do More Eyes on the Street Reduce Crime? Evidence from Chicago’s Safe Passage Program" from June 22, 2017[^8]. They find a reduction in violent crime counts along Safe Passage routes of around 14%, however no significant effect could be detected for property crimes. As the authors did so far neither make their code nor all of the data public, I took the opportunity to try to replicate one of the specifications done in the paper. The results thereof as well as the estimation will be presented on the following page. A direct comparison of descriptive figures, tables, and the main results can be obtained by clicking on the "launch binder" badge at the beginning of the page.

Note, that the paper by McMillen et al.[^8] contains much more then what I replicated. For a more detailed overview of the paper as well as other existing literature on the Safe Passage program see the section "Literature" in the [Appendix](https://github.com/binste/chicago_safepassage_evaluation/tree/master/reports/appendix/Appendix.pdf){:target="_blank"}.

Next to attempting to replicate the findings of McMillen et al. (2017)[^8], this project aims at providing a publicly available analysis of the Safe Passage program, which others can easily build upon and extend. This hopefully will eventually lead to a better understanding of how we can effectively fight crime and prevent as much suffer as possible.

Continue to the section on [Estimation strategy and results](./estimation_and_results.md)

## References

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
[^11]: [Harper High School - This American Life; February 15, 2013](https://www.thisamericanlife.org/487/harper-high-school-part-one)
[^12]: [Michelle Obama: Chicago Students Worried 'About Their Own Death' - dnainfo; May 5, 2013](https://www.dnainfo.com/chicago/20130505/chicago/michelle-obama-chicago-students-worried-about-their-own-death/)