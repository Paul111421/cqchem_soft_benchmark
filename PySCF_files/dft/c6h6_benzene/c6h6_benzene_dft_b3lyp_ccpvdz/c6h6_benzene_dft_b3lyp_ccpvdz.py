from pyscf import dft, gto

mol_c6h6 = gto.M(
        atom = '''
        C1   0.000  1.399  0.000
        C2   1.211  0.699  0.000
        C3   1.211 -0.699  0.000
        C4   0.000 -1.399  0.000
        C5  -1.211 -0.699  0.000
        C6  -1.211  0.699  0.000

        H7   0.000  2.491  0.000
        H8   2.158  1.246  0.000
        H9   2.158 -1.246  0.000
        H10  0.000 -2.491  0.000
        H11 -2.158 -1.246  0.000
        H12 -2.158  1.246  0.000
        ''',
        basis = 'cc-pVDZ')

rks_c6h6_ccpvdz = dft.RKS(mol_c6h6)
rks_c6h6_ccpvdz.xc = 'b3lyp'
rks_c6h6_ccpvdz.verbose = 5
e_c6h6_ccpvdz = rks_c6h6_ccpvdz.kernel()

