import glob
from os.path import basename, isfile, join


def get_modules_by_pattern(folder: str, file_pattern: str):
    """Gets all files with given pattern

    Args:
        file_pattern (str): pattern to search files for

    Returns:
        list[str]: list with file names
    """

    files = glob.glob(join(folder, file_pattern))
    return [
        basename(f)[:-3] for f in files if isfile(f) and not f.endswith("__init__.py")
    ]
