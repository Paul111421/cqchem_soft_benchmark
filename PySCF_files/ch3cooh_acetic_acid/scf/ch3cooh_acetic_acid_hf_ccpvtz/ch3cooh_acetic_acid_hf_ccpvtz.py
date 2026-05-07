from pyscf import gto, scf

mol_ch3cooh = gto.M(
        atom = '''
        C1  1.021 -0.943  0.000;
        C2  0.000  0.155  0.000;
        O3  0.235  1.314  0.000;
        H4  2.011 -0.517  0.000;
        H5  0.881 -1.566  0.880;
        H6  0.881 -1.566 -0.880;
        O7 -1.242 -0.318  0.000;
        H8 -1.842  0.413  0.000;
        ''',
        basis = 'ccpvtz')

rhf_ch3cooh_ccpvtz = scf.RHF(mol_ch3cooh)
rhf_ch3cooh_ccpvtz.verbose = 5
e_ch3cooh_ccpvtz = rhf_ch3cooh_ccpvtz.kernel()

