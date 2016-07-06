import numpy as np
from math import *
import sys
from calc_dmod import calc_lumd
from calc_kcor import calc_kcor

'''
#  get_colors
#
#  Takes a list of lines from an SN data file and parses the SN parameters and host colors
#  Returns two arrays, one containing arrays of SN peak mag, SALT s, SALT2 x1,x0, and c parameters and the
#  other containing array pairs of host colors and errors, so that plotting can be done easily.
'''
def get_colors(line_list):
	
	mag=[]
	mag_err=[]
	s=[]
	s_err=[]
	c=[]
	c_err=[]
	x0=[]
	x0_err=[]
	x1=[]
	x1_err=[]

	u_mag=[]
	u_err=[]
	g_mag=[]
	g_err=[]
	r_mag=[]
	r_err=[]
	i_mag=[]
	i_err=[]
	z_mag=[]
	z_err=[]

	for line1 in line_list:
		if line1[0]=='#': continue
	
		line=line1.split(',')
		if len(line)<2: continue  #This is to prevent an error if the line is too short
		
		redshift=float(line[4])
		if redshift>0.5: continue
		lumd=calc_lumd(redshift)
		dmod=5*np.log10(lumd*10**6)-5
		
		mag.append(float(line[5])-dmod)
		if line[6]=='': mag_err.append(0)
		else: mag_err.append(float(line[6]))
		c.append(float(line[11]))
		c_err.append(float(line[12]))
		s.append(float(line[13]))
		s_err.append(float(line[14]))
		
		if line[7]=='' or line[9]=='':
			x0.append(-99)
			x0_err.append(-99)
			x1.append(-99)
			x1_err.append(-99)
		
		else:
			x0.append(float(line[7]))
			x0_err.append(float(line[8]))
			x1.append(float(line[9]))
			x1_err.append(float(line[10]))
			
		umag=float(line[18])
		uerr=float(line[19])
		gmag=float(line[20])
		gerr=float(line[21])
		rmag=float(line[22])
		rerr=float(line[23])
		imag=float(line[24])
		ierr=float(line[25])
		zmag=float(line[26])
		zerr=float(line[27])
	
		u_cor=calc_kcor('u',redshift,'u - r',umag-rmag)
		g_cor=calc_kcor('g',redshift,'g - r',gmag-rmag)
		r_cor=calc_kcor('r',redshift,'g - r',gmag-rmag)
		i_cor=calc_kcor('i',redshift,'g - i',gmag-imag)
		z_cor=calc_kcor('z',redshift,'r - z',rmag-zmag)
			
		u_mag.append(umag-u_cor)
		u_err.append(uerr)
		g_mag.append(gmag-g_cor)
		g_err.append(gerr)
		r_mag.append(rmag-r_cor)
		r_err.append(rerr)
		i_mag.append(imag-i_cor)
		i_err.append(ierr)
		z_mag.append(zmag-z_cor)
		z_err.append(zerr)
	
	# Convert lists to arrays for manipulation
	mag=np.array(mag)
	mag_err=np.array(mag_err)
	s=np.array(s)
	s_err=np.array(s_err)
	c=np.array(c)
	c_err=np.array(c_err)
	x0=np.array(x0)
	x0_err=np.array(x0_err)
	x1=np.array(x1)
	x1_err=np.array(x1_err)
	
	u_mag=np.array(u_mag)
	u_err=np.array(u_err)
	g_mag=np.array(g_mag)
	g_err=np.array(g_err)
	r_mag=np.array(r_mag)
	r_err=np.array(r_err)
	i_mag=np.array(i_mag)
	i_err=np.array(i_err)
	z_mag=np.array(z_mag)
	z_err=np.array(z_err)
	
	ug=u_mag-g_mag
	ug_err=np.sqrt(u_err**2+g_err**2)
	ur=u_mag-r_mag
	ur_err=np.sqrt(u_err**2+r_err**2)
	ui=u_mag-i_mag
	ui_err=np.sqrt(u_err**2+i_err**2)
	uz=u_mag-z_mag
	uz_err=np.sqrt(u_err**2+z_err**2)
	gr=g_mag-r_mag
	gr_err=np.sqrt(g_err**2+r_err**2)
	gi=g_mag-i_mag
	gi_err=np.sqrt(g_err**2+i_err**2)
	gz=g_mag-z_mag
	gz_err=np.sqrt(g_err**2+z_err**2)
	ri=r_mag-i_mag
	ri_err=np.sqrt(r_err**2+i_err**2)
	rz=r_mag-z_mag
	rz_err=np.sqrt(r_err**2+z_err**2)
	iz=i_mag-z_mag
	iz_err=np.sqrt(i_err**2+z_err**2)

	sn_array=np.array([np.array([mag,mag_err]),np.array([s,s_err]),np.array([c,c_err]),np.array([x0,x0_err]),np.array([x1,x1_err])])	
	color_array=np.array([np.array([ug,ug_err]),np.array([ur,ur_err]),np.array([ui,ui_err]),np.array([uz,uz_err]),np.array([gr,gr_err]),np.array([gi,gi_err]),np.array([gz,gz_err]),np.array([ri,ri_err]),np.array([rz,rz_err]),np.array([iz,iz_err])])
	
	return sn_array, color_array

