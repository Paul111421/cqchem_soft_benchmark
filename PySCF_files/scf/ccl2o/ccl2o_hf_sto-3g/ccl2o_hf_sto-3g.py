from pyscf import gto, scf

mol_ccl2o = gto.M(
        atom = '''
        O1   0.000  0.000  1.707;
        C2   0.000  0.000  0.513;
        Cl3  0.000  1.496 -0.492;
        Cl4  0.000 -1.496 -0.492;
        ''',
        basis = 'sto-3g')

rhf_ccl2o_sto3g = scf.RHF(mol_ccl2o)
rhf_ccl2o_sto3g.verbose = 5
e_ccl2o_sto3g = rhf_ccl2o_sto3g.kernel()

