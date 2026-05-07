from pyscf import dft, gto

mol_h2o = gto.M(
        atom = '''
        O  0.000  0.000  0.118
        H  0.000  0.760 -0.471
        H  0.000 -0.760 -0.471
        ''',
        basis = 'cc-pVTZ')

rks_h2o_ccpvtz = dft.RKS(mol_h2o)
rks_h2o_ccpvtz.xc = 'b3lyp'
rks_h2o_ccpvtz.verbose = 5
e_h2o_ccpvtz = rks_h2o_ccpvtz.kernel()

