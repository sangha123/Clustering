import numpy,subprocess,pyfits,pylab,sys,time

if __name__=="__main__":
    
    filename="stripe_82_kevinbundy/S82coadd_RA316_360_new.fits"
    filenamebpz1="stripe_82_kevinbundy/bpz_S82coadd_RA316_340.fits"
    filenamebpz2="stripe_82_kevinbundy/bpz_S82coadd_RA340_360.fits"

    catalog_s82=pyfits.open(filename)
    table=catalog_s82[1].data
    objid_s82=table.field("OBJID")
    u=table.field('U')
    g=table.field('G')
    r=table.field('R')
    i=table.field('I')
    z=table.field('Z')
    TYPE=table.field('TYPE')
    ra=table.field('RA')
    dec=table.field('DEC')
   
    filesave='cc_bundy.png'
    
    #make the cut for blue galaxies

    colorgr=g-r
    colorri=r-i
    idgri=numpy.where((colorgr<2) & (colorgr>-1) & (colorri<2) & (colorri>-1) & (TYPE==3))
    print idgri[0].shape
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
    
    pylab.savefig(filesave)

    u_err=table.field('ERR_U')
    g_err=table.field('ERR_G')
    r_err=table.field('ERR_R')
    i_err=table.field('ERR_I')
    z_err=table.field('ERR_Z')
    
    filenew="s82coadd_mag_bpz_kevin.fits"

    print u.shape
    
    zcat1=pyfits.open(filenamebpz1)
    zcat2=pyfits.open(filenamebpz2)

    zcat1[1].columns.names[8]='XXX'
    zcat2[1].columns.names[8]='XXX'

    zcat1data=zcat1[1].data
    zcat2data=zcat2[1].data

    objid_z1=zcat1data.field('OBJID')
    objid_z2=zcat2data.field('OBJID')

    z1=zcat1data.field('Z')
    z1min=zcat1data.field('Z_MIN')
    z1max=zcat1data.field('Z_MAX')
    ra1=zcat1data.field('RA')
    dec1=zcat1data.field('DEC')

    n0=objid_z1.shape[0]
    n1=objid_z2.shape[0]
      
    id_objid_z1=numpy.argsort(objid_z1)
    objid_z1_s=objid_z1[id_objid_z1]
    z1_s=z1[id_objid_z1]
    z1min_s=z1min[id_objid_z1]
    z1max_s=z1max[id_objid_z1]
    ra1_s=ra1[id_objid_z1]
    dec1_s=dec1[id_objid_z1]
    

    id_objid_s82=numpy.argsort(objid_s82)
    objid_s82_s=objid_s82[id_objid_s82]
    ra_s=ra[id_objid_s82]
    dec_s=dec[id_objid_s82]
    u_s=u[id_objid_s82]
    g_s=g[id_objid_s82]
    r_s=r[id_objid_s82]
    i_s=i[id_objid_s82]
    z_s=z[id_objid_s82]

    u_err_s=u_err[id_objid_s82]
    g_err_s=g_err[id_objid_s82]
    r_err_s=r_err[id_objid_s82]
    i_err_s=i_err[id_objid_s82]
    z_err_s=z_err[id_objid_s82]

    ns82=ra.shape[0]
    nz1=objid_z1.shape[0]
   
    count=0
    f=open('s82_combined_catalog.dat',mode='w')
    for i in xrange(ns82):
        if ((objid_s82_s[i]==objid_z1_s[count]) & (count<nz1)):
            f.write('%d %d %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f \n'%(objid_z1_s[count],TYPE[i],ra1_s[count],dec1_s[count],z1_s[count],z1min[count],z1max[count],u_s[i],g_s[i],r_s[i],i_s[i],z_s[i],u_err_s[i],g_err_s[i],r_err_s[i],i_err_s[i],z_err_s[i]))
            count=count+1
    f.close()

    

    '''
    ra_new=numpy.array([])
    dec_new=numpy.array([])
    Zred_new=numpy.array([])
    zmin_new=numpy.array([])
    zmax_new=numpy.array([])
    u_new=numpy.array([])
    g_new=numpy.array([])
    r_new=numpy.array([])
    i_new=numpy.array([])
    z_new=numpy.array([])

    u_err_new=numpy.array([])
    g_err_new=numpy.array([])
    r_err_new=numpy.array([])
    i_err_new=numpy.array([])
    z_err_new=numpy.array([])

    objid_new=numpy.array([])
    
    for i0 in xrange(100):
        idx=numpy.where(objid_z1[i0]==objid_s82)
        Zred_new=numpy.append(Zred_new,z1[i0])
        zmin_new=numpy.append(zmin_new,z1min[i0])
        zmax_new=numpy.append(zmax_new,z1max[i0])
        ra_new=numpy.append(ra_new,ra1[i0])
        dec_new=numpy.append(dec_new,dec1[i0])
        objid_new=numpy.append(objid_new,objid_z1[i0])
        u_new=numpy.append(u_new,u[idx])
        g_new=numpy.append(g_new,g[idx])
        r_new=numpy.append(r_new,r[idx])
        i_new=numpy.append(i_new,i[idx])
        z_new=numpy.append(z_new,z[idx])

        u_err_new=numpy.append(u_err_new,u_err[idx])
        g_err_new=numpy.append(g_err_new,g_err[idx])
        r_err_new=numpy.append(r_err_new,r_err[idx])
        i_err_new=numpy.append(i_err_new,i_err[idx])
        z_err_new=numpy.append(z_err_new,z_err[idx])
        
    
    header0=catalog_s82[0].header
    col1=pyfits.Column(name='OBJID',format='J',array=objid_new)
    col2=pyfits.Column(name='RA',format='D',array=ra_new)
    col3=pyfits.Column(name='DEC',format='D',array=dec_new)
    col4=pyfits.Column(name='U',format='D',array=u_new)
    col5=pyfits.Column(name='G',format='D',array=g_new)
    col6=pyfits.Column(name='R',format='D',array=r_new)
    col7=pyfits.Column(name='I',format='D',array=i_new)
    col8=pyfits.Column(name='Z',format='D',array=z_new)

    col9=pyfits.Column(name='err_U',format='D',array=u_err_new)
    col10=pyfits.Column(name='err_G',format='D',array=g_err_new)
    col11=pyfits.Column(name='err_R',format='D',array=r_err_new)
    col12=pyfits.Column(name='err_I',format='D',array=i_err_new)
    col13=pyfits.Column(name='err_Z',format='D',array=z_err_new)

    col14=pyfits.Column(name='Z_rs',format='D',array=Zred_new)
    col15=pyfits.Column(name='Z_min',format='E',array=zmin_new)
    col16=pyfits.Column(name='Z_max',format='E',array=zmax_new)

    n = numpy.arange(100)
    hdu = pyfits.PrimaryHDU(n)
    cols=pyfits.ColDefs([col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16])
    tbhdu=pyfits.new_table(cols)
    thdulist = pyfits.HDUList([hdu, tbhdu])


    thdulist.writeto(filenew,clobber=True)
    '''
