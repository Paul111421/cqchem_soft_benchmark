from pyscf import dft, gto

mol_h2o = gto.M(
        atom = '''
        O  0.000  0.000  0.123
        H  0.000  0.785 -0.491
        H  0.000 -0.785 -0.491
        ''',
        basis = '3-21g')

rks_h2o_321g = dft.RKS(mol_h2o)
rks_h2o_321g.xc = 'b3lyp'
rks_h2o_321g.verbose = 5
e_h2o_321g = rks_h2o_321g.kernel()

