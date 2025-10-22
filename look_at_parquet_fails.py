parquet_fails = ['TCGA-BRCA.clinical', 'TCGA-BRCA.gene-level_absolute', 'TCGA-BRCA.gene-level_ascat-ngs', 'TCGA-BRCA.gene-level_ascat2', 'TCGA-BRCA.gene-level_ascat3', 'TCGA-BRCA.methylation27', 'TCGA-BRCA.protein', 'TCGA-BRCA.somaticmutation_wxs']

import pandas as pd
from random import random

path = 'data/tsv' # use your path
for filename in parquet_fails:
    df1 = pd.read_csv('data/tsv/' + filename + '.tsv', delimiter= '\t',  encoding="utf-8")
    # print(df)
    df2 = pd.read_parquet('data/parquet/' + filename + '.parquet')
    # print(df1)
    # print(df2)
    element_equalities = df1 == df2
    # print(element_equalities)
    column_equalities = element_equalities.all()
    # print(column_equalities)
    frame_equality = column_equalities.all()
    # print(frame_equality)
    for col in df1.columns:
        if random() > 0.05:
            if not column_equalities[col]:
                compare_df = pd.concat([df1[col], df2[col]], axis = 1)
                # print(compare_df)
                print(compare_df[~(df1[col] == df2[col])])
                # breakpoint()
