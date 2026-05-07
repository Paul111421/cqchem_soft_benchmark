from pyscf import gto, scf

mol_ch4 = gto.M(
        atom = '''
        C 0.000 0.000 0.000;
        H 0.625 0.625 0.625; 
        H -0.625 -0.625 0.625;
        H -0.625 0.625 -0.625;
        H 0.625 -0.625 -0.625;
        ''',
        basis = '6-31g')

rhf_ch4_631g = scf.RHF(mol_ch4)
rhf_ch4_631g.verbose = 5
e_ch4_631g = rhf_ch4_631g.kernel()

