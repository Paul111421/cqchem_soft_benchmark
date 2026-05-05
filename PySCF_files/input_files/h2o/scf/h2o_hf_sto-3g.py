from pyscf import gto, scf
 
mol_h2o = gto.M(atom = 'O 0 0 0.127; H 0 0.758 -0.509; H 0 -0.758 -0.509', basis = 'sto3g')
 
rhf_h2o_sto3g = scf.RHF(mol_h2o)
rhf_h2o_sto3g.verbose = 5
e_h2o_sto3g = rhf_h2o_sto3g.kernel()


