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
    model_file: string (optional)
        Name of text file containing model being used (default=None).
    fit_method: string (optional)
        Name of XD fitting method to use (default='astroML'). Must be
        either 'astroML' or 'Bovy'.

    Notes
    -----
    The class can be initialized with a model or one can be loaded or
        fit to data.
    """
    def __init__(self, model_file=None, fit_method = 'astroML'):
        
        self.XDGMM = XDGMM(n_components = 7, method = fit_method)
        self.fit_method = fit_method
        
        if model_file is not None:
            self.read_model(model_file)
    
    def get_SN(self, X, Xerr=None, n_SN=1):
        """Get SN parameters for host data
        
        Conditions the XDGMM model based on the data in X and returns
            SN parameters sampled from the conditioned model.
            
        This assumes that the first three parameters used when fitting 
            the model are the SN parameters.

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

    def fit_model(self, X, Xerr, filename='empiriciSN_model.fit',
                  n_components=7):
        """Fit the XD model to data
        
        The specified method and n_components Gaussian components will
            be used (the optimal number of components was determined 
            using BIC to be 6 or 7). The fit will be saved in the file
            with name defined by the filename variable.

        Parameters
        ----------
        X: array_like, shape = (n_samples, n_features)
            Input data.
        Xerr: array_like, shape = (n_samples, n_features, n_features)
            Error on input data.
        filename: string (optional)
            Filename for model fit (default = 'empiriciSN_model.fit').
        n_components: float (optional)
            Number of Gaussian components to use (default = 7)
        """
        self.XDGMM.n_components = n_components
        self.XDGMM = self.XDGMM.fit(X, Xerr)
        self.XDGMM.save_model(filename)
        self.model_file = filename

    def fit_from_files(self, filelist, filename='empiriciSN_model.fit',
                  n_components=7):
        """Fit the XD model to data contained in files.
        
        Fit the model using data contained in the files listed in the
            filelist variable. This assumes that the data files are in
            the same format as those provided with this code and that 
            only redshift, distance from host nucleus, host colors, and
            local host surface brightness are being used for the fit.

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
        self.fit_model(X, Xerr, filename=filename, 
                       n_components=n_components)
    
    def read_model(self, filename):
        """Read the parameters of the model from a file.
        
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

    def component_test(self, X, Xerr, component_range, no_err=False):
        """Test the performance of the model for a range of numbers of 
        Gaussian components.
        
        Uses the XDGMM.bic_test method to compute the BIC score for 
            each n_components in the component_range array.
        
        Parameters
        ----------
        X: array_like, shape = (n_samples, n_features)
            Input data.
        Xerr: array_like, shape = (n_samples, n_features, n_features)
            Error on input data.
        component_range: array_like
            Range of n_components to test.
        no_err: bool (optional)
            Flag for whether to calculate the BIC with the errors 
            included or not. (default = False)
        
        Returns
        -------
        bics: array_like, shape = (len(param_range),)
            BIC for each value of n_components
        optimal_n_comp: float
            Number of components with lowest BIC score
        lowest_bic: float
            Lowest BIC from the scores computed.
        """
        bics, optimal_n_comp, lowest_bic = \
            self.XDGMM.bic_test(X, Xerr, component_range, no_err)
        return bics, optimal_n_comp, lowest_bic

    def get_logR(self,cond_indeces, R_index, X, Xerr=None):
        """Use a subset of parameters in given data to condition the 
        model and return a sample value for log(R/Re).
        
        The fit_params array specifies a list of indeces to use to
            condition the model. The model will be conditioned and then
            a radius will be drawn from the conditioned model.
        
        This is so that the radius can then be used to calculate local
            surface brightness to fully condition the model to sample
            likely SN parameters.
        
        This does not make assumptions about what parameters are being
            used in the model, but does assume that the model has been
            fit already and that the first three parameters in the data 
            that were used to fit the model are the SN parameters.
        
        Parameters
        ----------
        cond_indeces: array_like
            Array of indeces indicating which parameters to use to
            condition the model. Cannot contain [0, 1, 2] since these
            are SN parameters.
        R_index: int
            Index of log(R/Re) in the list of parameters that were used
            to fit the model.
        X: array_like, shape = (n < n_features,)
            Input data.
        Xerr: array_like, shape = (X.shape,) (optional)
            Error on input data. If none, no error used to condition.
            
        Returns
        -------
        logR: float
            Sample value of log(R/Re) taken from the conditioned model.
        """
        if self.model_file is None: 
            raise StandardError("Model parameters not set.")
        
        if 0 in cond_indeces or 1 in cond_indeces or 2 in cond_indeces:
            raise ValueError("Cannot condition model on SN parameters.")
        if R_index in cond_indeces:
            raise ValueError("Cannot condition model on log(R/Re).")
        
        cond_data = np.array([])
        if Xerr is not None: cond_err = np.array([])
        R_cond_idx = R_index
        n_features = self.XDGMM.mu.shape[1]
        j = 0
        
        for i in range(n_features):
            if i in cond_indeces:
                cond_data = np.append(cond_data,X[j])
                if Xerr is not None: np.append(cond_err, Xerr[j])
                j += 1
                if i < R_index: R_cond_idx -= 1
            else:
                cond_data = np.append(cond_data,np.nan)
                if Xerr is not None: np.append(cond_err, 0.0)
        
        if Xerr is not None: 
            cond_XDGMM = self.XDGMM.condition(cond_data, cond_err)
        else: cond_XDGMM = self.XDGMM.condition(cond_data)
        
        sample = cond_XDGMM.sample()
        logR = sample[0][R_cond_idx]
        return logR

    def set_fit_method(self, fit_method):
        """Set the XD fitting method
        
        Changes the fitting method of self.XDGMM to the one specified
            in fit_method.
        
        Parameters
        ----------
        fit_method: string
            Name of fitting method to use. Must be either 'astroML' or 
            'Bovy'.
        """
        if fit_method == 'astroML': n_iter = 100
        elif fit_method == 'Bovy': n_iter = 10**9
        else:
            raise ValueError("Method must be either 'astroML' or 'Bovy'")
        
        self.XDGMM.method = fit_method
        self.XDGMM.n_iter = n_iter
        self.fit_method = fit_method
        

    def get_data(self, filelist):
        """Parse SN and host data from a list of data files.
        
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
        profiles: array_list, shape = (n_samples,)
            Surface brightness profile ('Exp' for exponential, 'deV' for
            de Vaucouleurs) of each host in the sample. Used for radius
            fitting and local surface brightness calculation.
        """
        x0=np.array([])
        x0_err=np.array([])
        x1=np.array([])
        x1_err=np.array([])
        c=np.array([])
        c_err=np.array([])
        z=np.array([])
        z_err=np.array([])
        logr=np.array([])
        logr_err=np.array([])
        umag=np.array([])
        umag_err=np.array([])
        gmag=np.array([])
        gmag_err=np.array([])
        rmag=np.array([])
        rmag_err=np.array([])
        imag=np.array([])
        imag_err=np.array([])
        zmag=np.array([])
        zmag_err=np.array([])
        SB_u=np.array([])
        SB_u_err=np.array([])
        SB_g=np.array([])
        SB_g_err=np.array([])
        SB_r=np.array([])
        SB_r_err=np.array([])
        SB_i=np.array([])
        SB_i_err=np.array([])
        SB_z=np.array([])
        SB_z_err=np.array([])
        
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
                x0 = np.append(x0,float(line[7])) #x0
                x0_err = np.append(x0_err,float(line[8]))
                x1 = np.append(x1,float(line[9]))  # x1
                x1_err = np.append(x1_err,float(line[10]))
                c = np.append(c,float(line[11]))  # c
                c_err = np.append(c_err,float(line[12]))
                
                # Host params
                z = np.append(z,float(line[4]))
                z_err = np.append(z_err,0.0)
                logr = np.append(logr,np.log10(float(line[15])/float(line[42]))) # r
                logr_err = np.append(logr_err,float(line[43])/(float(line[42])*np.log(10)))
                umag = np.append(umag,float(line[18]))  # u_mag
                umag_err = np.append(umag_err,float(line[19]))
                gmag = np.append(gmag,float(line[20]))  # g_mag
                gmag_err = np.append(gmag_err,float(line[21]))
                rmag = np.append(rmag,float(line[22]))  # r_mag
                rmag_err = np.append(rmag_err,float(line[23]))
                imag = np.append(imag,float(line[24]))  # i_mag
                imag_err = np.append(imag_err,float(line[25]))
                zmag = np.append(zmag,float(line[26]))  # z_mag
                zmag_err = np.append(zmag_err,float(line[27]))
                SB_u = np.append(SB_u,float(line[32]))  # SB_u
                SB_u_err = np.append(SB_u_err,float(line[33]))
                SB_g = np.append(SB_g,float(line[38]))  # SB_g
                SB_g_err = np.append(SB_g_err,float(line[39]))
                SB_r = np.append(SB_r,float(line[44]))  # SB_r
                SB_r_err = np.append(SB_r_err,float(line[45]))
                SB_i = np.append(SB_i,float(line[50]))  # SB_i
                SB_i_err = np.append(SB_i_err,float(line[52]))
                SB_z = np.append(SB_z,float(line[56]))  # SB_z
                SB_z_err = np.append(SB_z_err,float(line[57]))
        
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
        
        