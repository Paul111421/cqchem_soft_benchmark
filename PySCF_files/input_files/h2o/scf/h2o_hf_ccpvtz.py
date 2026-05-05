from pyscf import gto, scf 

mol_h2o = gto.M(atom = 'O 0 0 0.113; H 0 0.751 -0.453; H 0 -0.751 -0.453', basis = 'ccpvtz')

rhf_h2o_ccpvtz = scf.RHF(mol_h2o)
rhf_h2o_ccpvtz.verbose = 5 
e_h2o_ccpvtz = rhf_h2o_ccpvtz.kernel()


