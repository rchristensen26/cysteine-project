from os.path import join
import os

configfile: "config/config.yml"

# make list of nt HMMER genomes to search
# nt_strain_fpaths = os.listdir(config["ntGenomeDir"])
# NT_STRAINS = []
# for fpath in nt_strain_fpaths:
#     NT_STRAINS.append(os.path.splitext(fpath)[0])

# with open("config/strain_list.txt",'w') as f:
#     for strain in NT_STRAINS:
#         f.write(strain)
#         f.write('\n')

with open("config/strain_list.txt", 'r') as f:
    strains = f.read()
    NT_STRAINS = strains.split()

# # make list of genes
# profileHMM_fpaths = os.listdir(config["profileHMM_Dir"])
# GENES = []
# for fpath in profileHMM_fpaths:
#     GENES.append(os.path.splitext(fpath)[0])
#
# with open("config/gene_list.txt",'w') as f:
#     for gene in GENES:
#         f.write(gene)
#         f.write('\n')

with open("config/gene_list.txt", 'r') as f:
    genes = f.read()
    GENES = genes.split()

# # make list of reference gene fasta files (to build profile HMMs)
# faa_fpaths = os.listdir(config["refGene_Dir"])
# PHMM_GENES = []
# for fpath in faa_fpaths:
#     PHMM_GENES.append(os.path.splitext(fpath)[0])


rule all:
    input:
        expand("config/referenceGeneMSA/{gene}_msa.faa", gene=PHMM_GENES),
        expand("config/profileHMMs/{gene}.HMM", gene=PHMM_GENES),
        expand(join(config["geneCoordDir"],"{strain}_geneCoord.out"), strain=NT_STRAINS),
        expand(join(config["proteinSeqDir"],"{strain}_prodigal.faa"), strain=NT_STRAINS),
        expand("workflow/out/{gene}/hmmer_output/{strain}_{gene}.hmm.out",strain=NT_STRAINS,gene=GENES),
        expand("workflow/out/{gene}/hmmer_output/{strain}_{gene}.domtblout",strain=NT_STRAINS,gene=GENES),
        expand("workflow/out/{gene}/hmmer_output/{strain}_{gene}.sto",strain=NT_STRAINS,gene=GENES),
        expand("workflow/out/{gene}/csv_summary/{strain}_{gene}_hits.csv",strain=NT_STRAINS,gene=GENES),
        expand("workflow/out/{gene}/faa_summary/{strain}_{gene}_hits.faa",strain=NT_STRAINS,gene=GENES),
        expand("workflow/out/summary_all/csv_summary/compiled_{gene}_hits.csv", gene=GENES),
        expand("workflow/out/summary_all/faa_summary/compiled_{gene}_hits.faa", gene=GENES)


include:
    # "workflow/rules/makeProfileHMM.smk",
    "workflow/rules/runHMMER.smk"
