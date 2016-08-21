"""
Author: Tom Holoien
License: MIT

Tool for fitting supernova parameters from observed host galaxy 
properties based on an extreme deconvolution Gaussian mixture model.
"""

import numpy as np

from xdgmm import XDGMM

class empiriciSN():
    """empiriciSN

    Class that can fit SN parameters from host galaxy properties based
        on an XDGMM model

    Parameters
    ----------
    model: string (optional)
        Name of text file containing model being used (default=None).

    Notes
    -----
    The class can be initialized with a model or one can be loaded or
        fit to data.
    """
    def __init__(self, model_file=None):
        
        self.XDGMM = XDGMM(n_components = 7)
        
        if model_file is not None:
            self.read_model(model_file)
    
    def get_SN(self, X, Xerr=None, n_SN=1):
        """Get SN parameters for host data
        
        Conditions the XDGMM model based on the data in X and returns
            SN parameters sampled from the conditioned model.

        Parameters
        ----------
        X: array_like, shape = (n_samples, n_features)
            Input data. First 3 entries (SN parameters) should be NaN.
        Xerr: array_like, shape = (n_samples, n_features), optional
            Error on input data. SN errors should be 0.0. If None,
            errors are not used for the conditioning.
        n_SN: int (optional)
            Number of SNe to sample (default = 1).
        
        Returns
        -------
        SN_data: array_like, shape = (n_SN, 3)
            Sample of SN data taken from the conditioned model.
        """
        if self.model_file is None: 
            raise StandardError("Model parameters not set.")
        
        if Xerr is None: cond_XDGMM = self.XDGMM.condition(X)
        else: cond_XDGMM = self.XDGMM.condition(X, Xerr)
        
        return cond_XDGMM.sample(n_SN)
    
    def fit_model(self, filelist, filename='empiriciSN_model.fit',
                  n_components=7, method='astroML'):
        """Fit the XD model to data
        
        The specified method and n_components Gaussian components will
            be used (the optimal number of components was determined 
            using BIC to be 6 or 7).

        Parameters
        ----------
        filelist: array_like
            Array of strings containing names of files containing data
            to fit. 
        filename: string (optional)
            Filename for model fit (default = 'empiriciSN_model.fit').
        n_components: float (optional)
            Number of Gaussian components to use (default = 7)
        method: string (optional)
            XD fitting method to use (default = 'astroML')
        """
        X, Xerr = self.get_data(filelist)
        self.XDGMM.n_components = n_components
        self.XDGMM.method = method
        self.XDGMM = self.XDGMM.fit(X, Xerr)
        self.XDGMM.save_model(filename)
        self.model_file = filename
    
    def read_model(self, filename):
        """Read the parameters of the model from a file
        
        Read the parameters of a model from a file and store it in the 
            self.XDGMM object. The model filename is stored in 
            self.model_file.
        
        Parameters
        ----------
        filename: string
            Name of the file to read from.
        """
        self.XDGMM.read_model(filename)
        self.model_file = filename
    
    def get_data(self, filelist):
        """Parse SN and host data from a list of data files
        
        Reads in each data file and returns an array of data and a 
            matrix of errors, which can be used to fit the XDGMM model.
        
        Currently reads the SALT2 SN parameters, host redshift,
            log(R/Re), host magnitudes, and host surface brightnesses
            at the location of the SN .
        
        Parameters
        ----------
        filelist: array_like
            Array of strings containing names of files containing data
            to fit.
        
        Returns
        -------
        X: array_like, shape = (n_samples, n_features)
            Output data. Contains SALT2 SN parameters, host redshift, 
            log(R/Re), host colors, and host brightnesses at the
            locations of the SN in each filter.
        Xerr: array_like, shape = (n_samples, n_features, n_features)
            Error on output data.
        """
        x0=[]
        x0_err=[]
        x1=[]
        x1_err=[]
        c=[]
        c_err=[]
        z=[]
        z_err=[]
        logr=[]
        logr_err=[]
        umag=[]
        umag_err=[]
        gmag=[]
        gmag_err=[]
        rmag=[]
        rmag_err=[]
        imag=[]
        imag_err=[]
        zmag=[]
        zmag_err=[]
        SB_u=[]
        SB_u_err=[]
        SB_g=[]
        SB_g_err=[]
        SB_r=[]
        SB_r_err=[]
        SB_i=[]
        SB_i_err=[]
        SB_z=[]
        SB_z_err=[]
        
        for filename in filelist:
            infile=open(filename,'r')
            inlines=infile.readlines()
            infile.close()
            
            for line1 in inlines:
                if line1[0]=='#': continue
                line = line1.split(',')
                if line[33]=='nan' or line[39]=='nan' or line[45]=='nan'\
                    or line[51]=='nan' or line[57]=='nan': continue
                
                # SN params
                x0.append(float(line[7])) #x0
                x0_err.append(float(line[8]))
                x1.append(float(line[9]))  # x1
                x1_err.append(float(line[10]))
                c.append(float(line[11]))  # c
                c_err.append(float(line[12]))
                
                # Host params
                z.append(float(line[4]))
                z_err.append(0.0)
                logr.append(np.log10(float(line[15])/float(line[42]))) # r
                logr_err.append(float(line[43])/(float(line[42])*np.log(10)))
                umag.append(float(line[18]))  # u_mag
                umag_err.append(float(line[19]))
                gmag.append(float(line[20]))  # g_mag
                gmag_err.append(float(line[21]))
                rmag.append(float(line[22]))  # r_mag
                rmag_err.append(float(line[23]))
                imag.append(float(line[24]))  # i_mag
                imag_err.append(float(line[25]))
                zmag.append(float(line[26]))  # z_mag
                zmag_err.append(float(line[27]))
                SB_u.append(float(line[32]))  # SB_u
                SB_u_err.append(float(line[33]))
                SB_g.append(float(line[38]))  # SB_g
                SB_g_err.append(float(line[39]))
                SB_r.append(float(line[44]))  # SB_r
                SB_r_err.append(float(line[45]))
                SB_i.append(float(line[50]))  # SB_i
                SB_i_err.append(float(line[52]))
                SB_z.append(float(line[56]))  # SB_z
                SB_z_err.append(float(line[57]))
        
        x0=np.array(x0)
        x0_err=np.array(x0_err)
        x1=np.array(x1)
        x1_err=np.array(x1_err)
        c=np.array(c)
        c_err=np.array(c_err)
        z=np.array(z)
        z_err=np.array(z_err)
        logr=np.array(logr)
        logr_err=np.array(logr_err)
        umag=np.array(umag)
        umag_err=np.array(umag_err)
        gmag=np.array(gmag)
        gmag_err=np.array(gmag_err)
        rmag=np.array(rmag)
        rmag_err=np.array(rmag_err)
        imag=np.array(imag)
        imag_err=np.array(imag_err)
        zmag=np.array(zmag)
        zmag_err=np.array(zmag_err)
        SB_u=np.array(SB_u)
        SB_u_err=np.array(SB_u_err)
        SB_g=np.array(SB_g)
        SB_g_err=np.array(SB_g_err)
        SB_r=np.array(SB_r)
        SB_r_err=np.array(SB_r_err)
        SB_i=np.array(SB_i)
        SB_i_err=np.array(SB_i_err)
        SB_z=np.array(SB_z)
        SB_z_err=np.array(SB_z_err)
        
        ug = umag-gmag
        ug_err = np.sqrt(umag_err**2+gmag_err**2)
        ur=umag-rmag
        ur_err=np.sqrt(umag_err**2+rmag_err**2)
        ui=umag-imag
        ui_err=np.sqrt(umag_err**2+imag_err**2)
        uz=umag-zmag
        uz_err=np.sqrt(umag_err**2+zmag_err**2)
        gr=gmag-rmag
        gr_err=np.sqrt(gmag_err**2+rmag_err**2)
        gi=gmag-imag
        gi_err=np.sqrt(gmag_err**2+imag_err**2)
        gz=gmag-zmag
        gz_err=np.sqrt(gmag_err**2+zmag_err**2)
        ri=rmag-imag
        ri_err=np.sqrt(rmag_err**2+imag_err**2)
        rz=rmag-zmag
        rz_err=np.sqrt(rmag_err**2+zmag_err**2)
        iz=imag-zmag
        iz_err=np.sqrt(imag_err**2+zmag_err**2)
        
        X=np.vstack([x0,x1,c,z,logr,ug,ur,ui,uz,gr,gi,gz,ri,rz,iz,SB_u,
                     SB_g,SB_r,SB_i,SB_z]).T
        Xerr = np.zeros(X.shape + X.shape[-1:])
        diag = np.arange(X.shape[-1])
        Xerr[:, diag, diag] = np.vstack([x0_err**2,x1_err**2,c_err**2,
                                         z_err**2,logr_err**2,ug_err**2,
                                         ur_err**2,ui_err**2,uz_err**2,
                                         gr_err**2,gi_err**2,gz_err**2,
                                         ri_err**2,rz_err**2,iz_err**2,
                                         SB_u_err**2,SB_g_err**2,
                                         SB_r_err**2,SB_i_err**2,
                                         SB_z_err**2]).T
        return X, Xerr
        
        