import pandas as pd
import glob
import os
from tqdm import tqdm
path = 'data' # use your path
all_files = glob.glob(os.path.join(path , "*.tsv"))
print(len(all_files))
print(all_files)
for filename in tqdm(all_files):
    print('output/' + filename[:-4] + '.parquet')
    df = pd.read_csv(filename, delimiter= '\t', low_memory = False, encoding="utf-8")
    # print(df)
    df.to_parquet('output/' + filename[:-4] + '.parquet')
