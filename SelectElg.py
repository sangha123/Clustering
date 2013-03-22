import numpy,scipy,pylab

if __name__=="__main__":

    objid,type,ra1,dec1,z1,z1min,z1max,u,g,r,i,z,u_err,g_err,r_err,i_err,z_err=numpy.loadtxt('s82_combined_catalog.dat',unpack=True,skiprows=1)
    
    colorgr=g-r
    colorri=r-i

    idgri=numpy.where((colorgr<2) & (colorgr>0) & (colorri<2) & (colorri>0) & (type==3))
    colorgr=colorgr[idgri]
    colorri=colorri[idgri]
    x0=[0,2]
    y0=[1.1,1.1]
    y1=[0.45,0.45]
    x2=[0.85,0.85]
    y2=[0,2]
    pylab.hexbin(colorri,colorgr,gridsize=300)
    pylab.plot(x0,y0,'r')
    pylab.plot(x0,y1,'r')
    pylab.plot(x2,y2,'r')
    pylab.xlim(0,1)
    pylab.ylim(0,2)
    pylab.xlabel('r-i')
    pylab.ylabel('g-r')
    filesave="ELG_color.png"
    pylab.savefig(filesave)
    pylab.close()

    ra1=ra1[idgri]
    dec1=dec1[idgri]
    u=u[idgri]
    g=g[idgri]
    r=r[idgri]
    i=i[idgri]
    z=z[idgri]
    type=type[idgri]
    
    
    id0=numpy.where((colorgr<1.1) & (colorgr>0.45) & (colorri<0.8))
    print "No of ELG's= ",id0[0].shape

    u=u[id0]
    g=g[id0]
    r=r[id0]
    i=i[id0]
    z=z[id0]
    ra1=ra1[id0]
    dec1=dec1[id0]
    type=type[id0]

    numbin=24
    n0=numpy.zeros(numbin-1,dtype='double')
    mag0=14
    magrange=numpy.arange(numbin)*0.5+mag0

    for i0 in xrange(numbin-1):
        id=numpy.where((i>magrange[i0])&(i<magrange[i0+1]))
        n0[i0]=id[0].shape[0]
        
    area=(max(ra1)-min(ra1))*(max(dec1)-min(dec1)) #in sq degrees
    area=275
    
    n0=n0/area
    pylab.plot(magrange[0:numbin-1],n0)

    #pylab.savefig('magdist_i.png')
    
    for i0 in xrange(numbin-1):
        id=numpy.where((g>magrange[i0])&(g<magrange[i0+1]))
        n0[i0]=id[0].shape[0]
        print n0[i0]
    n0=n0/area
    pylab.plot(magrange[0:numbin-1],n0)

    

    for i0 in xrange(numbin-1):
        id=numpy.where((r>magrange[i0])&(r<magrange[i0+1]))
        n0[i0]=id[0].shape[0]
        print n0[i0]
    n0=n0/area
    pylab.plot(magrange[0:numbin-1],n0)

    for i0 in xrange(numbin-1):
        id=numpy.where((u>magrange[i0])&(u<magrange[i0+1]))
        n0[i0]=id[0].shape[0]
        print n0[i0]
    n0=n0/area
    pylab.plot(magrange[0:numbin-1],n0)

    for i0 in xrange(numbin-1):
        id=numpy.where((z>magrange[i0])&(z<magrange[i0+1]))
        n0[i0]=id[0].shape[0]
        print n0[i0]
    n0=n0/area
    pylab.plot(magrange[0:numbin-1],n0)
    pylab.legend(('i','g','r','u','z'),loc=0)
    pylab.xlabel('Magnitude')
    pylab.ylabel('#/sq degree/half mag')
    pylab.savefig('magdist.png')
    
    pylab.close()
