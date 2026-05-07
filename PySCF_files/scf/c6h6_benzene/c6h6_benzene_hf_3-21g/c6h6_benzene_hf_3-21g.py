from pyscf import gto, scf

mol_c6h6 = gto.M(
        atom = '''
        C1   0.000  1.385 0.000;
        C2   1.199  0.692 0.000;
        C3   1.199 -0.692 0.000;
        C4   0.000 -1.385 0.000;
        C5  -1.199 -0.692 0.000;
        C6  -1.199  0.692 0.000;
        H7   0.000  2.457 0.000;
        H8   2.128  1.228 0.000;
        H9   2.128 -1.228 0.000;
        H10  0.000 -2.457 0.000;
        H11 -2.128 -1.228 0.000;
        H12 -2.128  1.228 0.000
        ''',
        basis = '3-21g')

rhf_c6h6_benzene_321g = scf.RHF(mol_c6h6)
rhf_c6h6_benzene_321g.verbose = 5
e_c6h6_benzene_321g = rhf_c6h6_benzene_321g.kernel()

