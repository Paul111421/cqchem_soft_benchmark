from pyscf import dft, gto

mol_h2o = gto.M(
        atom = '''
        O  0.000  0.000  0.114
        H  0.000  0.791 -0.457
        H  0.000 -0.791 -0.457
        ''',
        basis = '6-31g')

rks_h2o_631g = dft.RKS(mol_h2o)
rks_h2o_631g.xc = 'b3lyp'
rks_h2o_631g.verbose = 5
e_h2o_631g = rks_h2o_631g.kernel()

