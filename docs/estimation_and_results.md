---
title: Estimation strategy and results
---
## Strategy
In the movie "Sliding Doors" (1998)[^2], we see the life of Helen in two versions. In one she catches the subway train, in another, she misses it by a split second. What unfolds are two completely different stories of her future, and you as a viewer can see both. The movie director therefore allows us to compare the two futures and derive the exact causal effect for Helen of catching that very train.

Unfortunately, when analyzing a policy such as the Safe Passage program, observing an alternate universe where the program would not have been implemented, is of course impossible. Else we could stop right here. We therefore have to resort to approximate it as good as possible. Although we will never know how good our approximation really is, we can avoid some pitfalls.

In this analysis, instead of observing the life of Helen, we will follow the evolution of violent-crime counts, summarized for each census block in Chicago and for each month per school year between January 2006 and June 2016 (click on the "launch binder" badge in the beginning of the [Introduction](./index.md) to see how this looks). This time frame allows for observing the evolution of crime in Chicago even before the start of the Safe Passage program in 2009.

Let us know continue with a fictional census block, which contains a street which is frequently used by kids to get to and from school. Due to various crime incidents, at the start of the school year 2012-2013, the City of Chicago implements the Safe Passage program for this very street and from now on, guards will protect the children on their way to school. In our analysis, we would then mark this block as "treated" for all subsequent months.

If we would want to know the effect of the guards, one approach would be to compare average crime counts per month before and after the program was implemented. Let's say we observe a reduction of 2 violent crimes per month. Such a reduction is shown with the blue line in the figure below (ignore the red lines for now).

<small>*Figure 4 - Illustration of DiD example*</small>
![did_illustration](figures/didfigure.png)
<small>*"Before" and "After Implementation" refer to the months prior and after the implementation of the Safe Passage program in the "treated" block.*</small>

However, as mentioned before, we do not know what would have happened, if the program was never implemented. Maybe there would have been a reduction of 2 crimes anyway,and the program would have had no effect whatsoever. Or there might even have been an increase by 3 violent crimes per month and the program effectively prevented an average of 5 violent crimes per month.

This is where the before mentioned approximation comes into play. Behind the approach used in this analysis stands the idea, that other census blocks, which are not crossed by a Safe Passage route in a given month, can be seen as such an approximation. Let's continue with the example from above and imagine a second census block ("control block") which did never receive a Safe Passage route. This control block might have experienced a decrease in crime counts of 1 crime per month, when comparing the same before and after months as for the treated block (i.e. before and after the beginning of the school year 2012-2013). In the above figure this would be the solid red line.

If we are confident, that the "control" block is a good approximation for the change in crime (the dashed red line in the figure above) for the treated block, should the program never have been implemented, the implication then is, that 1 of the on average 2 prevented crimes in the treated block is due to the program and the other one is due to other factors which affected both control and treated block (such as a city-wide program to prevent crime).

This approach is generally referred to as difference in differences (DiD). The first difference is the two trends over time, one of the treated blocks and one of the control. The second difference is then the difference between these two trends (as calculated above in our toy example).

How close the estimated effect is to the unobservable truth, depends on if the control block really represents the same crime trend that the treated block would have experienced in absence of the Safe Passage program. As mentioned in the Introduction, Safe Passage routes are predominantly implemented in high-crime and segregated neighborhoods where students are "mostly minorities and low income".[^1]  If you would therefore just pick control blocks at random from all blocks in Chicago, you might end up comparing fundamentally different areas. You'll have a hard time convincing people that the poorer neighborhoods of Chicago should be compared to the richer ones when assessing the impact of such a program.
{% comment %}
Further explain, why this is the case.
{% endcomment %}

To be more confident in the comparability of treated and control blocks, McMillen et al. (2017)[^1] choose census blocks as controls, which are right next to the treated ones. This leads to the control blocks having similar demographic characteristics as their treated counterparts (such as racial heterogeneity, income distribution, etc.). It might therefore be more reasonable to assume, that the trends of treated and control blocks would have been approximately the same in the absence of the implementation of the crime prevention program, compared to the more naive approach of picking control blocks at random from all available ones.

McMillen et al. (2017)[^1] further subdivide the control blocks into three groups. A block which itself is not treated but is adjacent to a treated block, is called a "One over" block. A block which has a "One over" block between itself and a "treated" block will be called "Two over". The same logic applies for "Three over" blocks.

<small>*Figure 5 - Illustration of block categorization*</small>
![block_groups](figures/blockgroups.png)
<small>*Example using the Safe Passage route of Bogan High School in the school year 2013-2014 as well as the surrounding blocks.*<br />
*Data sources: XXX*</small>
{% comment %}
Include illustration map?
{% endcomment %}


This categorization of control blocks allows to not only more accurately access the effect of the program on the treated blocks, but also to analyze possible displacement effects. If such effects would be present, crimes might not be prevented, but simply happen in areas close by, where the guards can't see them.

{% comment %}
Include binder badge to map of blocks?
{% endcomment %}

