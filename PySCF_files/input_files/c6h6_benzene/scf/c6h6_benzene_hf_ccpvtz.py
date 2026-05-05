from pyscf import gto, scf

mol_c6h6 = gto.M(
        atom = '''
        C1   0.000  1.383 0.000;
        C2   1.197  0.691 0.000;
        C3   1.197 -0.691 0.000;
        C4   0.000 -1.383 0.000;
        C5  -1.197 -0.691 0.000;
        C6  -1.197  0.691 0.000;
        H7   0.000  2.456 0.000;
        H8   2.127  1.228 0.000;
        H9   2.127 -1.228 0.000;
        H10  0.000 -2.456 0.000;
        H11 -2.127 -1.228 0.000;
        H12 -2.127  1.228 0.000
        ''',
        basis = 'ccpvtz')

rhf_c6h6_benzene_ccpvtz = scf.RHF(mol_c6h6)
rhf_c6h6_benzene_ccpvtz.verbose = 5
e_c6h6_benzene_ccpvtz = rhf_c6h6_benzene_ccpvtz.kernel()

