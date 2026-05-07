from pyscf import dft, gto

mol_ch4 = gto.M(
        atom = '''
        C1  0.000  0.000  0.000
        H2  0.633  0.633  0.633
        H3 -0.633 -0.633  0.633
        H4 -0.633  0.633 -0.633
        H5  0.633 -0.633 -0.633         
        ''',
        basis = 'sto-3g')

rks_ch4_sto3g = dft.RKS(mol_ch4)
rks_ch4_sto3g.xc = 'b3lyp'
rks_ch4_sto3g.verbose = 5
e_ch4_sto3g = rks_ch4_sto3g.kernel()

