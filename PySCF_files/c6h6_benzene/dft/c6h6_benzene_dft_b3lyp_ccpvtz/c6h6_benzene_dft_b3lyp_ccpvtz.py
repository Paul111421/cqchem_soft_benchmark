from pyscf import dft, gto

mol_c6h6 = gto.M(
        atom = '''
        C1   0.000  1.391  0.000
        C2   1.204  0.695  0.000
        C3   1.204 -0.695  0.000
        C4   0.000 -1.391  0.000
        C5  -1.204 -0.695  0.000
        C6  -1.204  0.695  0.000

        H7   0.000  2.473  0.000
        H8   2.142  1.236  0.000
        H9   2.142 -1.236  0.000
        H10  0.000 -2.473  0.000
        H11 -2.142 -1.236  0.000
        H12 -2.142  1.236  0.000
        ''',
        basis = 'cc-pVTZ')

rks_c6h6_ccpvtz = dft.RKS(mol_c6h6)
rks_c6h6_ccpvtz.xc = 'b3lyp'
rks_c6h6_ccpvtz.verbose = 5
e_c6h6_ccpvtz = rks_c6h6_ccpvtz.kernel()

