from _ast import If
from typing import List

from pandas import DataFrame

import warnings

warnings.filterwarnings('ignore')


class Turbine:
    """Facade to wrapper turbine logic"""
    name: str
    type: str
    hill_curve: DataFrame
    five_numbers: DataFrame
    position_measures: DataFrame
    dispersion_measures: DataFrame
    percentile: DataFrame
    net_head: DataFrame
    water_flow: DataFrame
    efficiency: DataFrame
    stats: List[DataFrame]

    def load_data(self) -> None:
        from functions.read_xls import read_hill_curve

        self.hill_curve = read_hill_curve(sheet_name="THG1")

        self.net_head = self.hill_curve["queda"]
        self.water_flow = self.hill_curve["vazao"]
        self.efficiency = self.hill_curve["rendimento"]

    def pair_plot(self) -> None:
        """scatter plot 2D e frequency distribution plot"""
        import seaborn as sns

        sns.pairplot(
            data=self.hill_curve,
            height=2.0,
            corner=True
        )

    def scatter_plot_3d(self) -> None:
        from functions.plots.plot_hill_curves import \
            hill_curve_scatter

        hill_curve_scatter(
            self.net_head,
            self.water_flow,
            self.efficiency
        )

    def calculate_stats(self, polynomial_degree: int = 3) -> List[DataFrame]:
        from functions.statistics.stats import \
            stats_from_one_hill_curve_fitted

        self.stats = stats_from_one_hill_curve_fitted(
            hill_curve=self.hill_curve, N=polynomial_degree
        )

    def plot_estimated_metrics(self, polynomial_degree: int = 3) -> None:
        from functions.plots.plot_estimates import \
            plot_estimated_metrics

        plot_estimated_metrics(
            turbine_name=self.name,
            statistics=self.stats,
            degree=polynomial_degree
        )

    def plot_regression_residuals(self) -> None:
        from functions.plots.plot_residuals import \
            plot_regression_residuals

        plot_regression_residuals(self.hill_curve, self.stats)

    def five_number_stats(self):
        return DataFrame(
            round(
                self.hill_curve.describe(
                    [.1, .2, .3, .4, .5, .6, .7, .8, .9]
                ),
                2
            )
        )

    def cont_mean_std(self) -> DataFrame:
        return self.five_numbers.iloc[0:2]

    def percentile(self) -> DataFrame:
        return self.five_numbers.iloc[3:14]

    def __init__(self) -> None:
        # polynomial_degree: max degree of polynomials to be fitted

        self.name = "Turbine A"
        self.type = "Type no specified"

        self.load_data()
        self.five_numbers = self.five_number_stats()
        self.dispersion_measures = self.cont_mean_std()
        self.position_measures = self.percentile()

    def __str__(self) -> str:
        return f"{self.name}: {self.type}"
