from pyscf import gto, scf

mol_ch4 = gto.M(
        atom = '''
        C 0.000 0.000 0.000;
        H 0.625 0.625 0.625; 
        H -0.625 -0.625 0.625;
        H -0.625 0.625 -0.625;
        H 0.625 -0.625 -0.625;
        ''',
        basis = '3-21g')

rhf_ch4_321g = scf.RHF(mol_ch4)
rhf_ch4_321g.verbose = 5
e_ch4_321g = rhf_ch4_321g.kernel()

