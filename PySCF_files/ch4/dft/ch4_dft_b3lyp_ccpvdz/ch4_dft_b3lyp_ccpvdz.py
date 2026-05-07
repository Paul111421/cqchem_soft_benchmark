from pyscf import dft, gto

mol_ch4 = gto.M(
        atom = '''
        C1  0.000  0.000  0.000
        H2  0.635  0.635  0.635
        H3 -0.635 -0.635  0.635
        H4 -0.635  0.635 -0.635
        H5  0.635 -0.635 -0.635         
        ''',
        basis = 'cc-pVDZ')

rks_ch4_ccpvdz = dft.RKS(mol_ch4)
rks_ch4_ccpvdz.xc = 'b3lyp'
rks_ch4_ccpvdz.verbose = 5
e_ch4_ccpvdz = rks_ch4_ccpvdz.kernel()

