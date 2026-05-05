from pyscf import gto, scf

mol_h2o = gto.M(atom = 'O 0 0 0.116; H 0 0.749 -0.463; H 0 -0.749 -0.463', basis = 'ccpvdz')

rhf_h2o_ccpvdz = scf.RHF(mol_h2o)
rhf_h2o_ccpvdz.verbose = 5
e_h2o_ccpvdz = rhf_h2o_ccpvdz.kernel()

