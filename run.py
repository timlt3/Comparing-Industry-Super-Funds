#!/usr/bin/env python

import pandas as pd


def main():
    df = pd.read_excel(r'data/APRA-MySuper-Product-Heatmap.xlsx',
                       sheet_name='Heatmap')
    print(df)


if __name__ == '__main__':
    main()
