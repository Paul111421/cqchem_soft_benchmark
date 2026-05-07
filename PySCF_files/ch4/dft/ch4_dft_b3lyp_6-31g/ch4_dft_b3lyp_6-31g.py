from pyscf import dft, gto

mol_ch4 = gto.M(
        atom = '''
        C1  0.000  0.000  0.000
        H2  0.631  0.631  0.631
        H3 -0.631 -0.631  0.631
        H4 -0.631  0.631 -0.631
        H5  0.631 -0.631 -0.631         
        ''',
        basis = '6-31g')

rks_ch4_631g = dft.RKS(mol_ch4)
rks_ch4_631g.xc = 'b3lyp'
rks_ch4_631g.verbose = 5
e_ch4_631g = rks_ch4_631g.kernel()

