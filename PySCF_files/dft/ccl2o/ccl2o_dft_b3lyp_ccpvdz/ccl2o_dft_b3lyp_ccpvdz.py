from pyscf import dft, gto

mol_ccl2o = gto.M(
        atom = '''
        O1   0.000  0.000  1.687
        C2   0.000  0.000  0.508
        Cl3  0.000  1.464 -0.487
        Cl4  0.000 -1.464 -0.487
        ''',
        basis = 'cc-pVDZ')

rks_ccl2o_ccpvdz = dft.RKS(mol_ccl2o)
rks_ccl2o_ccpvdz.xc = 'b3lyp'
rks_ccl2o_ccpvdz.verbose = 5
e_ccl2o_ccpvdz = rks_ccl2o_ccpvdz.kernel()

