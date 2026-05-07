from pyscf import gto, scf

mol_c6h6 = gto.M(
        atom = '''
        C1   0.000  1.387 0.000;
        C2   1.201  0.693 0.000;
        C3   1.201 -0.693 0.000;
        C4   0.000 -1.387 0.000;
        C5  -1.201 -0.693 0.000;
        C6  -1.201  0.693 0.000;
        H7   0.000  2.469 0.000;
        H8   2.139  1.235 0.000;
        H9   2.139 -1.235 0.000;
        H10  0.000 -2.469 0.000;
        H11 -2.139 -1.235 0.000;
        H12 -2.139  1.235 0.000
        ''',
        basis = 'sto-3g')

rhf_c6h6_benzene_sto3g = scf.RHF(mol_c6h6)
rhf_c6h6_benzene_sto3g.verbose = 5
e_c6h6_benzene_sto3g = rhf_c6h6_benzene_sto3g.kernel()

