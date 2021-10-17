import matplotlib.pyplot as plt

from functions.utils import get_file_path


def hill_curve_scatter(x, y, z):
    # figure
    fig = plt.figure()
    ax = plt.axes(projection="3d")

    # plot
    ax.scatter3D(x, y, z, color="blue")

    plt.xlabel("queda (m)", labelpad=-10, fontsize=10)
    plt.ylabel("vazão (m3/s)", labelpad=-10)
    ax.set_zlabel("rendimento (p.u.)")

    plt.tick_params(labelsize=6)

    # Turn off tick labels
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_zticklabels([])

    fig.tight_layout()

    plt.savefig(
        f"{get_file_path()}/hillCurveScatterPlot.png",
        format="png"
    )

    plt.show()
