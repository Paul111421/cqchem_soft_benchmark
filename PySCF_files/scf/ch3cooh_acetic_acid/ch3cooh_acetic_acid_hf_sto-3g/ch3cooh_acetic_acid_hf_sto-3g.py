from pyscf import gto, scf

mol_ch3cooh = gto.M(
        atom = '''
        C1  1.118 -0.893  0.000;
        C2  0.000  0.162  0.000;
        O3  0.138  1.370  0.000;
        H4  2.085 -0.401  0.000;
        H5  1.031 -1.522  0.881;
        H6  1.031 -1.522 -0.881;
        O7 -1.258 -0.433  0.000;
        H8 -1.893  0.327  0.000;
        ''',
        basis = 'sto-3g')

rhf_ch3cooh_sto3g = scf.RHF(mol_ch3cooh)
rhf_ch3cooh_sto3g.verbose = 5
e_ch3cooh_sto3g = rhf_ch3cooh_sto3g.kernel()

