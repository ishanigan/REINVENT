import pickle
from rdkit import Chem
from smiles_to_bandgap import get_bandgap_openbabel
from utils import sa_score, pickle_to_data, percentage_unique
import numpy as np
import matplotlib.pyplot as plt

# import qm9 dataset
train_smiles_list, train_bandgap = pickle_to_data("data//qm9_key_smiles_1_full_train_data.pickle")
holdout_smiles_list, holdout_bandgap = pickle_to_data("data//qm9_key_smiles_1_holdout_data.pickle")
full_qm9_smiles_list = train_smiles_list + holdout_smiles_list

# export test smiles to usable file 
def write_smiles_to_file(smiles_list, fname):
    """Write a list of SMILES to a file."""
    with open(fname, 'w') as f:
        for smiles in smiles_list:
            f.write(smiles + "\n")
            
# currently using training smiles, but can use any subset of QM9
train_smiles = train_smiles_list 
write_smiles_to_file(train_smiles, 'mols.smi')