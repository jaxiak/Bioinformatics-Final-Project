import pandas as pd
import glob
import os

path = 'data/tsv' # use your path
all_files = glob.glob(os.path.join(path , "*.tsv"))
fails = []
print(len(all_files))
for filename in all_files:
    df1 = pd.read_csv(filename, delimiter= '\t',  encoding="utf-8")
    # print(df)
    df2 = pd.read_parquet('data/parquet/' + filename[9:-4] + '.parquet')
    match =(df1 == df2).all().all()
    print(filename[9:-4], match)
    if not match:
        fails.append(filename[9:-4])
print(fails)
breakpoint()
