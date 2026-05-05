from pyscf import gto, scf

mol_ch3cooh = gto.M(
        atom = '''
        C1  1.101 -0.852  0.000;
        C2  0.000  0.150  0.000;
        O3  0.127  1.354  0.000;
        H4  2.053 -0.347  0.000;
        H5  1.020 -1.487  0.873;
        H6  1.020 -1.487 -0.873;
        O7 -1.222 -0.436  0.000;
        H8 -1.947  0.185  0.000;
        ''',
        basis = '6-31g')

rhf_ch3cooh_631g = scf.RHF(mol_ch3cooh)
rhf_ch3cooh_631g.verbose = 5
e_ch3cooh_631g = rhf_ch3cooh_631g.kernel()

