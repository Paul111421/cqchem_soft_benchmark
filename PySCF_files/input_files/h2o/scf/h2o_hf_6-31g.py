from pyscf import gto, scf 

mol_h2o = gto.M(atom = 'O 0 0 0.107; H 0 0.785 -0.427; H 0 -0.785 -0.427', basis = '6-31g')

rhf_h2o_631g = scf.RHF(mol_h2o)
rhf_h2o_631g.verbose = 5 
e_h2o_631g = rhf_h2o_631g.kernel()


