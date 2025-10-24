import pandas as pd

response = 'disease_type'
x_data = 'TCGA-BRCA.star_counts'
df_phenotype = pd.read_parquet('data/parquet/TCGA-BRCA.clinical.parquet')
df_X = pd.read_parquet('data/parquet/' + x_data + '.parquet')
df_X_T = df_X.set_index(df_X['Ensembl_ID']).drop(columns = 'Ensembl_ID').T 

data = df_phenotype[['sample', response]].set_index('sample').join(df_X_T)
data.to_parquet('data/parquet/' + x_data + '_' + response + '.parquet')

p_in_X = 0
p_in_X_samples = []
p_not_in_X = 0
X_in_P = 0
X_in_P_samples = []
X_not_in_P = 0
for samp in df_phenotype['sample']:
    if samp in df_X_T.index:
        p_in_X += 1
        p_in_X_samples.append(samp)
    else:
        p_not_in_X += 1
for samp in df_X_T.index:
    if samp in df_phenotype['sample'].values:
        X_in_P += 1
        X_in_P_samples.append(samp)
    else:
        X_not_in_P += 1

print("Phenotype samples in " + x_data + " data :" + str(p_in_X))
print("Phenotype samples not in " + x_data + " data :" + str(p_not_in_X))
print(x_data + " samples in Phenotype data :" + str(X_in_P))
print(x_data + " samples not in Phenotype data :" + str(X_not_in_P))