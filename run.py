#!/usr/bin/env python

import pandas as pd


def main():
    df = pd.read_excel(r'data/heatmap2.0.xlsx',
                       sheet_name='singleStrategy1.0')
    print(df)


if __name__ == '__main__':
    main()
