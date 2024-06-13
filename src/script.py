# added/edited
import pandas as pd

late_shipments = pd.read_feather("late_shipments.feather")


# Print the late_shipments dataset
print(late_shipments)

# Calculate the proportion of late shipments
late_prop_samp = (late_shipments["late"] == "Yes").mean()

# Print the results
print(late_prop_samp)


# added/edited
import numpy as np

late_shipments_boot_distn = [
    late_shipments.sample(n=len(late_shipments), replace=True)["late_delivery"].mean()
    for _ in range(5000)
]


# Hypothesize that the proportion is 6%
late_prop_hyp = 0.06

# Calculate the standard error
std_error = np.std(late_shipments_boot_distn, ddof=1)

# Find z-score of late_prop_samp
z_score = (late_prop_samp - late_prop_hyp) / std_error

# Print z_score
print(z_score)


# added/edited
from scipy.stats import norm


# Calculate the z-score of late_prop_samp
z_score = (late_prop_samp - late_prop_hyp) / std_error

# Calculate the p-value
p_value = 1 - norm.cdf(z_score)

# Print the p-value
print(p_value)


# Calculate 95% confidence interval using quantile method
lower = np.quantile(late_shipments_boot_distn, 0.025)
upper = np.quantile(late_shipments_boot_distn, 0.975)

# Print the confidence interval
print((lower, upper))

# added/edited
late_yes = late_shipments[late_shipments["late_delivery"] == 1]
late_no = late_shipments[late_shipments["late_delivery"] == 0]
xbar_no = late_no["weight_kilograms"].mean()
xbar_yes = late_yes["weight_kilograms"].mean()
s_no = late_no["weight_kilograms"].std()
s_yes = late_yes["weight_kilograms"].std()
n_no = late_no["weight_kilograms"].count()
n_yes = late_yes["weight_kilograms"].count()
numerator = xbar_no - xbar_yes


# Calculate the numerator of the test statistic
numerator = xbar_no - xbar_yes

# Calculate the denominator of the test statistic
denominator = np.sqrt(s_no**2 / n_no + s_yes**2 / n_yes)

# Calculate the test statistic
t_stat = numerator / denominator

# Print the test statistic
print(t_stat)

# added/edited
from scipy.stats import t


# Calculate the degrees of freedom
degrees_of_freedom = n_no + n_yes - 2

# Calculate the p-value from the test stat
p_value = t.cdf(t_stat, df=degrees_of_freedom)

# Print the p_value
print(p_value)


# added/edited
import matplotlib.pyplot as plt

sample_dem_data = pd.read_feather("dem_votes_potus_12_16.feather")


# Calculate the differences from 2012 to 2016
sample_dem_data["diff"] = (
    sample_dem_data["dem_percent_12"] - sample_dem_data["dem_percent_16"]
)

# Print sample_dem_data
print(sample_dem_data)


# Find the mean of the diff column
xbar_diff = sample_dem_data["diff"].mean()

# Print xbar_diff
print(xbar_diff)

# Find the standard deviation of the diff column
s_diff = sample_dem_data["diff"].std()

# Print s_diff
print(s_diff)

# Plot a histogram of diff with 20 bins
sample_dem_data["diff"].hist(bins=20)
plt.show()


# added/edited
import pingouin


# Conduct a t-test on diff
test_results = pingouin.ttest(x=sample_dem_data["diff"], y=0, alternative="two-sided")

# Print the test results
print(test_results)


# Conduct a paired t-test on dem_percent_12 and dem_percent_16
paired_test_results = pingouin.ttest(
    x=sample_dem_data["dem_percent_12"],
    y=sample_dem_data["dem_percent_16"],
    paired=True,
    alternative="two-sided",
)

# Print the paired test results
print(paired_test_results)

# added/edited
import seaborn as sns


# Calculate the mean pack_price for each shipment_mode
xbar_pack_by_mode = late_shipments.groupby("shipment_mode")["pack_price"].mean()

# Print the grouped means
print(xbar_pack_by_mode)


# Calculate the standard deviation of the pack_price for each shipment_mode
s_pack_by_mode = late_shipments.groupby("shipment_mode")["pack_price"].std()

# Print the grouped standard deviations
print(s_pack_by_mode)

