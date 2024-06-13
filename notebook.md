# Hypothesis Testing in Python

## Hypothesis Testing Fundamentals

### Calculating the sample mean

The `late_shipments` dataset contains supply chain data on the delivery
of medical supplies. Each row represents one delivery of a part. The
`late` columns denotes whether or not the part was delivered late. A
value of `"Yes"` means that the part was delivered late, and a value of
`"No"` means the part was delivered on time.

You'll begin your analysis by calculating a point estimate (or sample
statistic), namely the proportion of late shipments.

In `pandas`, a value's proportion in a categorical DataFrame column can
be quickly calculated using the syntax:

    prop = (df['col'] == val).mean()

`late_shipments` is available, and `pandas` is loaded as `pd`.

**Instructions**

- Print the `late_shipments` dataset.

**Answer**

```{python}

```

### Calculating a z-score

Since variables have arbitrary ranges and units, we need to standardize
them. For example, a hypothesis test that gave different answers if the
variables were in Euros instead of US dollars would be of little value.
Standardization avoids that.

One standardized value of interest in a hypothesis test is called a
z-score. To calculate it, you need three numbers: the sample statistic
(point estimate), the hypothesized statistic, and the standard error of
the statistic (estimated from the bootstrap distribution).

The sample statistic is available as `late_prop_samp`.

`late_shipments_boot_distn` is a bootstrap distribution of the
proportion of late shipments, available as a list.

`pandas` and `numpy` are loaded with their usual aliases.

**Instructions**

- Hypothesize that the proportion of late shipments is 6%.
- Calculate the standard error from the standard deviation of the
  bootstrap distribution.
- Calculate the z-score.

**Answer**

```{python}

```

### Calculating a confidence interval

If you give a single estimate of a sample statistic, you are bound to be
wrong by some amount. For example, the hypothesized proportion of late
shipments was 6%. Even if evidence suggests the null hypothesis that the
proportion of late shipments is equal to this, for any new sample of
shipments, the proportion is likely to be a little different due to
sampling variability. Consequently, it's a good idea to state a
confidence interval. That is, you say, "we are 95% 'confident' that the
proportion of late shipments is between A and B" (for some value of A
and B).

