import os
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from specutils import Spectrum1D
from astropy import units as u

print(os.getcwd())
cwd=os.getcwd()
os.chdir(cwd)

print(os.getcwd())

# READ THE TEMPLATE SPECTRUM (ASCII FILE)
w,f = np.genfromtxt('template.syn', comments='#', usecols=(0,1), dtype='float', unpack=True)


# READ THE OBJECT SPECTRUM (FITS FILE)
spec = fits.open('low_rv.fits',ignore_missing_end=True)
header = spec[0].header
spectrum_data = spec[0].data
wl = np.zeros(header['NAXIS1'])
spec[0].header['CRVAL1'] = header['CRVAL1'] + (1 - header['CRPIX1']) * header['CDELT1']
for i in np.arange(header['NAXIS1']):
        wl[i] = header['CRVAL1'] + i * header['CDELT1']

spectrum = Spectrum1D(flux=spectrum_data*u.ct, spectral_axis=wl*u.AA) 


# PLOT
for i in range(4800,5800,100):
        plt.xlim([i,i+100])
        plt.plot(spectrum.spectral_axis,spectrum.flux)
        plt.plot(w,f,c='red')
        plt.show()
