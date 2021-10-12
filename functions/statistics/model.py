from sklearn.preprocessing import PolynomialFeatures
from pandas import DataFrame
from statsmodels import api as sm


def get_polynomial_features(
        data: DataFrame, degree: int, include_bias: bool = False
) -> DataFrame:

    poly = PolynomialFeatures(degree=degree, include_bias=include_bias)
    # create features and transform to data frame
    features = DataFrame(poly.fit_transform(data))
    # rename data frame columns
    names_list = list()
    feature_names = poly.get_feature_names(data.columns)
    [names_list.append(x.replace(" ", "").replace("^", "")) for x in feature_names]
    features.columns = names_list
    return features


def fit_hill_curve(
        data: DataFrame,
        degree: int = 3,
) -> object:
    """
    Hill Curve stats estimated from polynomial regression
        using Ordinary Last Square
    """
    explained = DataFrame(data["rendimento"])
    explained.columns = ['R']

    # features do not include bias variable
    features = get_polynomial_features(
        data=data[["queda", "vazao"]],
        degree=degree,
        include_bias=False
    )
    model = sm.OLS(explained, features)
    return model.fit()
