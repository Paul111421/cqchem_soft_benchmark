from pyscf import gto, scf

mol_c6h6 = gto.M(
        atom = '''
        C1   0.000  1.388 0.000;
        C2   1.202  0.694 0.000;
        C3   1.202 -0.694 0.000;
        C4   0.000 -1.388 0.000;
        C5  -1.202 -0.694 0.000;
        C6  -1.202  0.694 0.000;
        H7   0.000  2.462 0.000;
        H8   2.132  1.231 0.000;
        H9   2.132 -1.231 0.000;
        H10  0.000 -2.462 0.000;
        H11 -2.132 -1.231 0.000;
        H12 -2.132  1.231 0.000
        ''',
        basis = '6-31g')

rhf_c6h6_benzene_631g = scf.RHF(mol_c6h6)
rhf_c6h6_benzene_631g.verbose = 5
e_c6h6_benzene_631g = rhf_c6h6_benzene_631g.kernel()