Sampling in Python
[demonstrated](https://campus.datacamp.com/courses/sampling-in-python/bootstrap-distributions-4?ex=10)
two methods for calculating confidence intervals. Here, you'll use
quantiles of the bootstrap distribution to calculate the confidence
interval.

`late_prop_samp` and `late_shipments_boot_distn` are available; `pandas`
and `numpy` are loaded with their usual aliases.

**Instructions**

- Calculate a 95% confidence interval from `late_shipments_boot_distn`
  using the quantile method, labeling the lower and upper intervals
  `lower` and `upper`.

**Answer**

```{python}

```

## Two-Sample and ANOVA Tests

### Two sample mean test statistic

The hypothesis test for determining if there is a difference between the
means of two populations uses a different type of test statistic to the
z-scores you saw in Chapter 1. It's called "t", and it can be calculated
from three values from each sample using this equation.

\$\$ t = \dfrac{(\bar{x}\_{\text{child}} -
\bar{x}\_{\text{adult}})}{\sqrt{\dfrac{s\_{\text{child}}^2}{n\_{\text{child}}} +
\dfrac{s\_{\text{adult}}^2}{n\_{\text{adult}}}}} \$\$

While trying to determine why some shipments are late, you may wonder if
the weight of the shipments that were on time is **less than** the
weight of the shipments that were late. The `late_shipments` dataset has
been split into a "yes" group, where `late == "Yes"` and a "no" group
where `late == "No"`. The weight of the shipment is given in the
`weight_kilograms` variable.

The sample means for the two groups are available as `xbar_no` and
`xbar_yes`. The sample standard deviations are `s_no` and `s_yes`. The
sample sizes are `n_no` and `n_yes`. `numpy` is also loaded as `np`.

**Instructions**

- Calculate the numerator of the \\t\\ test statistic.
- Calculate the denominator of the \\t\\ test statistic.
- Use those two numbers to calculate the \\t\\ test statistic.

**Answer**

```{python}

```

### Visualizing the difference

Before you start running hypothesis tests, it's a great idea to perform
some exploratory data analysis; that is, calculating summary statistics
and visualizing distributions.

Here, you'll look at the proportion of county-level votes for the
Democratic candidate in 2012 and 2016, `sample_dem_data`. Since the
counties are the same in both years, these samples are paired. The
columns containing the samples are `dem_percent_12` and
`dem_percent_16`.

`dem_votes_potus_12_16` is available as `sample_dem_data`. `pandas` and
`matplotlib.pyplot` are loaded with their usual aliases.

**Instructions**

- Create a new `diff` column containing the percentage of votes for the
  democratic candidate in 2012 minus the percentage of votes for the
  democratic candidate in 2016.

**Answer**

```{python}

```

### Using ttest()

Manually calculating test statistics and transforming them with a CDF to
get a p-value is a lot of effort to compare two sample means. The
comparison of two sample means is called a t-test, and the `pingouin`
Python package has a `.ttest()` method to accomplish it. This method
provides some flexibility in how you perform the test.

As in the previous exercise, you'll explore the difference between the
proportion of county-level votes for the Democratic candidate in 2012
and 2016 to identify if the difference is significant. The hypotheses
are as follows:

\\H\_{0}\\: The proportion of democratic votes in 2012 and 2016 were the
same. \\H\_{A}\\: The proportion of democratic votes in 2012 and 2016
were different.

`sample_dem_data` is available and has the columns `diff`,
`dem_percent_12`, and `dem_percent_16` in addition to the `state` and
`county` names. `pingouin` and has been loaded along with `pandas` as
`pd`.

**Instructions**

- Conduct a t-test on the sample differences (the `diff` column of
  `sample_dem_data`), using an appropriate alternative hypothesis chosen
  from `"two-sided"`, `"less"`, and `"greater"`.

**Answer**

```{python}

```

### Visualizing many categories

So far in this chapter, we've only considered the case of differences in
a numeric variable between two categories. Of course, many datasets
contain more categories. Before you get to conducting tests on many
categories, it's often helpful to perform exploratory data analysis
(EDA), calculating summary statistics for each group and visualizing the
distributions of the numeric variable for each category using box plots.

Here, we'll return to the late shipments data, and how the price of each
package (`pack_price`) varies between the three shipment modes
(`shipment_mode`): `"Air"`, `"Air Charter"`, and `"Ocean"`.

`late_shipments` is available; `pandas` and `matplotlib.pyplot` are
loaded with their standard aliases, and `seaborn` is loaded as `sns`.

**Instructions**

- Group `late_shipments` by `shipment_mode` and calculate the mean
  `pack_price` for each group, storing the result in
  `xbar_pack_by_mode`.

**Answer**

```{python}

```

### Conducting an ANOVA test

The box plots made it look like the distribution of pack price was
different for each of the three shipment modes. However, it didn't tell
us whether the mean pack price was different in each category. To
determine that, we can use an ANOVA test. The null and alternative
hypotheses can be written as follows.

\\H\_{0}\\: Pack prices for every category of shipment mode are the
same.

\\H\_{A}\\: Pack prices for some categories of shipment mode are
different.

Use a significance level of 0.1.

`late_shipments` is available and `pingouin` has been loaded.

**Instructions**

- Run an ANOVA on `late_shipments` investigating `'pack_price'` (the
  dependent variable) between the groups of `'shipment_mode'`.

**Answer**

```{python}

```

### Pairwise t-tests

The ANOVA test didn't tell you which categories of shipment mode had
significant differences in pack prices. To pinpoint which categories had
differences, you could instead use pairwise t-tests.

`late_shipments` is available and `pingouin` has been loaded.

**Instructions**

- Perform pairwise t-tests on `late_shipments`'s `pack_price` variable,
  grouped by `shipment_mode`, without doing any p-value adjustment.

**Answer**

```{python}

```

## Proportion Tests

### Test for single proportions

In Chapter 1, you calculated a p-value for a test hypothesizing that the
proportion of late shipments was **greater than** 6%. In that chapter,
you used a bootstrap distribution to estimate the standard error of the
statistic. An alternative is to use an equation for the standard error
based on the sample proportion, hypothesized proportion, and sample
size.

\\z = \dfrac{\hat{p} - p\_{0}}{\sqrt{\dfrac{p\_{0}\*(1-p\_{0})}{n}}}\\

You'll revisit the p-value using this simpler calculation.

`late_shipments` is available. `pandas` and `numpy` are available under
their usual aliases, and `norm` is loaded from `scipy.stats`.

**Instructions**

- Hypothesize that the proportion of late shipments is 6%.
- Calculate the sample proportion of shipments where `late` equals
  `"Yes"`.
- Calculate the number of observations in the sample.

**Answer**

```{python}

```

### Test of two proportions

You may wonder if the amount paid for freight affects whether or not the
shipment was late. Recall that in the `late_shipments` dataset, whether
or not the shipment was late is stored in the `late` column. Freight
costs are stored in the `freight_cost_group` column, and the categories
are `"expensive"` and `"reasonable"`.

The hypotheses to test, with `"late"` corresponding to the proportion of
late shipments for that group, are

\\H\_{0}\\: \\late\_{\text{expensive}} - late\_{\text{reasonable}} = 0\\

\\H\_{A}\\: \\late\_{\text{expensive}} - late\_{\text{reasonable}} \>
0\\

`p_hats` contains the estimates of population proportions (sample
proportions) for each `freight_cost_group`:

    freight_cost_group  late
    expensive           Yes     0.082569
    reasonable          Yes     0.035165
    Name: late, dtype: float64

`ns` contains the sample sizes for these groups:

    freight_cost_group
    expensive     545
    reasonable    455
    Name: late, dtype: int64

`pandas` and `numpy` have been imported under their usual aliases, and
`norm` is available from `scipy.stats`.

**Instructions**

- Calculate the pooled sample proportion, \\\hat{p}\\, from `p_hats` and
  `ns`.

\$\$ \hat{p} = \frac{n\_{\text{expensive}} \times
\hat{p}\_{\text{expensive}} + n\_{\text{reasonable}} \times
\hat{p}\_{\text{reasonable}}}{n\_{\text{expensive}} +
n\_{\text{reasonable}}} \$\$

**Answer**

```{python}

```

### proportions_ztest() for two samples

That took a lot of effort to calculate the p-value, so while it is
useful to see how the calculations work, it isn't practical to do in
real-world analyses. For daily usage, it's better to use the
`statsmodels` package.

Recall the hypotheses.

\\H\_{0}\\: \\late\_{\text{expensive}} - late\_{\text{reasonable}} = 0\\

\\H\_{A}\\: \\late\_{\text{expensive}} - late\_{\text{reasonable}} \>
0\\

`late_shipments` is available, containing the `freight_cost_group`
column. `numpy` and `pandas` have been loaded under their standard
aliases, and `proportions_ztest` has been loaded from
`statsmodels.stats.proportion`.

**Instructions**

- Get the counts of the `late` column grouped by `freight_cost_group`.

**Answer**

```{python}

```

### Performing a chi-square test

The *chi-square independence test* compares proportions of successes of
one categorical variable across the categories of another categorical
variable.

Trade deals often use a form of business shorthand in order to specify
the exact details of their contract. These are International Chamber of
Commerce (ICC) international commercial terms, or *incoterms* for short.

The `late_shipments` dataset includes a `vendor_inco_term` that
describes the incoterms that applied to a given shipment. The choices
are:

- [`EXW`](https://www.investopedia.com/terms/e/exw.asp): "Ex works". The
  buyer pays for transportation of the goods.
- [`CIP`](https://www.investopedia.com/terms/c/carriage-and-insurance-paid-cip.asp):
  "Carriage and insurance paid to". The seller pays for freight and
  insurance until the goods board a ship.
- [`DDP`](https://www.investopedia.com/terms/d/delivery-duty-paid.asp):
  "Delivered duty paid". The seller pays for transportation of the goods
  until they reach a destination port.
- [`FCA`](https://www.investopedia.com/terms/f/fca.asp): "Free carrier".
  The seller pays for transportation of the goods.

Perhaps the incoterms affect whether or not the freight costs are
expensive. Test these hypotheses with a significance level of `0.01`.

\\H\_{0}\\: `vendor_inco_term` and `freight_cost_group` are independent.

\\H\_{A}\\: `vendor_inco_term` and `freight_cost_group` are associated.

`late_shipments` is available, and the following have been loaded:
`matplotlib.pyplot` as `plt`, `pandas` as `pd`, and `pingouin`.

**Instructions**

- Calculate the proportion of `freight_cost_group` in `late_shipments`
  grouped by `vendor_inco_term`.

**Answer**

```{python}

```

### Visualizing goodness of fit

The *chi-square goodness of fit test* compares proportions of each level
of a categorical variable to hypothesized values. Before running such a
test, it can be helpful to visually compare the distribution in the
sample to the hypothesized distribution.

Recall the vendor incoterms in the `late_shipments` dataset. You
hypothesize that the four values occur with these frequencies in the
population of shipments.

- `CIP`: 0.05
- `DDP`: 0.1
- `EXW`: 0.75
- `FCA`: 0.1

These frequencies are stored in the `hypothesized` DataFrame.

The `incoterm_counts` DataFrame stores the `.value_counts()` of the
`vendor_inco_term` column.

`late_shipments` is available; `pandas` and `matplotlib.pyplot` are
loaded with their standard aliases.

**Instructions**

- Find the total number of rows in `late_shipments`.

**Answer**

```{python}

```

### Performing a goodness of fit test

The bar plot of `vendor_inco_term` suggests that the distribution across
the four categories was quite close to the hypothesized distribution.
You'll need to perform a *chi-square goodness of fit test* to see
whether the differences are statistically significant.

Recall the hypotheses for this type of test:

\\H\_{0}\\: The sample matches with the hypothesized distribution.

\\H\_{A}\\: The sample does not match with the hypothesized
distribution.

To decide which hypothesis to choose, we'll set a significance level of
`0.1`.

`late_shipments`, `incoterm_counts`, and `hypothesized` from the last
exercise are available. `chisquare` from `scipy.stats` has been loaded.

**Instructions**

- Using the `incoterm_counts` and `hypothesized` datasets, perform a
  chi-square goodness of fit test on the incoterm counts, `n`.

**Answer**

```{python}

```

## Non-Parametric Tests

### Testing sample size

In order to conduct a hypothesis test and be sure that the result is
fair, a sample must meet three requirements: it is a random sample of
the population, the observations are independent, and there are enough
observations. Of these, only the last condition is easily testable with
code.

The minimum sample size depends on the type of hypothesis tests you want
to perform. You'll now test some scenarios on the `late_shipments`
dataset.

Note that the `.all()` method from `pandas` can be used to check if all
elements are true. For example, given a DataFrame `df` with numeric
entries, you check to see if all its elements are less than `5`, using
`(df < 5).all()`.

`late_shipments` is available, and `pandas` is loaded as `pd`.

**Instructions**

- Get the count of each value in the `freight_cost_group` column of
  `late_shipments`.
- Insert a suitable number to inspect whether the counts are "big
  enough" for a two sample t-test.

<!-- -->

- Get the count of each value in the `late` column of `late_shipments`.
- Insert a suitable number to inspect whether the counts are "big
  enough" for a one sample proportion test.

<!-- -->

- Get the count of each value in the `freight_cost_group` column of
  `late_shipments` grouped by `vendor_inco_term`.
- Insert a suitable number to inspect whether the counts are "big
  enough" for a chi-square independence test.

<!-- -->

- Get the count of each value in the `shipment_mode` column of
  `late_shipments`.
- Insert a suitable number to inspect whether the counts are "big
  enough" for an ANOVA test.

**Answer**

```{python}

```

### Wilcoxon signed-rank test

You'll explore the difference between the proportion of county-level
votes for the Democratic candidate in 2012 and 2016 to identify if the
difference is significant.

`sample_dem_data` is available, and has columns `dem_percent_12` and
`dem_percent_16` in addition to `state` and `county` names. The
following packages have also been loaded: `pingouin` and `pandas` as
`pd`.

**Instructions**

- Conduct a paired t-test on the percentage columns using an appropriate
  alternative hypothesis.

<!-- -->

- Conduct a Wilcoxon-signed rank test on the same columns.

**Answer**

```{python}

```

### Wilcoxon-Mann-Whitney

Another class of non-parametric hypothesis tests are called *rank sum
tests*. Ranks are the positions of numeric values from smallest to
largest. Think of them as positions in running events: whoever has the
fastest (smallest) time is rank 1, second fastest is rank 2, and so on.

By calculating on the ranks of data instead of the actual values, you
can avoid making assumptions about the distribution of the test
statistic. It's more robust in the same way that a median is more robust
than a mean.

One common rank-based test is the Wilcoxon-Mann-Whitney test, which is
like a non-parametric t-test.

`late_shipments` is available, and the following packages have been
loaded: `pingouin` and `pandas` as `pd`.

**Instructions**

- Select `weight_kilograms` and `late` from `late_shipments`, assigning
  the name `weight_vs_late`.
- Convert `weight_vs_late` from long-to-wide format, setting `columns`
  to `'late'`.
- Run a Wilcoxon-Mann-Whitney test for a difference in
  `weight_kilograms` when the shipment was late and on-time.

**Answer**

```{python}

```

### Kruskal-Wallis

Recall that the Kruskal-Wallis test is a non-parametric version of an
ANOVA test, comparing the means across multiple groups.

`late_shipments` is available, and the following packages have been
loaded: `pingouin` and `pandas` as `pd`.

**Instructions**

- Run a Kruskal-Wallis test on `weight_kilograms` between the different
  shipment modes in `late_shipments`.

**Answer**

```{python}

```
