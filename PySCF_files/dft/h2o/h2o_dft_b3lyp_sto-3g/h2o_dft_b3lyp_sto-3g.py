from pyscf import dft, gto

mol_h2o = gto.M(
        atom = '''
        O  0.000  0.000  0.136
        H  0.000  0.771 -0.543
        H  0.000 -0.771 -0.543
        ''',
        basis = 'sto-3g')

rks_h2o_sto3g = dft.RKS(mol_h2o)
rks_h2o_sto3g.xc = 'b3lyp'
rks_h2o_sto3g.verbose = 5
e_h2o_sto3g = rks_h2o_sto3g.kernel()

