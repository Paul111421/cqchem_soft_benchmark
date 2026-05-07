from pyscf import gto, scf

mol_ccl2o = gto.M(
        atom = '''
        O1   0.000  0.000  1.680;
        C2   0.000  0.000  0.505;
        Cl3  0.000  1.496 -0.484;
        Cl4  0.000 -1.496 -0.484;
        ''',
        basis = '6-31g')

rhf_ccl2o_631g = scf.RHF(mol_ccl2o)
rhf_ccl2o_631g.verbose = 5
e_ccl2o_631g = rhf_ccl2o_631g.kernel()

