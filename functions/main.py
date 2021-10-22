####
#   This code is from the research:
#   Hydroelectric Efficiency Curve Estimation
####
# by Claudio Siervi Mota Junior
# claudio.siervi@gmail.com

from functions.plots.plot_estimates import plot_estimated_metrics
from functions.read_xls import read_hill_curve_dataset
from functions.statistics.model import get_polynomial_features, fit_hill_curve
from functions.statistics.stats import (
    get_stats_from_all_hill_curves, stats_from_one_hill_curve_fitted
)


def read_data():
    uhe1_data, uhe2_data, uhe3_data, uhe4_data = read_hill_curve_dataset()
    uhe1_data.describe()

    X = get_polynomial_features(uhe1_data, 3, False)
    print(X.head(5))

    results = fit_hill_curve(
        data=uhe1_data, degree=5
    )
    print(results.resid)

    r = stats_from_one_hill_curve_fitted(hill_curve=uhe1_data, N=5)
    print(list(r))
    print(r["fvalue"])

    stats_uhe1, stats_uhe2, stats_uhe3, stats_uhe4 = get_stats_from_all_hill_curves(N=5)
    print(stats_uhe1["fvalue"])


def statistics():
    degree = 5

    from functions.statistics.stats import get_stats_from_all_hill_curves

    stats_uhe1, _, _, _ = \
        get_stats_from_all_hill_curves(N=degree)

    type(stats_uhe1)
    stats_uhe1.head(5)

    plot_estimated_metrics(
        turbine_name="Turbina A",
        statistics=stats_uhe1,
        degree=degree
    )
    return stats_uhe1


def residuals(stats_uhe1):
    from functions.read_xls import read_hill_curve
    from functions.plots.plot_residuals import plot_regression_residuals

    cc_uhe1 = read_hill_curve(sheet_name="THG1")
    plot_regression_residuals(cc_uhe1, stats_uhe1)


if __name__ == '__main__':
    stats = statistics()
    residuals(stats)

