from pyscf import dft, gto

mol_ccl2o = gto.M(
        atom = '''
        O1   0.000  0.000  1.677
        C2   0.000  0.000  0.504
        Cl3  0.000  1.457 -0.483
        Cl4  0.000 -1.457 -0.483
        ''',
        basis = 'cc-pVTZ')

rks_ccl2o_ccpvtz = dft.RKS(mol_ccl2o)
rks_ccl2o_ccpvtz.xc = 'b3lyp'
rks_ccl2o_ccpvtz.verbose = 5
e_ccl2o_ccpvtz = rks_ccl2o_ccpvtz.kernel()

