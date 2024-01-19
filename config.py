from pathlib import Path

PROJECT_ROOT: Path = Path(__file__).parent.parent
file_path = PROJECT_ROOT.joinpath('src/items.csv')
