from typing import List

from scipy import stats

from statsmodels.stats.stattools import durbin_watson, jarque_bera
from statsmodels.stats.outliers_influence import OLSInfluence


from pandas import DataFrame, concat

from functions.read_xls import read_hill_curve_dataset
from functions.statistics.model import fit_hill_curve


def influence_measures(estimates):
    # PRESS statistics
    return OLSInfluence(estimates)


def r_press(estimates):
    # R PRESS
    return (
            1 - (OLSInfluence(estimates).ess_press / estimates.ess)
    )


def shapiro_pvalue(estimates):
    # shapiro wilk normality test for small samples < 2000
    return stats.shapiro(estimates.resid)[1]


def jarque_pvalue(estimates):
    # jarque bera normality test for big samples > 2000
    return jarque_bera(estimates.resid)[1]


def stats_from_one_hill_curve_fitted(
        hill_curve: DataFrame,
        statistics: DataFrame = DataFrame(),
        N: int = 3,
) -> List[DataFrame]:
    """List of statistics estimated for N polynomials
    with degree varying of 2 to N."""

    for degree in range(2,  N + 1):

        estimates = fit_hill_curve(
            data=hill_curve, degree=degree,
        )
        stats_list = {}
        stats_list.update({
            "aic": estimates.aic,
            "bic": estimates.bic,
            "durbin_watson": durbin_watson(estimates.resid),
            "fvalue": estimates.fvalue,
            "f_pvalue": estimates.f_pvalue,
            "jarque_bera": jarque_pvalue(estimates),
            "pvalues": estimates.pvalues,
            "params": estimates.params,
            "resid": estimates.resid,
            "rsquared": estimates.rsquared,
            "rsquared_adj": estimates.rsquared_adj,
            "shapiro_pvalue": shapiro_pvalue(estimates),
            "resid_press": influence_measures(estimates).resid_press,
            "ess_press": influence_measures(estimates).ess_press,
            "ess": estimates.ess,
            "r_press": r_press(estimates),
            "delta_r": estimates.rsquared - r_press(estimates),
        })
        statistics = concat([
            statistics,
            DataFrame([stats_list], index=[degree])
        ])
    return statistics


def get_stats_from_all_hill_curves(N: int = 3) -> tuple:

    # read hill curve samples
    uhe1_data, uhe2_data, uhe3_data, uhe4_data = read_hill_curve_dataset()

    # get stats for each hill curve sample
    stats_uhe1 = stats_from_one_hill_curve_fitted(hill_curve=uhe1_data, N=N)
    stats_uhe2 = stats_from_one_hill_curve_fitted(hill_curve=uhe2_data, N=N)
    stats_uhe3 = stats_from_one_hill_curve_fitted(hill_curve=uhe3_data, N=N)
    stats_uhe4 = stats_from_one_hill_curve_fitted(hill_curve=uhe4_data, N=N)

    # transform r_press stats below zero
    stats_uhe1.loc[stats_uhe1["r_press"] < 0, "r_press"] = 0
    stats_uhe2.loc[stats_uhe2["r_press"] < 0, "r_press"] = 0
    stats_uhe3.loc[stats_uhe3["r_press"] < 0, "r_press"] = 0
    stats_uhe4.loc[stats_uhe4["r_press"] < 0, "r_press"] = 0

    return stats_uhe1, stats_uhe2, stats_uhe3, stats_uhe4
