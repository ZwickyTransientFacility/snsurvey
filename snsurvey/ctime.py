import numpy as np
#from astropy.io import ascii
from astropy.table import Table
#from scipy.interpolate import interp1d
import sncosmo
from astropy.cosmology import FlatLambdaCDM
#from astropy import units as u
#import astropy.constants as const

def efficiency(mag, threshold, k = 10):
    return 1/(1+np.exp(k*(mag-threshold)))

def LC_spread(phase, M, mu, sig):
    pdf = np.exp(-0.5*((M-mu)/sig)**2)/(sig*(2*np.pi)**0.5)
    return pdf

def control_time(lc_tab, threshold, time_resolution = 0.1):
    phase = lc_tab.field('phase')
    mag = lc_tab.field('mag')
    mags = np.linspace(25,15,201)
    ctime = 0
    for i in range(0,len(phase)):
        spread = LC_spread(phase[i],mags,mag[i],0.5)*efficiency(mags,threshold)
        e = np.trapz(spread,mags)*(-1)
        ctime += time_resolution*e
        #ctime.append(time_resolution*e)
        #print e,ctime
    return ctime

def total_ctime(z, obs, threshold, filters, time_resolution = 0.1):
    lc_dict = {}
    for filter in np.unique(filters):
        lc_dict[filter] = LC(z,filter) 
    lc = lc_dict[filters[0]]
    ct = control_time(lc,threshold[0])
    ctimes = [ct]
    foo = obs[0]+ct
    for i in range(1,len(obs)):
        lc = lc_dict[filters[i]]
        ct = control_time(lc,threshold[i])
        bar = obs[i]+ct-foo
        if obs[i] > foo:
            ctimes.append(ct)
            foo = obs[i]+ct
        elif bar > 0:
            ctimes.append(bar)
            foo = obs[i]+ct
        else:
            ctimes.append(0)
    return ctimes


def LC(z, obsfilter, time_resolution = 0.1, absmag_V = -19.3, magsystem = 'ab', modelphase = 0, template = 'salt2'):
    
    cosmo = FlatLambdaCDM(H0=69.6, Om0=0.286)
       #z = 0.05
       #obsfiler = = 'besselb'
    model = sncosmo.Model(source=template)
    model.set(z=0)
    magdiff = model.bandmag('bessellv','vega',[0])-absmag_V
    templatescale = 10**(0.4*magdiff)

    epochs = np.linspace(model.mintime(),model.maxtime(),(model.maxtime()-model.mintime())/time_resolution)
    
    model.set(x0=templatescale,z=z)
    absmag = model.bandmag(obsfilter,magsystem,epochs)
    DM = cosmo.distmod(z)
    obsmag = absmag+DM.value
    return Table([epochs,obsmag],names=('phase', 'mag'))
