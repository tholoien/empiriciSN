# empiriciSN
empiriciSN is a software module for generating realistic supernova parameters given photometric observations of a potential host galaxy, based entirely on empirical correlations measured from supernova datasets. This code is intended to be used to improve supernova simulation for LSST. It is extendable such that additional datasets may be added in the future to improve the fitting algorithm or so that additional light curve parameters or supernova types may be fit.

# SN Parameters
The code currently supports the generation of SALT2 parameters (stretch, color, and magnitude) for Type Ia supernovae.

# Host Parameters
Currently the code is trained based on the following host galaxy parameters:
- *ugriz* magnitudes and colors
- Separation of SN from host nucleus (angular and physical)
- Sersic index

These same parameters are used to generate SN parameters for a given host. Photometry is K-corrected and corrected for Galactic extinction prior to correlations being calculated and SN properties being fit. 

# SN Datasets
The software has been trained using the following datasets:
- SNLS ([Guy et al. (2010)] (http://cdsads.u-strasbg.fr/cgi-bin/nph-bib_query?2010A%26A...523A...7G&db_key=AST&nosetcookie=1), [Sullivan et al. (2010)] (http://cdsads.u-strasbg.fr/abs/2011yCat..74060782S); 277 SNe Ia with SALT2 params, 231 with host params) [to be added]
- SDSS ([Sako et al. (2104)] (http://arxiv.org/abs/1401.3317); ~1400 SNe Ia) [to be added]
- DES (???) [to be added]