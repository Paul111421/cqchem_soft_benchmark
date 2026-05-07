from pyscf import dft, gto

mol_ccl2o = gto.M(
        atom = '''
        O1   0.000  0.000  1.761
        C2   0.000  0.000  0.576
        Cl3  0.000  1.511 -0.516
        Cl4  0.000 -1.511 -0.516
        ''',
        basis = '3-21g')

rks_ccl2o_321g = dft.RKS(mol_ccl2o)
rks_ccl2o_321g.xc = 'b3lyp'
rks_ccl2o_321g.verbose = 5
e_ccl2o_321g = rks_ccl2o_321g.kernel()

