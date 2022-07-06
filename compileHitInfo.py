"""
This code adds info for species that have hits for each gene and adds it to a CSV file
^ i can't make words today
"""

import csv
import os
import pandas as pd

file_path = '/Users/rebeccachristensen/Desktop/Cremer_Lab_2022/cysteine_utilization_project/main/workflow/out/summary_all/compiled_hits_allGenes_customProfiles.csv'
# output_file_path = "/Users/rebeccachristensen/Desktop/Cremer_Lab_2022/cysteine_utilization_project/main/workflow/out/summary_all/gene_strain_results_customProfiles.csv"
score_file = '/Users/rebeccachristensen/Desktop/Cremer_Lab_2022/cysteine_utilization_project/main/workflow/out/summary_all/maxHitScoreDF.csv'
len_file = '/Users/rebeccachristensen/Desktop/Cremer_Lab_2022/cysteine_utilization_project/main/workflow/out/summary_all/maxHSPLen.csv'
hspScore_file = "/Users/rebeccachristensen/Desktop/Cremer_Lab_2022/cysteine_utilization_project/main/workflow/out/summary_all/maxHSPScoreDF.csv"
# # make list of strains
# STRAINS = []
# strain_fpaths = os.listdir("/Users/rebeccachristensen/Desktop/Cremer_Lab_2022/cysteine_utilization_project/main/config/strain_genomes/nt")
# for fpath in strain_fpaths:
#     STRAINS.append(os.path.splitext(fpath)[0])
#
# strain_fpaths = os.listdir("/Users/rebeccachristensen/Desktop/Cremer_Lab_2022/cysteine_utilization_project/main/config/strain_genomes/NinjaMapFastaFiles")
# for fpath in strain_fpaths:
#     STRAINS.append(os.path.splitext(fpath)[0])
#
# # make list of genes
# profileHMM_fpaths = os.listdir("/Users/rebeccachristensen/Desktop/Cremer_Lab_2022/cysteine_utilization_project/main/config/profileHMMs")
# GENES = []
# for fpath in profileHMM_fpaths:
#     GENES.append(os.path.splitext(fpath)[0])
#
# csv_dictWriter_rows = []
#
# # make empty dict
# for strain in STRAINS:
#     strain_dict = {"species": strain}
#     for gene in GENES:
#         strain_dict[gene] = ""
#     csv_dictWriter_rows.append(strain_dict)

# fieldnames = ["species", GENES]
# with open(file_path, 'w') as f:
#     csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
#     for item in csv_dictWriter_rows:
#         csv_writer.writerow(item)

# keys = csv_dictWriter_rows[0].keys()

# file = open(file_path, "w")
# dict_writer = csv.DictWriter(file, keys)
# dict_writer.writeheader()
# dict_writer.writerows(csv_dictWriter_rows)
# file.close()

# create CSV file with strains and profile HMM results
# no duplicate values for strain+profile HMM combinations
# df = pd.read_csv(file_path, usecols=[0], names=['bingbong'])
# df = df['bingbong'].str.rsplit("_", 1, expand=True)
# df.drop_duplicates(inplace=True)
# df.to_csv(output_file_path)

# now, i wanna make a csv file with only the highest score value per strain per profile HMM
df = pd.read_csv(file_path)
# make new column for strain name and profile HMM
df[["strain", "pHMM"]] = df['description'].str.rsplit("_", 1, expand=True)
score_df = df.groupby(["strain", "pHMM"], as_index=False).hit_score.max()
score_df.to_csv(score_file)

len_df = df.groupby(["strain", "pHMM"], as_index=False).hsp_len.max()
len_df.to_csv(len_file)

hspScore_df = df.groupby(["strain", "pHMM"], as_index=False).hsp_score.max()
hspScore_df.to_csv(hspScore_file)