# Boxplot of shipment_mode vs. pack_price
sns.boxplot(x="pack_price", y="shipment_mode", data=late_shipments)
plt.show()


# Run an ANOVA for pack_price across shipment_mode
anova_results = pingouin.anova(
    data=late_shipments, dv="pack_price", between="shipment_mode"
)

# Print anova_results
print(anova_results)


# Perform a pairwise t-test on pack price, grouped by shipment mode
pairwise_results = pingouin.pairwise_tests(
    data=late_shipments, dv="pack_price", between="shipment_mode", padjust="none"
)

# Print pairwise_results
print(pairwise_results)


# Modify the pairwise t-tests to use Bonferroni p-value adjustment
pairwise_results = pingouin.pairwise_tests(
    data=late_shipments, dv="pack_price", between="shipment_mode", padjust="bonf"
)

# Print pairwise_results
print(pairwise_results)


# Hypothesize that the proportion of late shipments is 6%
p_0 = 0.06

# Calculate the sample proportion of late shipments
p_hat = (late_shipments["late"] == "Yes").mean()

# Calculate the sample size
n = len(late_shipments)

# Print p_hat and n
print(p_hat, n)


# Calculate the numerator and denominator of the test statistic
numerator = p_hat - p_0
denominator = np.sqrt(p_0 * (1 - p_0) / n)

# Calculate the test statistic
z_score = numerator / denominator

# Print the result
print(z_score)


# Calculate the p-value from the z-score
p_value = 1 - norm.cdf(z_score)

# Print the p-value
print(p_value)

# added/edited
late_shipments["freight_cost_group"] = late_shipments["freight_cost_groups"].fillna(
    "expensive"
)
p_hats = late_shipments.groupby(["freight_cost_group"])["late_delivery"].mean()
ns = late_shipments.groupby("freight_cost_group").size()


# Calculate the pooled estimate of the population proportion
p_hat = (
    p_hats["reasonable"] * ns["reasonable"] + p_hats["expensive"] * ns["expensive"]
) / (ns["reasonable"] + ns["expensive"])

# Print the result
print(p_hat)

# Calculate p_hat one minus p_hat
p_hat_times_not_p_hat = p_hat * (1 - p_hat)

# Divide this by each of the sample sizes and then sum
p_hat_times_not_p_hat_over_ns = (
    p_hat_times_not_p_hat / ns["expensive"] + p_hat_times_not_p_hat / ns["reasonable"]
)

# Calculate the standard error
std_error = np.sqrt(p_hat_times_not_p_hat_over_ns)

# Print the result
print(std_error)

# Calculate the z-score
z_score = (p_hats["expensive"] - p_hats["reasonable"]) / std_error

# Print z_score
print(z_score)

# Calculate the p-value from the z-score
p_value = 1 - norm.cdf(z_score)

# Print p_value
print(p_value)

# added/edited
from statsmodels.stats.proportion import proportions_ztest


# Count the late column values for each freight_cost_group
late_by_freight_cost_group = late_shipments.groupby("freight_cost_group")[
    "late"
].value_counts()

# Print the counts
print(late_by_freight_cost_group)


# Count the late column values for each freight_cost_group
late_by_freight_cost_group = late_shipments.groupby("freight_cost_group")[
    "late"
].value_counts()

# Create an array of the "Yes" counts for each freight_cost_group
success_counts = np.array([45, 16])

# Create an array of the total number of rows in each freight_cost_group
n = np.array([45 + 500, 16 + 439])

# Run a z-test on the two proportions
stat, p_value = proportions_ztest(count=success_counts, nobs=n, alternative="larger")

# Print the results
print(stat, p_value)

# added/edited
late_shipments = late_shipments[late_shipments.vendor_inco_term != "DDU"]


# Proportion of freight_cost_group grouped by vendor_inco_term
props = late_shipments.groupby("vendor_inco_term")["freight_cost_group"].value_counts(
    normalize=True
)

# Print props
print(props)


# Convert props to wide format
wide_props = props.unstack()

# Print wide_props
print(wide_props)

# Proportional stacked bar plot of freight_cost_group vs. vendor_inco_term
wide_props.plot(kind="bar", stacked=True)
plt.show()


