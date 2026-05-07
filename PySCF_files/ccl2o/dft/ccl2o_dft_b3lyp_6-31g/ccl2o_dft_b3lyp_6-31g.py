from pyscf import dft, gto

mol_ccl2o = gto.M(
        atom = '''
        O1   0.000  0.000  1.726
        C2   0.000  0.000  0.531
        Cl3  0.000  1.511 -0.500
        Cl4  0.000 -1.511 -0.500
        ''',
        basis = '6-31g')

rks_ccl2o_631g = dft.RKS(mol_ccl2o)
rks_ccl2o_631g.xc = 'b3lyp'
rks_ccl2o_631g.verbose = 5
e_ccl2o_631g = rks_ccl2o_631g.kernel()

