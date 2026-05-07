from pyscf import dft, gto

mol_ccl2o = gto.M(
        atom = '''
        O1   0.000  0.000  1.766
        C2   0.000  0.000  0.540
        Cl3  0.000  1.516 -0.511
        Cl4  0.000 -1.516 -0.511
        ''',
        basis = 'sto-3g')

rks_ccl2o_sto3g = dft.RKS(mol_ccl2o)
rks_ccl2o_sto3g.xc = 'b3lyp'
rks_ccl2o_sto3g.verbose = 5
e_ccl2o_sto3g = rks_ccl2o_sto3g.kernel()

