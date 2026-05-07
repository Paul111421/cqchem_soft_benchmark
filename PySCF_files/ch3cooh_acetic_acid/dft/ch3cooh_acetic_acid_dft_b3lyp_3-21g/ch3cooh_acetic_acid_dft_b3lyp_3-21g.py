from pyscf import dft, gto

mol_ch3cooh = gto.M(
        atom = '''
        C1  1.144 -0.816  0.000;
        C2  0.000  0.168  0.000;
        O3  0.057  1.390  0.000;
        H4  2.090 -0.276  0.000;
        H5  1.074 -1.459  0.883;
        H6  1.074 -1.459 -0.883;
        O7 -1.202 -0.522  0.000;
        H8 -1.942  0.147  0.000;
        ''',
        basis = '3-21g')

rks_ch3cooh_321g = dft.RKS(mol_ch3cooh)
rks_ch3cooh_321g.xc = "b3lyp"
rks_ch3cooh_321g.verbose = 5
e_ch3cooh_321g = rks_ch3cooh_321g.kernel()

