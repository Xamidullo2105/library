from core.file_manager import read


def get_next_id(filename: str):
    all_rows = read(filename=filename)
    if all_rows:
        return int(all_rows[-1][0]) + 1
    return 1
