from pyscf import dft, gto

mol_h2o = gto.M(
        atom = '''
        O  0.000  0.000  0.121
        H  0.000  0.756 -0.484
        H  0.000 -0.756 -0.484
        ''',
        basis = 'cc-pVDZ')

rks_h2o_ccpvdz = dft.RKS(mol_h2o)
rks_h2o_ccpvdz.xc = 'b3lyp'
rks_h2o_ccpvdz.verbose = 5
e_h2o_ccpvdz = rks_h2o_ccpvdz.kernel()

