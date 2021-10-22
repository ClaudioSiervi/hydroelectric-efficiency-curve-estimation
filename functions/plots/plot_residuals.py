
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd


def plot_regression_residuals(
        hill_curve, statistics
) -> None:

    data_dict = {
        'queda': hill_curve["queda"],
        'vazao': hill_curve["vazao"],
        'residuo': statistics.resid.values[0]
    }

    residuals = pd.DataFrame(data=data_dict)
    residuo = residuals["residuo"]
    queda = residuals["queda"]
    vazao = residuals["vazao"]

    fig = plt.figure(figsize=plt.figaspect(0.4))

    # First subplot - scatter
    ax = fig.add_subplot(1, 3, 1)
    ax.scatter(queda, residuo, color="C7")

    plt.title("Dispersão queda x resíduo");
    plt.xlabel("Queda")
    plt.ylabel("Resíduo")
    plt.tick_params(labelsize=8)

    # Second subplot - scatter
    ax = fig.add_subplot(1, 3, 2)
    ax.scatter(vazao, residuo, color="C7")

    plt.title("Dispersão vazão x resíduo");
    plt.xlabel("Vazão")
    plt.ylabel("Resíduo")
    plt.tick_params(labelsize=8)

    # Third subplot - Quantile-QuantilePlot
    ax = fig.add_subplot(1, 3, 3)

    pp = sm.ProbPlot(residuo, fit=True)

    pp.qqplot(
        ax=ax,
        ylabel="Quantis amostrais",
        xlabel="Quantis teóricos",
        markerfacecolor="k",
        markeredgecolor="k",
        color="C7",
        line="45",
        alpha=0.3
    )
    plt.title("Normal QQplot")

    fig.tight_layout()
    plt.show()

