from pyscf import gto, scf

mol_ccl2o = gto.M(
        atom = '''
        O1   0.000  0.000  1.712;
        C2   0.000  0.000  0.548;
        Cl3  0.000  1.501 -0.500;
        Cl4  0.000 -1.501 -0.500;
        ''',
        basis = '3-21g')

rhf_ccl2o_321g = scf.RHF(mol_ccl2o)
rhf_ccl2o_321g.verbose = 5
e_ccl2o_321g = rhf_ccl2o_321g.kernel()

