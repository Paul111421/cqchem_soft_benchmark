from pyscf import gto, scf

mol_c6h6 = gto.M(
        atom = '''
        C1   0.000  1.389 0.000;
        C2   1.203  0.694 0.000;
        C3   1.203 -0.694 0.000;
        C4   0.000 -1.389 0.000;
        C5  -1.203 -0.694 0.000;
        C6  -1.203  0.694 0.000;
        H7   0.000  2.471 0.000;
        H8   2.140  1.235 0.000;
        H9   2.140 -1.235 0.000;
        H10  0.000 -2.471 0.000;
        H11 -2.140 -1.235 0.000;
        H12 -2.140  1.235 0.000
        ''',
        basis = 'ccpvdz')

rhf_c6h6_benzene_ccpvdz = scf.RHF(mol_c6h6)
rhf_c6h6_benzene_ccpvdz.verbose = 5
e_c6h6_benzene_ccpvdz = rhf_c6h6_benzene_ccpvdz.kernel()

