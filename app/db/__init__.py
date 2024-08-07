import sys
import site
from pathlib import Path

from icecream import ic
ic(Path(__file__).parent)
site.addsitedir(Path(__file__).parent)
ic(sys.path)
