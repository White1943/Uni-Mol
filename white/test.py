import numpy as np
from unimol_tools import UniMolRepr

clf = UniMolRepr(data_type='molecule', remove_hs=False)

smiles_list = [
    "CCO",
    "c1ccccc1",
    "COc1ccc(N=Nc2ccccc2)cc1"
]

unimol_repr = clf.get_repr(smiles_list, return_atomic_reprs=True)

print(unimol_repr.keys())
print("CLS repr shape:", np.array(unimol_repr["cls_repr"]).shape)
print("Number of atomic reprs:", len(unimol_repr["atomic_reprs"]))