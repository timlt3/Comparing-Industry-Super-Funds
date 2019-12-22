#!/usr/bin/env python

import pandas as pd


def main():
    df = pd.read_excel(r'APRA-MySuper-Product-Heatmap.xlsx')
    print(df)


if __name__ == '__main__':
    main()
