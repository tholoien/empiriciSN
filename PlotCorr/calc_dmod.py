import numpy as np
from math import *
import sys


h_0=69.3
redshift=-99
omega_m=0.286
omega_l=0.714
omega_r=8.66e-5
output=False
outfname=''

omega_k=1-omega_m-omega_l-omega_r

yr=3.156e7 		# number of seconds in year
c=2.997e10 		# speed of light in cm/s

h_0_s=h_0/3.086E19 		# Hubble constant in 1/s
t_h=1/(h_0_s*yr*10**9) 	# Hubble time in Gyr
d_h=c/h_0_s/3.086E24 	# Hubble distance in Mpc

tol=1e-7 # tolerance for integrals
stepmax=50000 # max number of steps for integrals

wise_off=-0.647
wise_err=0.045

def integrand(x):
	return 1/sqrt((omega_r/x**2)+(omega_m/x)+(omega_l*x**2)+omega_k)
	
def integrand_z(z):
	return 1/sqrt((omega_r*(1+z)**4)+(omega_m*(1+z)**3)+(omega_l)+(omega_k*(1+z)**2))

def midpt(llim,ulim,tolerance,nstep,nstepmax,integr,oldint=0.0):
    
    hstep=(ulim-llim)/nstep

    y=llim+hstep/2.0                                # evaluate for minimum nstep
    integral=hstep*integr(y)
    for i in xrange(nstep-1):
        y+=hstep
        integral+=integr(y)*hstep
    
    if (np.fabs(oldint/integral-1.0) < tolerance):
    	return [integral,nstep]
    
    elif (2*nstep>=nstepmax):
    	print "Midpt: Warning, fractional convergence is only ", np.fabs(oldint/integral-1.0)
    	return [integral,nstep]
    	
    else:
		return midpt(llim,ulim,tolerance,2*nstep,nstepmax,integr,integral)

'''
Function definition for calculating and outputting all the desired quantities given the cosmological parameters input.
Uses numerical integration to get ages and comoving distance.
Other quantities are calculated using equations in Hogg (1999).
'''
def calc_lumd(redshift):
	
	a_z=1/(1+redshift) 		# Scale factor at redshift z
	
	d_c=midpt(0.0,redshift,tol,4,stepmax,integrand_z)[0]*d_h # Comoving radial distance
	
	d_m=d_c			# Comoving transverse distance
	if omega_k>0:
		d_m=d_h*1/sqrt(omega_k)*sinh(sqrt(omega_k)*d_c/d_h)
	elif omega_k<0:
		d_m=d_h*1/sqrt(-1.0*omega_k)*sin(sqrt(-1.0*omega_k)*d_c/d_h)
	
	return d_m*(1+redshift)	# Luminosity distance
		
		
		
		
