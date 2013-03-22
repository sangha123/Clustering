import numpy,pylab

if __name__=="__main__":
    
    low,high,DD=numpy.loadtxt('dataresult.dat',unpack=True,skiprows=1)
    low,high,DR=numpy.loadtxt('datarandomresult.dat',unpack=True,skiprows=1)
    low,high,RR=numpy.loadtxt('datarandomresult.dat',unpack=True,skiprows=1)

    bin_center = ((low[:-1]**3 + low[1:]**3)/2)**(1./3.)
    print low.shape,bin_center.shape
    print low,high,bin_center
    Nr=1.
    N=1.
    

    xi=(DD-2*DR+RR)/RR

    #pylab.loglog((low+high/2),(zi*0.5),'o')
    #pylab.loglog(bin_center,(DD[:-1]/DR[:-1]-1),'o')
    pylab.loglog(bin_center,xi[:-1],'o')
    #pylab.plot.axis((0.2,200,1e-3,100))
    #pylab.xlabel(r'$s\:(\mathrm{Mpc}/h)$')
    #pylab.ylabel(r'$\xi (s)$')

    X=numpy.loadtxt('xir.A00_0.5882.halos_1.e13.dat',skiprows=4)
    r=X[:,0]
    zi_theo=X[:,1]

    pylab.loglog(r,zi_theo)
    pylab.xlim(10,150)
    X=numpy.loadtxt('xir.A00_0.5882.halos.dat',skiprows=4)
    r=X[:,0]
    zi_theo=X[:,1]
    
    
    pylab.plot(r,zi_theo)
    pylab.xlim(10,150)
    pylab.legend(('mycode','M>1.e13','entire_sample'),loc=0)
    pylab.savefig('correlation_theo.png')
    
