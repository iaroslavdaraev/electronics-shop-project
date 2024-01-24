from pathlib import Path

PROJECT_ROOT: Path = Path(__file__).parent
file_path = PROJECT_ROOT.joinpath('src', 'items.csv')
broken_file_path = PROJECT_ROOT.joinpath('src', 'bad_items.csv')
