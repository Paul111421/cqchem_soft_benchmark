from pyscf import dft, gto

mol_ch3cooh = gto.M(
        atom = '''
        C1  1.134 -0.828  0.000;
        C2  0.000  0.153  0.000;
        O3  0.089  1.383  0.000;
        H4  2.082 -0.291  0.000;
        H5  1.072 -1.474  0.882;
        H6  1.072 -1.474 -0.882;
        O7 -1.224 -0.492  0.000;
        H8 -1.953  0.166  0.000;
        ''',
        basis = '6-31g')

rks_ch3cooh_631g = dft.RKS(mol_ch3cooh)
rks_ch3cooh_631g.xc = "b3lyp"
rks_ch3cooh_631g.verbose = 5
e_ch3cooh_631g = rks_ch3cooh_631g.kernel()