'''
#  get_separation
#
#  Takes a list of lines from an SN data file and parses the SN parameters and SN offset from host nucleus
#  Returns two arrays, one containing arrays of SN peak mag, SALT s, SALT2 x1,x0, and c parameters and the
#  other containing arrays of host offsets in arcsec and kpc, so that plotting can be done easily.
'''
def get_separation(line_list):
	
	mag=[]
	mag_err=[]
	s=[]
	s_err=[]
	c=[]
	c_err=[]
	x0=[]
	x0_err=[]
	x1=[]
	x1_err=[]

	sep_kpc=[]
	sep_arcsec=[]
	
	for line1 in line_list:
		if line1[0]=='#': continue
	
		line=line1.split(',')
		if len(line)<2: continue  #This is to prevent an error if the line is too short
		if float(line[15])>300000: continue
		
		redshift=float(line[4])
		lumd=calc_lumd(redshift)
		dmod=5*np.log10(lumd*10**6)-5
		
		mag.append(float(line[5])-dmod)
		if line[6]=='': mag_err.append(0)
		else: mag_err.append(float(line[6]))
		c.append(float(line[11]))
		c_err.append(float(line[12]))
		s.append(float(line[13]))
		s_err.append(float(line[14]))
		
		if line[7]=='' or line[9]=='':
			x0.append(-99)
			x0_err.append(-99)
			x1.append(-99)
			x1_err.append(-99)
		
		else:
			x0.append(float(line[7]))
			x0_err.append(float(line[8]))
			x1.append(float(line[9]))
			x1_err.append(float(line[10]))
	
		sep=float(line[15])
		
		sep_arcsec.append(sep)
		
		d=calc_lumd(redshift)
		d_kpc=d*10**3
		sep_kpc.append(d_kpc*np.tan(np.deg2rad(sep/3600)))
	
	mag=np.array(mag)
	mag_err=np.array(mag_err)
	s=np.array(s)
	s_err=np.array(s_err)
	c=np.array(c)
	c_err=np.array(c_err)
	x0=np.array(x0)
	x0_err=np.array(x0_err)
	x1=np.array(x1)
	x1_err=np.array(x1_err)
	
	sep_arcsec=np.array(sep_arcsec)
	sep_kpc=np.array(sep_kpc)
	
	sn_array=np.array([np.array([mag,mag_err]),np.array([s,s_err]),np.array([c,c_err]),np.array([x0,x0_err]),np.array([x1,x1_err])])
	
	sep_array=np.array([sep_arcsec,sep_kpc])
	
	return sn_array,sep_array


