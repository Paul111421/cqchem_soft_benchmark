from pyscf import dft, gto

mol_c6h6 = gto.M(
        atom = '''
        C1   0.000  1.409  0.000
        C2   1.220  0.705  0.000
        C3   1.220 -0.705  0.000
        C4   0.000 -1.409  0.000
        C5  -1.220 -0.705  0.000
        C6  -1.220  0.705  0.000

        H7   0.000  2.508  0.000
        H8   2.172  1.254  0.000
        H9   2.172 -1.254  0.000
        H10  0.000 -2.508  0.000
        H11 -2.172 -1.254  0.000
        H12 -2.172  1.254  0.000 
        ''',
        basis = 'sto-3g')

rks_c6h6_sto3g = dft.RKS(mol_c6h6)
rks_c6h6_sto3g.xc = 'b3lyp'
rks_c6h6_sto3g.verbose = 5
e_c6h6_sto3g = rks_c6h6_sto3g.kernel()

