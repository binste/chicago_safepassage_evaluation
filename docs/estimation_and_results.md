---
title: Estimation strategy and results
permalink: /estimation_and_results
---
## Strategy
In the movie "Sliding Doors" (1998)[^2], we see the life of Helen in two versions. In one she catches the subway train, in another, she misses it by a split second. What unfolds are two completely different stories of her future, and you as a viewer can see both. The movie director therefore allows us to compare the two futures and derive the exact causal effect for Helen of catching that very train.

Unfortunately, when analyzing a policy such as the Safe Passage program, observing an alternate universe, where the program was never implemented, is of course impossible. Else, we could stop right here. We have to resort to approximate the unobservable as good as possible. Consequently, we will never know how good our approximation really is, but we can avoid some pitfalls.

In this analysis, instead of observing the life of Helen, we will follow the evolution of violent-crime counts, summarized for each census block in Chicago and for each month per school year between January 2006 and June 2016 (click on the "launch binder" badge in the [Overview](./index.md) to analyze the data yourself). This time frame allows for observing the evolution of crime in Chicago even before the start of the Safe Passage program in 2009.

### DiD illustration
Let us now imagine a fictional census block, which is crossed by a street frequently used by kids to get to and from school. Due to various crime incidents, at the start of the school year 2012-2013, the City of Chicago implements the Safe Passage program for this very street and from now on, civilian guards will protect the children on their way to school. In our analysis, we would then mark this census block as "treated" for all subsequent months.

If we want to know the effect of the guards, one could compare average crime counts per month before and after the program was implemented. Let's say we observe a reduction of 2 violent crimes per month. This scenario is shown with the blue line in the figure below (ignore the red lines for now).

*<font size="-1">Figure 4 - Illustration of DiD example</font>*
![did_illustration](figures/didfigure.png)
{: .full}
*<font size="-1">"Before" and "After Implementation" refer to the months prior and after the implementation of the Safe Passage program in the "treated" block.<br />
Data source: Example from text</font>*

However, as mentioned before, we do not know what would have happened, if the program was never implemented. Maybe there would have been a reduction of 2 crimes anyway,and the program would have had no effect whatsoever. Or there might have been an increase by 3 violent crimes per month and the program actually prevented an average of 5 violent crimes per month.

This is, where the before mentioned approximation comes into play. Behind the approach used in this analysis stands the idea, that other census blocks, which are not crossed by a Safe Passage route in a given month, can be used to approximate the change in crime, should the program not have been implemented. Let's continue with the example from above and imagine a second census block ("control block") which did never receive a Safe Passage route. This control block might have experienced a decrease in crime counts of 1 crime per month, when comparing the same before and after months as for the treated block (i.e. before and after the beginning of the school year 2012-2013). In the above figure this is the solid red line.

If we are confident, that the "control" block is a good approximation for the change in crime, we can now think of the treated block having experienced the same change in crime in absence of the program (the dashed red line in the figure above). The implication then is, that 1 of the on average 2 prevented crimes in the treated block is due to the program and the other one is due to other factors which affected both control and treated block (such as a city-wide program to prevent crime). We now do not simply compare before and after of the treated block (blue line), but we take the difference in the trends of the blue line and the dashed red line.

This approach is generally referred to as difference in differences (DiD). The first difference is the two trends over time, one of the treated blocks and one of the control. The second difference refers to the difference between these two trends. How close the estimated effect of the DiD approach is to the unobservable truth, depends on how close the control block represents the unobservable crime trend that the treated block would have experienced in absence of the Safe Passage program.

### Finding good control blocks
As mentioned in the Introduction, Safe Passage routes are predominantly implemented in high-crime, low income, and segregated neighborhoods.[^1] Therefore, by picking control blocks at random from all blocks in Chicago, you might end up comparing fundamentally different areas. You'll have a hard time convincing people that the poorer neighborhoods of Chicago should be compared to some of the richer ones when assessing the impact of the program, as they are fundamentally different in many factors, which can influence crime.

To be more confident in the comparability of treated and control blocks, McMillen et al. (2017)[^1] choose census blocks as controls, which are right next to the treated ones. This leads to the control blocks having similar demographic characteristics as their treated counterparts (such as racial heterogeneity, income distribution, etc.). It might therefore be more reasonable to assume, that the trends of treated and control blocks would have been approximately the same in the absence of the implementation of the crime prevention program, compared to the more naive approach of picking control blocks at random from all available ones.

McMillen et al. (2017)[^1] further subdivide the control blocks into three groups. A block which itself is not treated but is adjacent to a treated block, is called a "One over" block. A block which has a "One over" block between itself and a "treated" block will be called "Two over". The same logic applies for "Three over" blocks.

*<font size="-1">Figure 5 - Illustration of block categorization</font>*
![block_groups](figures/blockgroups.png)
{: .full}
*<font size="-1">Example using the Safe Passage route of Bogan High School in the school year 2013-2014 as well as the surrounding blocks.<br />
Data sources: See the section "Data" in the <a href="https://github.com/binste/chicago_safepassage_evaluation/tree/master/reports/appendix/Appendix.pdf" target="_blank">Appendix</a></font>*

This categorization of control blocks allows to not only more accurately access the effect of the program on the treated blocks, but also to analyze possible displacement effects. If such effects would be present, crimes might not be prevented, but simply happen in areas close by, where the guards can't see them.

{% comment %}
Include binder badge to map of blocks?
{% endcomment %}

The following figure shows the number of blocks over the school years, which are labelled as belonging to one of the four categories.