'''
#  get_profiles
#
#  Takes a list of lines from an SN data file and parses the sersic index and surface brightness at SN loc.
#  Returns two arrays, one containing arrays of SN peak mag, SALT s, SALT2 x1,x0, and c parameters and the
#  other containing arrays of sersic indeces and surface brightnesses, so that plotting can be done easily.
'''
def get_profiles(line_list):
	
	mag=[]
	mag_err=[]
	s=[]
	s_err=[]
	c=[]
	c_err=[]
	x0=[]
	x0_err=[]
	x1=[]
	x1_err=[]
	
	mag_ser=[]
	mag_err_ser=[]
	s_ser=[]
	s_err_ser=[]
	c_ser=[]
	c_err_ser=[]
	x0_ser=[]
	x0_err_ser=[]
	x1_ser=[]
	x1_err_ser=[]
	
	mag_dev=[]
	mag_err_dev=[]
	s_dev=[]
	s_err_dev=[]
	c_dev=[]
	c_err_dev=[]
	x0_dev=[]
	x0_err_dev=[]
	x1_dev=[]
	x1_err_dev=[]
	
	mag_exp=[]
	mag_err_exp=[]
	s_exp=[]
	s_err_exp=[]
	c_exp=[]
	c_err_exp=[]
	x0_exp=[]
	x0_err_exp=[]
	x1_exp=[]
	x1_err_exp=[]
	
	ser_index=[]
	ser_index_all=[]
	
	sb_ser=[]
	sb_ser_err=[]
	sb_dev=[]
	sb_dev_err=[]
	sb_exp=[]
	sb_exp_err=[]
	
	for line1 in line_list:
		if line1[0]=='#': continue
	
		line=line1.split(',')
		if len(line)<2: continue  #This is to prevent an error if the line is too short

		redshift=float(line[4])
		lumd=calc_lumd(redshift)
		dmod=5*np.log10(lumd*10**6)-5
		
		mag.append(float(line[5])-dmod)
		if line[6]=='': mag_err.append(0)
		else: mag_err.append(float(line[6]))
		c.append(float(line[11]))
		c_err.append(float(line[12]))
		s.append(float(line[13]))
		s_err.append(float(line[14]))
		
		if line[7]=='' or line[9]=='':
			x0.append(-99)
			x0_err.append(-99)
			x1.append(-99)
			x1_err.append(-99)
		
		else:
			x0.append(float(line[7]))
			x0_err.append(float(line[8]))
			x1.append(float(line[9]))
			x1_err.append(float(line[10]))
		
		sep=float(line[15])
		
		if line[101]!='':
			mag_ser.append(float(line[5])-dmod)
			if line[6]=='': mag_err_ser.append(0)
			else: mag_err_ser.append(float(line[6]))
			c_ser.append(float(line[11]))
			c_err_ser.append(float(line[12]))
			s_ser.append(float(line[13]))
			s_err_ser.append(float(line[14]))
			
			if line[7]=='' or line[9]=='':
				x0_ser.append(-99)
				x0_err_ser.append(-99)
				x1_ser.append(-99)
				x1_err_ser.append(-99)
		
			else:
				x0_ser.append(float(line[7]))
				x0_err_ser.append(float(line[8]))
				x1_ser.append(float(line[9]))
				x1_err_ser.append(float(line[10]))
			
			n=float(line[101])
			r0=float(line[96])
			A=float(line[91])
			
			ser_index.append(n)
			ser_index_all.append(n)
			
			surf_b=A*np.exp((-1.0*((sep/r0))**(1.0/n)))
			### CALCULATE ERROR HERE ###
			surf_b_err=0
			sb_ser.append(surf_b)
			sb_ser_err.append(surf_b_err)
		
		dev_L=np.exp(float(line[61]))
		exp_L=np.exp(float(line[31]))
		
		if exp_L > dev_L:
			if line[101]=='': ser_index_all.append(1.0)
						
			re=float(line[38])
			re_err=float(line[39])
			if re==0: continue
			
			mag_exp.append(float(line[5])-dmod)
			if line[6]=='': mag_err_exp.append(0)
			else: mag_err_exp.append(float(line[6]))
			c_exp.append(float(line[11]))
			c_err_exp.append(float(line[12]))
			s_exp.append(float(line[13]))
			s_err_exp.append(float(line[14]))
			
			if line[7]=='' or line[9]=='':
				x0_exp.append(-99)
				x0_err_exp.append(-99)
				x1_exp.append(-99)
				x1_err_exp.append(-99)
		
			else:
				x0_exp.append(float(line[7]))
				x0_err_exp.append(float(line[8]))
				x1_exp.append(float(line[9]))
				x1_err_exp.append(float(line[10]))
			
			surf_b=np.exp(-1.68*(sep/re))
			surf_b_err=1.68*sep*surf_b*(1.0/re)*(re_err/re)
			
			sb_exp.append(surf_b)
			sb_exp_err.append(surf_b_err)

		else:
			if line[101]=='': ser_index_all.append(4.0)
			
			re=float(line[68])
			re_err=float(line[69])
			
			if re==0: continue
		
			mag_dev.append(float(line[5])-dmod)
			if line[6]=='': mag_err_dev.append(0)
			else: mag_err_dev.append(float(line[6]))
			c_dev.append(float(line[11]))
			c_err_dev.append(float(line[12]))
			s_dev.append(float(line[13]))
			s_err_dev.append(float(line[14]))
			
			if line[7]=='' or line[9]=='':
				x0_dev.append(-99)
				x0_err_dev.append(-99)
				x1_dev.append(-99)
				x1_err_dev.append(-99)
		
			else:
				x0_dev.append(float(line[7]))
				x0_err_dev.append(float(line[8]))
				x1_dev.append(float(line[9]))
				x1_err_dev.append(float(line[10]))
			
			surf_b=np.exp(-7.67*((sep/re)**0.25))
			surf_b_err=7.67*sep*surf_b*(re_err/re)*0.25*(1.0/re)**0.25
			
			sb_dev.append(surf_b)
			sb_dev_err.append(surf_b_err)
	
	mag=np.array(mag)
	mag_err=np.array(mag_err)
	s=np.array(s)
	s_err=np.array(s_err)
	c=np.array(c)
	c_err=np.array(c_err)
	x0=np.array(x0)
	x0_err=np.array(x0_err)
	x1=np.array(x1)
	x1_err=np.array(x1_err)

	mag_ser=np.array(mag_ser)
	mag_err_ser=np.array(mag_err_ser)
	s_ser=np.array(s_ser)
	s_err_ser=np.array(s_err_ser)
	c_ser=np.array(c_ser)
	c_err_ser=np.array(c_err_ser)
	x0_ser=np.array(x0_ser)
	x0_err_ser=np.array(x0_err_ser)
	x1_ser=np.array(x1_ser)
	x1_err_serr=np.array(x1_err_ser)
	
	mag_dev=np.array(mag_dev)
	mag_err_dev=np.array(mag_err_dev)
	s_dev=np.array(s_dev)
	s_err_dev=np.array(s_err_dev)
	c_dev=np.array(c_dev)
	c_err_dev=np.array(c_err_dev)
	x0_dev=np.array(x0_dev)
	x0_err_dev=np.array(x0_err_dev)
	x1_dev=np.array(x1_dev)
	x1_err_devr=np.array(x1_err_dev)
	
	mag_exp=np.array(mag_exp)
	mag_err_exp=np.array(mag_err_exp)
	s_exp=np.array(s_exp)
	s_err_exp=np.array(s_err_exp)
	c_exp=np.array(c_exp)
	c_err_exp=np.array(c_err_exp)
	x0_exp=np.array(x0_exp)
	x0_err_exp=np.array(x0_err_exp)
	x1_exp=np.array(x1_exp)
	x1_err_expr=np.array(x1_err_exp)
	
	ser_index=np.array(ser_index)
	ser_index_all=np.array(ser_index_all)
	sb_ser=np.array(sb_ser)
	sb_ser_err=np.array(sb_ser_err)
	sb_exp=np.array(sb_exp)
	sb_exp_err=np.array(sb_exp_err)
	sb_dev=np.array(sb_dev)
	sb_dev_err=np.array(sb_dev_err)
	
	sn_array_all=np.array([np.array([mag,mag_err]),np.array([s,s_err]),np.array([c,c_err]),np.array([x0,x0_err]),np.array([x1,x1_err])])
	
	sn_array_ser=np.array([np.array([mag_ser,mag_err_ser]),np.array([s_ser,s_err_ser]),np.array([c_ser,c_err_ser]),np.array([x0_ser,x0_err_ser]),np.array([x1_ser,x1_err_ser])])
	
	sn_array_dev=np.array([np.array([mag_dev,mag_err_dev]),np.array([s_dev,s_err_dev]),np.array([c_dev,c_err_dev]),np.array([x0_dev,x0_err_dev]),np.array([x1_dev,x1_err_dev])])
	
	sn_array_exp=np.array([np.array([mag_exp,mag_err_exp]),np.array([s_exp,s_err_exp]),np.array([c_exp,c_err_exp]),np.array([x0_exp,x0_err_exp]),np.array([x1_exp,x1_err_exp])])
	
	ser_ind_array=np.array([ser_index,ser_index_all])
	ser_sb_array=np.array([sb_ser,sb_ser_err])
	exp_sb_array=np.array([sb_exp,sb_exp_err])
	dev_sb_array=np.array([sb_dev,sb_dev_err])
	
	return sn_array_all,sn_array_ser,sn_array_exp,sn_array_dev,ser_ind_array,ser_sb_array,exp_sb_array,dev_sb_array
			