
import matplotlib.pyplot as plt


def plot_statistics_dots_line(
        metric, df_data, ax, degree, ylabel="", yaxis=[]
) -> None:
    """
        Transform axes and indexes
    """
    # plot metric estimated for each polynomial model
    ticks = [tick for tick in range(2, degree+1)]
    ax.plot(
        ticks,
        df_data[metric],
        'bo-'
    )
    # set yaxis limits
    if yaxis != []:
        ax.set_ylim(yaxis[0], yaxis[1])
    # set ylabel
    if ylabel == "":
        ylabel = metric
    ax.set_ylabel(ylabel)
    ax.set_xlabel("Modelos")


def plot_estimated_metrics(turbine_name, statistics, degree):
    # TODO receber uma lista de métricas das função nível acima
    metric1 = "rsquared_adj"  # penaliza muitas variáveis
    metric2 = "ess_press"  # penaliza modelos com baixo poder preditivo
    metric3 = "aic"  # penaliza muitas variáveis
    metric4 = "f_pvalue"
    metric5 = "fvalue"
    metric6 = "bic"

    formulas_dict = {}

    for d in range(2, degree+1):
        formulas_dict.update({d: str(d)})


    # TODO ajustar os eixos de cada plot
    # TODO mudar a cor dos gráficos
    fig1 = plt.figure(figsize=plt.figaspect(0.4))
    ax1 = fig1.add_subplot(1, 3, 1)  # subplot 1
    ax2 = fig1.add_subplot(1, 3, 2)  # "    2
    ax3 = fig1.add_subplot(1, 3, 3)  # "    3

    plot_statistics_dots_line(
        metric1, statistics, ax1, degree, "$R^2$ ajustado", [0.799, 1.01]
    )
    plot_statistics_dots_line(
        metric2, statistics, ax2, degree, "PRESS", [0, 0.021]
    )
    plot_statistics_dots_line(
        metric3, statistics, ax3, degree, "AIC"
    )
    # fig1.autofmt_xdate(rotation=90)
    fig1.tight_layout()
    plt.show()

    fig2 = plt.figure(figsize=plt.figaspect(0.4))
    ax4 = fig2.add_subplot(1, 3, 1)  # "    4
    ax5 = fig2.add_subplot(1, 3, 2)  # "    5
    ax6 = fig2.add_subplot(1, 3, 3)  # "    6
    plot_statistics_dots_line(metric4, statistics, ax4, degree)
    plot_statistics_dots_line(metric5, statistics, ax5, degree)
    plot_statistics_dots_line(metric6, statistics, ax6, degree)
    # fig2.autofmt_xdate(rotation=90)
    fig2.tight_layout()
    plt.show()
