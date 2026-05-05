from pyscf import gto, scf

mol_ccl2o = gto.M(
        atom = '''
        O1   0.000  0.000  1.648;
        C2   0.000  0.000  0.492;
        Cl3  0.000  1.448 -0.475;
        Cl4  0.000 -1.448 -0.475;
        ''',
        basis = 'ccpvdz')

rhf_ccl2o_ccpvdz = scf.RHF(mol_ccl2o)
rhf_ccl2o_ccpvdz.verbose = 5
e_ccl2o_ccpvdz = rhf_ccl2o_ccpvdz.kernel()