*<font size="-1">Figure 6 - Number of treated and control blocks per school year</font>*
![block_trend](figures/blocktrend.png)
{: .full}
*<font size="-1">Data sources: See the section "Data" in the <a href="https://github.com/binste/chicago_safepassage_evaluation/tree/master/reports/appendix/Appendix.pdf" target="_blank">Appendix</a></font>*

You can see the big expansion of the program in the school year 2013-2014, which was mentioned in the introduction.

To get a feeling for how good the comparability of treatment and control units is, we can look at the evolution of crime counts before the implementation. As the approach relies on control and treated blocks being similar, it is reassuring if the pre-treatment trends are similar, as no factor should then affect the two groups differently.

The following figure visualizes average violent-crime counts per block per weekday. The school years on the horizontal axis are relative to the implementation of the Safe Passage program of the corresponding "Treated" block (each control block has the closest treated block assigned to it).

*<font size="-1">Figure 7 - Difference in differences plot for violent crimes</font>*
![did_violent](figures/didfigureviolent.png)
{: .full}
*<font size="-1">To create this figure, each block needs to be assigned to exactly one group. The data used here is therefore not exactly representative of the one used in the final estimation of the effect, as there, blocks are allowed to change their status. They can for example first be a "Two over" block and then become a "One over" block, if a Safe Passage route gets implemented in an adjacent block. However, this can be seen as a close approximation.<br />
This figure is an approximate replication of Figure 3a in McMillen et al. (2017)<br />
Data sources: See the section "Data" in the <a href="https://github.com/binste/chicago_safepassage_evaluation/tree/master/reports/appendix/Appendix.pdf" target="_blank">Appendix</a></font>*

When looking at the overall level of the crime counts, treated blocks do suffer from more incidents then the control blocks. Therefore, even though the control blocks are right next to the treated blocks, they are not comparable in terms of the number of incidents. This again shows, that the Safe Passage program was implemented primarily in high-crime areas. However, as mentioned before, what we need for the difference-in-difference approach to work, is that the changes in crime over time would be similar in absence of treatment.

**Note**: The average areas of treatment and control blocks are very similar and can therefore not be the cause for the level difference in crime counts in Figure 7 and Figure 8.
{: .notice}

We see that the changes in crime counts are rather close before the implementation of the program, with slightly stronger differences between treatment and control blocks from the 4th to the 5th school year prior to the implementation. In the first school year after the implementation of the program, we see a drop in crime counts for the treated blocks. No such jump however is visible for the three control block categories.

*<font size="-1">Figure 8 - Difference in differences plot for property crimes</font>*
![did_property](figures/didfigureproperty.png)
{: .full}
*<font size="-1">To create this figure, each block needs to be assigned to exactly one group. The data used here is therefore not exactly representative of the one used in the final estimation of the effect, as there, blocks are allowed to change their status. They can for example first be a "Two over" block and then become a "One over" block, if a Safe Passage route gets implemented in an adjacent block. However, this can be seen as a close approximation.<br />
This figure is an approximate replication of Figure 3b in McMillen et al. (2017)<br />
Data sources: See the section "Data" in the <a href="https://github.com/binste/chicago_safepassage_evaluation/tree/master/reports/appendix/Appendix.pdf" target="_blank">Appendix</a></font>*

When we look at property crimes in Figure 8, we again see, apart from the 5th and 4th school year prior to the implementation, rather similar pre-treatment trends. However, visually there is no clue that the implementation led to an effect on property crime, as all groups experienced a similar downwards trend.

## Results
To quantify the effect of the Safe Passage program, which we already visually saw in the two figures above, McMillen et al. (2017) use a Poisson regression. Details on the specification can be found in the [Appendix](https://github.com/binste/chicago_safepassage_evaluation/tree/master/reports/appendix/Appendix.pdf){:target="_blank"}. Following the same estimation strategy, I found that the Safe Passage program reduces violent crime by 12.5% on average between 6.30 am and 5.30 pm for the week days of a school year. The result is therefore very similar to their findings of a 13.4% reduction. Furthermore, no displacement effects to the adjacent areas were found. For property crime, the estimation finds no evidence of a reduction in crime, neither in the original paper nor in my own.

I was therefore able to successfully replicate their findings regarding the effect of the Safe Passage program on crime on the level of census blocks. A more detailed comparison of the main results and the figures presented here can be found by clicking on the first "launch binder" badge in the Introduction.

Note, that the paper by McMillen, Sarmiento-Berbieri, and Singh contains much more than this one specification, including various robustness checks assessing the reliability of the results, an analysis of the effect of the program on attendance rates, as well as a cost-benefit analysis of the whole Safe Passage program.

Again, I would like to reference to the [Appendix](https://github.com/binste/chicago_safepassage_evaluation/tree/master/reports/appendix/Appendix.pdf){:target="_blank"} for more details on the analysis, the data used, the empirical strategy, as well as its limitations. The code and data, as well as instructions on how to reproduce the analysis, are available in the corresponding [GitHub repository](https://github.com/binste/chicago_safepassage_evaluation){:target="_blank"}.

If you are interested in doing your own reproducible data analysis, head over to my [Basic Guide on Reproducible Research](https://binste.github.io/basic_reproducibility_guide/){:target="_blank"}.

## References
[^1]: [Do More Eyes on the Street Reduce Crime? Evidence from Chicago’s Safe Passage Program; June 22, 2017](https://ignaciomsarmiento.github.io/assets/Safe_Passage_WP.pdf){:target="_blank"}
[^2]: [Sliding Doors (1998) - imdb.com](https://www.imdb.com/title/tt0120148/){:target="_blank"}