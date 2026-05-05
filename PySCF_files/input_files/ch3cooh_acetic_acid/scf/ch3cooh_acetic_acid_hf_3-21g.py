from pyscf import gto, scf

mol_ch3cooh = gto.M(
        atom = '''
        C1  1.120 -0.832  0.000;
        C2  0.000  0.163  0.000;
        O3  0.087  1.362  0.000;
        H4  2.066 -0.315  0.000;
        H5  1.037 -1.465  0.874;
        H6  1.037 -1.465 -0.874;
        O7 -1.201 -0.474  0.000;
        H8 -1.941  0.152  0.000;
        ''',
        basis = '3-21g')

rhf_ch3cooh_321g = scf.RHF(mol_ch3cooh)
rhf_ch3cooh_321g.verbose = 5
e_ch3cooh_321g = rhf_ch3cooh_321g.kernel()