The following figure shows the number of blocks over the school years, which are labelled as belonging to one of the four categories.

<small>*Figure 6 - Number of treated and control blocks per school year*</small>
![block_trend](figures/blocktrend.png)
<small>*Data sources: XXX*</small>
{% comment %}
Is this figure really needed?
{% endcomment %}

You can see the big expansion of the program in the school year 2013-2014, which was mentioned in the introduction.

To get a feeling for how good the comparability of treatment and control units is, we can look at the evolution of crime counts before the implementation. As the approach relies on control and treated blocks being similar, it is reassuring if the pre-treatment trends are similar, as no factor should then affect the two groups differently.

The following figure visualizes average violent-crime counts per block per weekday. The school years on the horizontal axis are relative to the implementation of the Safe Passage program of the corresponding "Treated" block (each control block has the closest treated block assigned to it).

<small>*Figure 7 - Difference in differences plot for violent crimes*</small>
![did_violent](figures/didfigureviolent.png)
<small>*To create this figure, each block needs to be assigned to exactly one group. The data used here is therefore not exactly representative of the one used in the final estimation of the effect, as there, blocks are allowed to change their status. They can for example first be a "Two over" block and then become a "One over" block, if a Safe Passage route gets implemented in an adjacent block. However, this can be seen as a close approximation.*<br />
*This figure is an approximate replication of Figure 3a in McMillen et al. (2017)[^1]*<br />
*Data sources: XXX*</small>

When looking at the overall level of the crime counts, treated blocks do suffer from more incidents then the control blocks. Therefore, even though the control blocks are right next to the treated blocks, they are not comparable in terms of the number of incidents. This again shows, that the Safe Passage program was implemented primarily in high-crime areas. However, as mentioned before, what we need for the difference-in-difference approach to work, is that the changes in crime over time would be similar in absence of treatment.

We see that the trends in crimes are rather similar before the implementation of the program, with slightly stronger differences between the 4th and 5th school year prior to the implementation. In the first school year after the implementation of the program, we see a drop in crime counts for the treated blocks. No such jump however is visible for the three control block categories.

<small>*Figure 8 - Difference in differences plot for property crimes*</small>
![did_property](figures/didfigureproperty.png)
<small>*To create this figure, each block needs to be assigned to exactly one group. The data used here is therefore not exactly representative of the one used in the final estimation of the effect, as there, blocks are allowed to change their status. They can for example first be a "Two over" block and then become a "One over" block, if a Safe Passage route gets implemented in an adjacent block. However, this can be seen as a close approximation.*<br />
*This figure is an approximate replication of Figure 3b in McMillen et al. (2017)[^1]*<br />
*Data sources: XXX*</small>

When we look at property crimes in Figure 7, we again see, apart from the 5th and 4th school year prior to the implementation, rather similar pre-treatment trends. However, visually there is no clue that the implementation led to an effect on property crime, as all groups experienced a similar downwards trend.

## Results
To quantify the effect of the Safe Passage program, which we already visually saw in the two figures above, McMillen et al. (2017) use a Poisson regression. Details on the specification can be found in the Appendix XXX. Following the same estimation strategy, I found that the Safe Passage program reduces violent crime by 12.5% on average between 6.30 am and 5.30 pm for week days of a school year. The result is therefore very similar to their findings of a 13.4% reduction. Furthermore, no displacement effects to the adjacent areas was found. For property crime, the estimation shows no statistically significant reduction in crime, neither by the authors of the original paper, nor by myself.

I was therefore able to successfully replicate their findings concerning the effect of the Safe Passage program on crime on the level of census blocks. A more detailed comparison of the main results and the figures presented here can be found by clicking on the first "launch binder" badge on the previous page or in the Appendix XXX.

Note, that the paper by McMillen, Sarmiento-Berbieri, and Singh contains much more than this one specification, including various robustness checks assessing the reliability of the results, an analysis of the effect of the program on attendance rates, as well as a cost-benefit analysis of the whole Safe Passage program.

{% comment %}
Set the percentages into context. How much reduction from baseline crime is it?

However, the reduction in violent crimes is only half the number claimed by city officials. It remains interesting to see an evaluation from the official side to back up these numbers.
{% endcomment %}

Again I would like to reference to the Appendix XXX for more details on the analysis, the data used, the empirical strategy, as well as its limitations. The code and data, as well as instructions on how to reproduce the analysis, are available in the corresponding [GitHub repository](https://github.com/binste/chicago_safepassage_evaluation).

If you are interested in reproducible research, head over to my [Basic Guide on Reproducible Research](https://binste.github.io/basic_reproducibility_guide/).

[Back to the introduction](./index.md)

# References
[^1]: [Do More Eyes on the Street Reduce Crime? Evidence from Chicago’s Safe Passage Program; June 22, 2017](https://ignaciomsarmiento.github.io/assets/Safe_Passage_WP.pdf){:target="_blank"}
[^2]: [Sliding Doors (1998) - imdb.com](https://www.imdb.com/title/tt0120148/){:target="_blank"}