# Determine if freight_cost_group and vendor_inco_term are independent
expected, observed, stats = pingouin.chi2_independence(
    data=late_shipments, x="vendor_inco_term", y="freight_cost_group"
)

# Print results
print(stats[stats["test"] == "pearson"])

# added/edited
hypothesized_dict = {
    "vendor_inco_term": ["CIP", "DDP", "EXW", "FCA"],
    "prop": [0.05, 0.10, 0.75, 0.10],
}
hypothesized = pd.DataFrame(hypothesized_dict, index=[1, 2, 0, 3])
incoterm_counts = (
    late_shipments.groupby("vendor_inco_term")["vendor_inco_term"]
    .count()
    .reset_index(name="n")
)


# Find the number of rows in late_shipments
n_total = len(late_shipments)

# Print n_total
print(n_total)

# Create n column that is prop column * n_total
hypothesized["n"] = hypothesized["prop"] * n_total

# Print the modified hypothesized DataFrame
print(hypothesized)

# Plot a red bar graph of n vs. vendor_inco_term for incoterm_counts
plt.bar(
    incoterm_counts["vendor_inco_term"],
    incoterm_counts["n"],
    color="red",
    label="Observed",
)
plt.legend()
plt.show()


# Plot a red bar graph of n vs. vendor_inco_term for incoterm_counts
plt.bar(
    incoterm_counts["vendor_inco_term"],
    incoterm_counts["n"],
    color="red",
    label="Observed",
)

# Add a blue bar plot for the hypothesized counts
plt.bar(
    hypothesized["vendor_inco_term"],
    hypothesized["n"],
    alpha=0.5,
    color="blue",
    label="Hypothesized",
)
plt.legend()
plt.show()

# added/edited
from scipy.stats import chisquare


# Perform a goodness of fit test on the incoterm counts n
gof_test = chisquare(f_obs=incoterm_counts["n"], f_exp=hypothesized["n"])

# Print gof_test results
print(gof_test)


# Count the freight_cost_group values
counts = late_shipments["freight_cost_group"].value_counts()

# Print the result
print(counts)

# Inspect whether the counts are big enough
print((counts >= 30).all())


# Count the late values
counts = late_shipments["late"].value_counts()

# Print the result
print(counts)

# Inspect whether the counts are big enough
print((counts >= 10).all())


# Count the values of freight_cost_group grouped by vendor_inco_term
counts = late_shipments.groupby("vendor_inco_term")["freight_cost_group"].value_counts()

# Print the result
print(counts)

# Inspect whether the counts are big enough
print((counts >= 5).all())


# Count the shipment_mode values
counts = late_shipments["shipment_mode"].value_counts()

# Print the result
print(counts)

# Inspect whether the counts are big enough
print((counts >= 30).all())


# Conduct a paired t-test on dem_percent_12 and dem_percent_16
paired_test_results = pingouin.ttest(
    x=sample_dem_data["dem_percent_12"],
    y=sample_dem_data["dem_percent_16"],
    paired=True,
    alternative="two-sided",
)

# Print paired t-test results
print(paired_test_results)


# Conduct a Wilcoxon test on dem_percent_12 and dem_percent_16
wilcoxon_test_results = pingouin.wilcoxon(
    x=sample_dem_data["dem_percent_12"],
    y=sample_dem_data["dem_percent_16"],
    alternative="two-sided",
)

# Print Wilcoxon test results
print(wilcoxon_test_results)


# Select the weight_kilograms and late columns
weight_vs_late = late_shipments[["weight_kilograms", "late"]]

# Convert weight_vs_late into wide format
weight_vs_late_wide = weight_vs_late.pivot(columns="late", values="weight_kilograms")

# Run a two-sided Wilcoxon-Mann-Whitney test on weight_kilograms vs. late
wmw_test = pingouin.mwu(
    x=weight_vs_late_wide["No"], y=weight_vs_late_wide["Yes"], alternative="two-sided"
)

# Print the test results
print(wmw_test)


# Run a Kruskal-Wallis test on weight_kilograms vs. shipment_mode
kw_test = pingouin.kruskal(
    data=late_shipments, dv="weight_kilograms", between="shipment_mode"
)

# Print the results
print(kw_test)
