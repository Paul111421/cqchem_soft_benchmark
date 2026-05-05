from pyscf import dft, gto

mol_ch3cooh = gto.M(
        atom = '''
        C1  1.060 -0.916  0.000;
        C2  0.000  0.156  0.000;
        O3  0.192  1.350  0.000;
        H4  2.053 -0.451  0.000;
        H5  0.941 -1.558  0.886;
        H6  0.941 -1.558 -0.886;
        O7 -1.247 -0.381  0.000;
        H8 -1.859  0.378  0.000;
        ''',
        basis = 'ccpvdz')

rks_ch3cooh_ccpvdz = dft.RKS(mol_ch3cooh)
rks_ch3cooh_ccpvdz.xc = "b3lyp"
rks_ch3cooh_ccpvdz.verbose = 5
e_ch3cooh_ccpvdz = rks_ch3cooh_ccpvdz.kernel()

