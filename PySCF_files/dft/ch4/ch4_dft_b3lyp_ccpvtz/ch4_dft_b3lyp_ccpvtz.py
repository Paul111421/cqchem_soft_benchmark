from pyscf import dft, gto

mol_ch4 = gto.M(
        atom = '''
        C1  0.000  0.000  0.000
        H2  0.628  0.628  0.628
        H3 -0.628 -0.628  0.628
        H4 -0.628  0.628 -0.628
        H5  0.628 -0.628 -0.628         
        ''',
        basis = 'cc-pVTZ')

rks_ch4_ccpvtz = dft.RKS(mol_ch4)
rks_ch4_ccpvtz.xc = 'b3lyp'
rks_ch4_ccpvtz.verbose = 5
e_ch4_ccpvtz = rks_ch4_ccpvtz.kernel()

