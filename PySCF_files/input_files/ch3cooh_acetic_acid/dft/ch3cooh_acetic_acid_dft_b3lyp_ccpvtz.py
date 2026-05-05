from pyscf import dft, gto

mol_ch3cooh = gto.M(
        atom = '''
        C1  1.064 -0.905  0.000;
        C2  0.000  0.156  0.000;
        O3  0.185  1.345  0.000;
        H4  2.044 -0.438  0.000;
        H5  0.953 -1.542  0.878;
        H6  0.953 -1.542 -0.878;
        O7 -1.243 -0.386  0.000;
        H8 -1.869  0.352  0.000;
        ''',
        basis = 'ccpvtz')

rks_ch3cooh_ccpvtz = dft.RKS(mol_ch3cooh)
rks_ch3cooh_ccpvtz.xc = "b3lyp"
rks_ch3cooh_ccpvtz.verbose = 5
e_ch3cooh_ccpvtz = rks_ch3cooh_ccpvtz.kernel()

