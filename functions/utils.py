
def get_image_path():
    import pathlib
    path = str(pathlib.Path(__file__).parent.resolve())
    return path.replace("/functions", "/src/images")


def get_data_path():
    import pathlib
    path = str(pathlib.Path(__file__).parent.resolve())
    return path.replace("/functions", "/src/data")
