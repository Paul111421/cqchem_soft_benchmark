from pyscf import gto, scf

mol_ch3cooh = gto.M(
        atom = '''
        C1  1.025 -0.940  0.000;
        C2  0.000  0.155  0.000;
        O3  0.229  1.318  0.000;
        H4  2.021 -0.507  0.000;
        H5  0.885 -1.586  0.880;
        H6  0.885 -1.586 -0.880;
        O7 -1.242 -0.326  0.000;
        H8 -1.840  0.414  0.000;
        ''',
        basis = 'ccpvdz')

rhf_ch3cooh_ccpvdz = scf.RHF(mol_ch3cooh)
rhf_ch3cooh_ccpvdz.verbose = 5
e_ch3cooh_ccpvdz = rhf_ch3cooh_ccpvdz.kernel()

