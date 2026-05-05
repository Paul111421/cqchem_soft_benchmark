from pyscf import gto, scf

mol_ch4 = gto.M(
        atom = '''
        C 0.000 0.000 0.000;
        H 0.630 0.630 0.630; 
        H -0.630 -0.630 0.630;
        H -0.630 0.630 -0.630;
        H 0.630 -0.630 -0.630;
        ''',
        basis = 'ccpvdz')

rhf_ch4_ccpvdz = scf.RHF(mol_ch4)
rhf_ch4_ccpvdz.verbose = 5
e_ch4_ccpvdz = rhf_ch4_ccpvdz.kernel()


