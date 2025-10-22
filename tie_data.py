import pandas as pd

response = 'disease_type'
x_data = 'TCGA-BRCA.star_counts'
df_phenotype = pd.read_parquet('data/parquet/TCGA-BRCA.clinical.parquet')
df_X = pd.read_parquet('data/parquet/' + x_data + '.parquet')
df_X_T = df_X.set_index(df_X['Ensembl_ID']).drop(columns = 'Ensembl_ID').T 

data = df_phenotype[['sample', response]].set_index('sample').join(df_X_T)
data.to_parquet('data/parquet/' + x_data + '_' + response + '.parquet')
