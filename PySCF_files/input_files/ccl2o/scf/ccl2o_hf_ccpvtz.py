from pyscf import gto, scf

mol_ccl2o = gto.M(
        atom = '''
        O1   0.000  0.000  1.642;
        C2   0.000  0.000  0.489;
        Cl3  0.000  1.444 -0.473;
        Cl4  0.000 -1.444 -0.473;
        ''',
        basis = 'ccpvtz')

rhf_ccl2o_ccpvtz = scf.RHF(mol_ccl2o)
rhf_ccl2o_ccpvtz.verbose = 5
e_ccl2o_ccpvtz = rhf_ccl2o_ccpvtz.kernel()

