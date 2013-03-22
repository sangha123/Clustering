# z: zband
# Z: redshift

import numpy,subprocess,pyfits,pylab,sys,time

if __name__=="__main__":

    id,ra,dec,Z_red,zmin,zmax,u,g,r,i,z,uerr,gerr,rerr,ierr,zerr=numpy.loadtxt('s82_combined_catalog.dat', unpack=True)

    colorgr=g-r
    colorri=r-i
    idgri=numpy.where((colorgr<2) & (colorgr>-1) & (colorri<2) & (colorri>-1) & (r<24.0))

    idgri[0].shape
    id=id[idgri]
    ra=ra[idgri]
    dec=dec[idgri]
    Z_red=Z_red[idgri]
    zmin=zmin[idgri]
    zmax=zmax[idgri]
    u=u[idgri]
    g=g[idgri]
    r=r[idgri]
    i=i[idgri]
    z=z[idgri]
    uerr=uerr[idgri]
    gerr=gerr[idgri]
    rerr=rerr[idgri]
    ierr=ierr[idgri]
    zerr=zerr[idgri]

    id1=numpy.where((Z_red>0.5) & (Z_red<0.7) )

    pylab.hist(-r[id1],bins=10)
    pylab.savefig('hist_r_57.png')
    

    

    
