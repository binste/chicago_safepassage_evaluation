---
title: Estimation and results
---

## Strategy
The challenge one has to solve when trying to find a causal effect of a policy such as the Safe Passage program, is that we do not know what would have happened, should the program never have been implemented. A commonly used approach in econometrics to tackle this issue, is a technique called difference in differences (DiD). Using a DiD, we can find the causal effect by comparing the evolution of crime counts in areas (here census blocks), which have a Safe Passage route with the evolution of crime counts in comparable areas without a Safe Passage route (the counterfactual).

The caveat lies in the word "comparable". These areas would need to have the exact same changes in crime over time as the affected areas would have had, if the program would not have been implemented. For a great visualization of the difference in differences approach see [this figure](http://nepaldevelopment.pbworks.com/f/1353649147/A2A%20DIDgraph.png).

A naive approach might be to use the parts of Chicago, which do not have a Safe Passage route, as the comparison group. However, the Safe Passage program was implemented primarily in areas with especially high crime counts. These are also the areas where students are "mostly minorities and low income"[^1]. It will be hard to argue, that these areas are comparable to let's say richer neighborhoods.
{% comment %}
Better explain problem and characteristics which might differ and lead to a problem.
{% endcomment %}

McMillen et al. (2017) chose to use the census blocks around the ones, which contain an actively guarded Safe Passage route, as their control group. The directly adjacent blocks are called "One over" blocks, where as blocks which have a "One over" block between themselves and a "Treated" block, are called "Two over" blocks. The same logic is applied for "Three over" blocks.
{% comment %}
Include a figure which shows this? Also could include link to notebook which shows evolution over time on a map.
{% endcomment %}

The following figure shows the number of blocks over the school years, which are labelled as belonging to one of the four categories.

{% include block_trend.html %}

You can see the big expansion of the program in the school year 2013-2014, which was mentioned in the introduction.

As the comparison blocks ("One over", "Two over", "Three over") are close to the "Treated" blocks, they share similar demographic and other crime-related characteristics. {% comment %}
link to McMillen et al. (2017) paper?
{% endcomment %} It might be therefore more reasonable to assume, that the trends of the four categories, would have been approximately the same in the absence of the implementation of the crime prevention program, compared to the naive approach.

The reason, why the comparison blocks are split up into three groups, depending on their proximity to a "Treated" block, which contains a Safe Passage route", is that it gives us the possibility to check, if the crimes simply happened in the neighboring blocks, instead of on a Safe Passage route. These so called "displacement effects" can pose serious problems for your evaluation strategy, should you not control for them. For more detailed description of the data, the empirical strategy, its limitations, and how "displacement effects" are measured see the Appendix (XXX link).

To compare treated and control blocks, we can plot the evolution of their violent crime counts over time. I do this in the following figure, with the years being relative to the implementation of the Safe Passage program of the corresponding "Treated" block.

{% include did_figure_violent.html %}
<small>*Due to the need for this figure to assign each block exactly one group, the data used here is not exactly representative of the one used in the final estimation of the effect. However, it can serve as a close approximation.</small>

First, we see that the trends in crimes are similar before the implementation of the program, although the changes are slightly stronger in magnitude for the "Treated" blocks. This can serve as a reassurance, that you have chosen a reasonable comparison group. However, we also see that the "Treated" blocks in general have a higher crime-count, which might pose a danger to our strategy. Again I refer to the Appendix XXX for additional information.

At the time of the implementation we see a clear jump downwards for the "Treated" blocks, which is not present for the others. If our comparison blocks serve as good counterfactuals, this jump represents the effect of the program on the count of violent crimes.

As sort of a falsification check, we can do the same but looking at property crime counts. For these crimes, intuitively the program should not really have an effect.

{% include did_figure_property.html %}

It is reassuring, that indeed, the same jump is not present for property crimes.

## Main findings
To quantify the jump, McMillen et al. (2017) used a Poisson regression. Details again can be found in the Appendix XXX. Following their estimation strategy, I found that the Safe Passage program reduces violent crime by 12.5% on average. The result is therefore very similar to the findings of McMillen et al. (2017), which found 13.4% reduction in violent crime. For property crime no significant reduction in crime could be found, neither by the authors of the original paper, nor by myself. I was therefore able to successfully replicate their findings concerning crime prevention, and a detailed comparison of the main results on a census block level can be found by clicking on the first "launch binder" badge on the previous page.

However, the reduction in violent crimes is only half the number claimed by city officials. It remains interesting to see an evaluation from the official side to back up these numbers.

{% comment %}
Set the percentages into context. How much reduction from baseline crime is it?
{% endcomment %}

Again I would like to point the interested reader in the direction of [the Appendix](XXX), which contains more detailed information on this analysis.

# References
[^1]: [Do More Eyes on the Street Reduce Crime? Evidence from Chicago’s Safe Passage Program; June 22, 2017](https://ignaciomsarmiento.github.io/assets/Safe_Passage_WP.pdf){:target="_blank"}

[Back to the introduction](./1_Introduction.md)