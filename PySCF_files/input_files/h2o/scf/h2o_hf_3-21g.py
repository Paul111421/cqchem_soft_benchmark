from pyscf import gto, scf 

mol_h2o = gto.M(atom = 'O 0 0 0.114; H 0 0.780 -0.456; H 0 -0.780 -0.456', basis = '3-21g')

rhf_h2o_321g = scf.RHF(mol_h2o)
rhf_h2o_321g.verbose = 5 
e_h2o_321g = rhf_h2o_321g.kernel()


