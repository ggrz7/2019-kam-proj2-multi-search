import os
import sys

import pandas as pd


def search_data(data):
    print(data)


def search_data_argparse(args):
    if args.data is None or not (os.path.exists(args.data) and os.path.isfile(args.data)):
        print('"%s" is not a valid path, please enter a path to your "data.csv"...' % args.path)
        sys.exit(0)

    search_data(data=pd.read_csv(args.data, header=None))
