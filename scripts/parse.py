from rdkit import Chem

from molvs import Standardizer
s = Standardizer()


suppl = Chem.SDMolSupplier('/data/nci/ncidb.sdf', sanitize=True)
i = 0
f = 0
n = 0
for mol in suppl:
    if i == 10000: break
    i += 1
    if mol:
        try:
            smol = s.standardize(mol)
            print(str(i) + ":" + str(mol.GetNumAtoms()) + ":" + Chem.MolToSmiles(smol))
            tmol = s.tautomer_parent(smol, True)
            print(str(i) + ":" + str(mol.GetNumAtoms()) + ":" + Chem.MolToSmiles(tmol))
        except Exception as e:
            print(e)
            n += 1

    else:
        f += 1

print("failed         : " + str(f))
print("not normalized : " + str(n))