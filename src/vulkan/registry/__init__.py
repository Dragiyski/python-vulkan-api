def __init__():
    from .repository import update as update_files
    import pathlib
    registry_dir = pathlib.Path(__file__).resolve().parent
    registry_files = update_files(registry_dir)

__init__()
