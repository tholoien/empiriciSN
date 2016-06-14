# empiriciSN
empiriciSN is a software module for generating realistic supernova parameters given photometric observations of a potential host galaxy, based entirely on empirical correlations measured from supernova datasets. This code is intended to be used to improve supernova simulation for LSST. It is intended to be extendable such that additional datasets may be added in the future to improve the fitting algorithm or so that additional light curve parameters or supernova types may be fit.

# SN Parameters
The code currently supports the generation of SALT2 parameters (stretch, color, and magnitude) for Type Ia supernovae.

# SN Datasets
The software has been trained using the following datasets:
- SNLS ([REF], number of SNe) [in progress]
- SDSS ([Sako et al. (2104)] (http://arxiv.org/abs/1401.3317), number of SNe) [in progress]
- DES (number of SNe) [in progress]