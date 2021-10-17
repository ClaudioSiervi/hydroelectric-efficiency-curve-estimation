
def get_file_path():
    import pathlib
    path = str(pathlib.Path(__file__).parent.resolve())
    return path.replace("/functions", "/src/images")
