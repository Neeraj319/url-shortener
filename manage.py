from models import create_table
import sys

if sys.argv[1] == "migrate":
    create_table()
