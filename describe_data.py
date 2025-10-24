import pandas as pd
import glob
import os

path = 'data/parquet' # use your path
all_files = glob.glob(os.path.join(path , "*.parquet"))
print(len(all_files))
important_files = ['data/parquet/TCGA-BRCA.clinical.parquet','data/parquet/TCGA-BRCA.star_counts.parquet', 'data/parquet/TCGA-BRCA.gene-level_absolute.parquet' ]
# for filename in all_files:
for filename in important_files:
    df = pd.read_parquet('data/parquet/' + filename[13:-8] + '.parquet')
    print(filename[13:-4])
    # print(df)
    # print(df.describe())
    breakpoint()