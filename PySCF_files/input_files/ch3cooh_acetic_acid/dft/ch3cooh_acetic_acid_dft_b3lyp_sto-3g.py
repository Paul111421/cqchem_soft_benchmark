from pyscf import dft, gto

mol_ch3cooh = gto.M(
        atom = '''
        C1  1.159 -0.872  0.000;
        C2  0.000  0.170  0.000;
        O3  0.087  1.418  0.000;
        H4  2.125 -0.347  0.000;
        H5  1.092 -1.513  0.893;
        H6  1.092 -1.513 -0.893;
        O7 -1.256 -0.505  0.000;
        H8 -1.918  0.283  0.000;
        ''',
        basis = 'sto-3g')

rks_ch3cooh_sto3g = dft.RKS(mol_ch3cooh)
rks_ch3cooh_sto3g.xc = "b3lyp"
rks_ch3cooh_sto3g.verbose = 5
e_ch3cooh_sto3g = rks_ch3cooh_sto3g.kernel()

