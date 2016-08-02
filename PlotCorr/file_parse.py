import numpy as np
from math import *
import sys
from calc_dmod import calc_lumd
#from calc_kcor import calc_kcor

'''
#  get_colors
#
#  Takes a list of lines from an SN data file and parses the SN parameters and host colors
#  Returns two arrays, one containing arrays of SN peak mag, SALT s, SALT2 x0, x1, and c parameters, and the
#  separation of the SN from the host nucleus, and the other containing array pairs of host colors and errors,
#  so that plotting can be done easily.
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
	sep=[]

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
		
		if line[42]=='0.0': continue #Make sure there is an r-band R_e
		
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
		sep.append(np.log10(float(line[15])/float(line[42])))
		
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
			
		u_mag.append(float(line[18]))
		u_err.append(float(line[19]))
		g_mag.append(float(line[20]))
		g_err.append(float(line[21]))
		r_mag.append(float(line[22]))
		r_err.append(float(line[23]))
		i_mag.append(float(line[24]))
		i_err.append(float(line[25]))
		z_mag.append(float(line[26]))
		z_err.append(float(line[27]))
		
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
	sep=np.array(sep)
	
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

	sn_array=np.array([np.array([mag,mag_err]),np.array([s,s_err]),np.array([c,c_err]),np.array([x0,x0_err]),np.array([x1,x1_err]),sep])	
	color_array=np.array([np.array([ug,ug_err]),np.array([ur,ur_err]),np.array([ui,ui_err]),np.array([uz,uz_err]),np.array([gr,gr_err]),np.array([gi,gi_err]),np.array([gz,gz_err]),np.array([ri,ri_err]),np.array([rz,rz_err]),np.array([iz,iz_err])])
	
	return sn_array, color_array

'''
#  get_separation
#
#  Takes a list of lines from an SN data file and parses the SN parameters and SN offset from host nucleus
#  Returns two arrays, one containing arrays of SN peak mag, SALT s, SALT2 x1,x0, and c parameters and the
#  other containing an array of the separation from the host nucleus in units of arcsec, kpc, and the r-band
#  effective radius.
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
	sep_re=[]
	
	for line1 in line_list:
		if line1[0]=='#': continue
	
		line=line1.split(',')
		if len(line)<2: continue  #This is to prevent an error if the line is too short
		if float(line[15])>300000: continue
		
		# Get effective radius
		re=float(line[42])
		re_err=float(line[43])
		if re==0: continue
		
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
		sep_re.append(np.log10(sep/re))
		
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
	sep_re=np.array(sep_re)
	
	sn_array=np.array([np.array([mag,mag_err]),np.array([s,s_err]),np.array([c,c_err]),np.array([x0,x0_err]),np.array([x1,x1_err])])
	
	sep_array=np.array([sep_arcsec,sep_kpc,sep_re])
	
	return sn_array,sep_array


'''
#  get_profiles
#
#  Takes a list of lines from an SN data file and parses the sersic index and surface brightness at SN loc.
#  Returns two arrays, one containing arrays of SN peak mag, SALT s, SALT2 x1,x0, and c parameters, and 
#  separation from host, and the other containing arrays of surface brightnesses, so that
#  plotting can be done easily.
'''
def get_profiles(line_list):
	
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
	sep_dev=[]
	
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
	sep_exp=[]
	
	sb_u_exp=[]
	sb_u_exp_err=[]
	sb_g_exp=[]
	sb_g_exp_err=[]
	sb_r_exp=[]
	sb_r_exp_err=[]
	sb_i_exp=[]
	sb_i_exp_err=[]
	sb_z_exp=[]
	sb_z_exp_err=[]
	
	sb_u_dev=[]
	sb_u_dev_err=[]
	sb_g_dev=[]
	sb_g_dev_err=[]
	sb_r_dev=[]
	sb_r_dev_err=[]
	sb_i_dev=[]
	sb_i_dev_err=[]
	sb_z_dev=[]
	sb_z_dev_err=[]
	
	for line1 in line_list:
		if line1[0]=='#': continue
	
		line=line1.split(',')
		if len(line)<2: continue  #This is to prevent an error if the line is too short
		
		if line[42]=='0.0': continue #Make sure there is an r-band R_e

		redshift=float(line[4])
		lumd=calc_lumd(redshift)
		dmod=5*np.log10(lumd*10**6)-5
		'''
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
		'''
		sep=float(line[15])
		
		re_u=float(line[30])
		re_err_u=float(line[31])
		sb_u=float(line[32])
		sb_u_err=float(line[33])
		if re_u==0 or sb_u==0: continue
		
		re_g=float(line[36])
		re_err_g=float(line[37])
		sb_g=float(line[38])
		sb_g_err=float(line[39])
		if re_g==0 or sb_g==0: continue
		
		re_r=float(line[42])
		re_err_r=float(line[43])
		sb_r=float(line[44])
		sb_r_err=float(line[45])
		if re_r==0 or sb_u==0: continue
		
		re_i=float(line[48])
		re_err_i=float(line[49])
		sb_i=float(line[50])
		sb_i_err=float(line[51])
		if re_i==0 or sb_i==0: continue
		
		re_z=float(line[54])
		re_err_z=float(line[55])
		sb_z=float(line[56])
		sb_z_err=float(line[57])
		if re_z==0 or sb_z==0: continue
		
		if line[29]=='Exp':
			
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
			
			sep_exp.append(np.log10(sep/re_r))
									
			sb_u_exp.append(sb_u)
			sb_u_exp_err.append(sb_u_err)
			sb_g_exp.append(sb_g)
			sb_g_exp_err.append(sb_g_err)
			sb_r_exp.append(sb_r)
			sb_r_exp_err.append(sb_r_err)
			sb_i_exp.append(sb_i)
			sb_i_exp_err.append(sb_i_err)
			sb_z_exp.append(sb_z)
			sb_z_exp_err.append(sb_z_err)

		else:
		
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
			
			sep_dev.append(np.log10(sep/re_r))
			
			sb_u_dev.append(sb_u)
			sb_u_dev_err.append(sb_u_err)
			sb_g_dev.append(sb_g)
			sb_g_dev_err.append(sb_g_err)
			sb_r_dev.append(sb_r)
			sb_r_dev_err.append(sb_r_err)
			sb_i_dev.append(sb_i)
			sb_i_dev_err.append(sb_i_err)
			sb_z_dev.append(sb_z)
			sb_z_dev_err.append(sb_z_err)
	
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
	sep_dev=np.array(sep_dev)
	
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
	sep_exp=np.array(sep_exp)
	
	sb_u_dev=np.array(sb_u_dev)
	sb_u_dev_err=np.array(sb_u_dev_err)
	sb_g_dev=np.array(sb_g_dev)
	sb_g_dev_err=np.array(sb_g_dev_err)
	sb_r_dev=np.array(sb_r_dev)
	sb_r_dev_err=np.array(sb_r_dev_err)
	sb_i_dev=np.array(sb_i_dev)
	sb_i_dev_err=np.array(sb_i_dev_err)
	sb_z_dev=np.array(sb_z_dev)
	sb_z_dev_err=np.array(sb_z_dev_err)
	
	sb_u_exp=np.array(sb_u_exp)
	sb_u_exp_err=np.array(sb_u_exp_err)
	sb_g_exp=np.array(sb_g_exp)
	sb_g_exp_err=np.array(sb_g_exp_err)
	sb_r_exp=np.array(sb_r_exp)
	sb_r_exp_err=np.array(sb_r_exp_err)
	sb_i_exp=np.array(sb_i_exp)
	sb_i_exp_err=np.array(sb_i_exp_err)
	sb_z_exp=np.array(sb_z_exp)
	sb_z_exp_err=np.array(sb_z_exp_err)
	
	sn_array_dev=np.array([np.array([mag_dev,mag_err_dev]),np.array([s_dev,s_err_dev]),np.array([c_dev,c_err_dev]),np.array([x0_dev,x0_err_dev]),np.array([x1_dev,x1_err_dev]),sep_dev])
	sn_array_exp=np.array([np.array([mag_exp,mag_err_exp]),np.array([s_exp,s_err_exp]),np.array([c_exp,c_err_exp]),np.array([x0_exp,x0_err_exp]),np.array([x1_exp,x1_err_exp]),sep_exp])
	exp_sb_array=np.array([np.array([sb_u_exp,sb_u_exp_err]),np.array([sb_g_exp,sb_g_exp_err]),np.array([sb_r_exp,sb_r_exp_err]),np.array([sb_i_exp,sb_i_exp_err]),np.array([sb_z_exp,sb_z_exp_err])])
	dev_sb_array=np.array([np.array([sb_u_dev,sb_u_dev_err]),np.array([sb_g_dev,sb_g_dev_err]),np.array([sb_r_dev,sb_r_dev_err]),np.array([sb_i_dev,sb_i_dev_err]),np.array([sb_z_dev,sb_z_dev_err])])

	return sn_array_dev,sn_array_exp,dev_sb_array,exp_sb_array

'''
#  get_local_colors
#
#  Takes a list of lines from an SN data file and calculates the local colors from the local magnitudes.
#  Returns two arrays, one containing arrays of SN peak mag, SALT s, SALT2 x1,x0, and c parameters, and 
#  separation from host, and the other containing arrays of local colors, so that
#  plotting can be done easily.
'''
def get_local_colors(line_list):

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
	sep_dev=[]
	
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
	sep_exp=[]

	u_mag_dev=[]
	u_err_dev=[]
	g_mag_dev=[]
	g_err_dev=[]
	r_mag_dev=[]
	r_err_dev=[]
	i_mag_dev=[]
	i_err_dev=[]
	z_mag_dev=[]
	z_err_dev=[]
	
	u_mag_exp=[]
	u_err_exp=[]
	g_mag_exp=[]
	g_err_exp=[]
	r_mag_exp=[]
	r_err_exp=[]
	i_mag_exp=[]
	i_err_exp=[]
	z_mag_exp=[]
	z_err_exp=[]
	
	for line1 in line_list:
		if line1[0]=='#': continue
	
		line=line1.split(',')
		if len(line)<2: continue  #This is to prevent an error if the line is too short
		
		if line[42]=='0.0': continue #Make sure there is an r-band R_e

		redshift=float(line[4])
		lumd=calc_lumd(redshift)
		dmod=5*np.log10(lumd*10**6)-5
		
		sep=float(line[15])
		
		if line[34]=='nan' or line[34]=='inf' or line[35]=='nan' or line[35]=='inf' or line[40]=='nan' or line[40]=='inf' or line[41]=='nan' or line[41]=='inf' or line[46]=='nan' or line[46]=='inf' or line[47]=='nan' or line[47]=='inf' or line[52]=='nan' or line[52]=='inf' or line[53]=='nan' or line[53]=='inf' or line[58]=='nan' or line[58]=='inf' or line[59]=='nan' or line[59]=='inf': continue
		
		if line[29]=='Exp':
			
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
			
			sep_exp.append(np.log10(sep/float(line[42])))
			
			u_mag_exp.append(float(line[34]))
			u_err_exp.append(float(line[35]))
			g_mag_exp.append(float(line[40]))
			g_err_exp.append(float(line[41]))
			r_mag_exp.append(float(line[46]))
			r_err_exp.append(float(line[47]))
			i_mag_exp.append(float(line[52]))
			i_err_exp.append(float(line[53]))
			z_mag_exp.append(float(line[58]))
			z_err_exp.append(float(line[59]))
		
		else:
		
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
			
			sep_dev.append(np.log10(sep/float(line[42])))
			
			u_mag_dev.append(float(line[34]))
			u_err_dev.append(float(line[35]))
			g_mag_dev.append(float(line[40]))
			g_err_dev.append(float(line[41]))
			r_mag_dev.append(float(line[46]))
			r_err_dev.append(float(line[47]))
			i_mag_dev.append(float(line[52]))
			i_err_dev.append(float(line[53]))
			z_mag_dev.append(float(line[58]))
			z_err_dev.append(float(line[59]))
	
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
	sep_dev=np.array(sep_dev)
	
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
	sep_exp=np.array(sep_exp)
	
	u_mag_dev=np.array(u_mag_dev)
	u_err_dev=np.array(u_err_dev)
	g_mag_dev=np.array(g_mag_dev)
	g_err_dev=np.array(g_err_dev)
	r_mag_dev=np.array(r_mag_dev)
	r_err_dev=np.array(r_err_dev)
	i_mag_dev=np.array(i_mag_dev)
	i_err_dev=np.array(i_err_dev)
	z_mag_dev=np.array(z_mag_dev)
	z_err_dev=np.array(z_err_dev)

	u_mag_exp=np.array(u_mag_exp)
	u_err_exp=np.array(u_err_exp)
	g_mag_exp=np.array(g_mag_exp)
	g_err_exp=np.array(g_err_exp)
	r_mag_exp=np.array(r_mag_exp)
	r_err_exp=np.array(r_err_exp)
	i_mag_exp=np.array(i_mag_exp)
	i_err_exp=np.array(i_err_exp)
	z_mag_exp=np.array(z_mag_exp)
	z_err_exp=np.array(z_err_exp)

	ug_dev=u_mag_dev-g_mag_dev
	ug_err_dev=np.sqrt(u_err_dev**2+g_err_dev**2)
	ur_dev=u_mag_dev-r_mag_dev
	ur_err_dev=np.sqrt(u_err_dev**2+r_err_dev**2)
	ui_dev=u_mag_dev-i_mag_dev
	ui_err_dev=np.sqrt(u_err_dev**2+i_err_dev**2)
	uz_dev=u_mag_dev-z_mag_dev
	uz_err_dev=np.sqrt(u_err_dev**2+z_err_dev**2)
	gr_dev=g_mag_dev-r_mag_dev
	gr_err_dev=np.sqrt(g_err_dev**2+r_err_dev**2)
	gi_dev=g_mag_dev-i_mag_dev
	gi_err_dev=np.sqrt(g_err_dev**2+i_err_dev**2)
	gz_dev=g_mag_dev-z_mag_dev
	gz_err_dev=np.sqrt(g_err_dev**2+z_err_dev**2)
	ri_dev=r_mag_dev-i_mag_dev
	ri_err_dev=np.sqrt(r_err_dev**2+i_err_dev**2)
	rz_dev=r_mag_dev-z_mag_dev
	rz_err_dev=np.sqrt(r_err_dev**2+z_err_dev**2)
	iz_dev=i_mag_dev-z_mag_dev
	iz_err_dev=np.sqrt(i_err_dev**2+z_err_dev**2)

	ug_exp=u_mag_exp-g_mag_exp
	ug_err_exp=np.sqrt(u_err_exp**2+g_err_exp**2)
	ur_exp=u_mag_exp-r_mag_exp
	ur_err_exp=np.sqrt(u_err_exp**2+r_err_exp**2)
	ui_exp=u_mag_exp-i_mag_exp
	ui_err_exp=np.sqrt(u_err_exp**2+i_err_exp**2)
	uz_exp=u_mag_exp-z_mag_exp
	uz_err_exp=np.sqrt(u_err_exp**2+z_err_exp**2)
	gr_exp=g_mag_exp-r_mag_exp
	gr_err_exp=np.sqrt(g_err_exp**2+r_err_exp**2)
	gi_exp=g_mag_exp-i_mag_exp
	gi_err_exp=np.sqrt(g_err_exp**2+i_err_exp**2)
	gz_exp=g_mag_exp-z_mag_exp
	gz_err_exp=np.sqrt(g_err_exp**2+z_err_exp**2)
	ri_exp=r_mag_exp-i_mag_exp
	ri_err_exp=np.sqrt(r_err_exp**2+i_err_exp**2)
	rz_exp=r_mag_exp-z_mag_exp
	rz_err_exp=np.sqrt(r_err_exp**2+z_err_exp**2)
	iz_exp=i_mag_exp-z_mag_exp
	iz_err_exp=np.sqrt(i_err_exp**2+z_err_exp**2)
	
	sn_array_dev=np.array([np.array([mag_dev,mag_err_dev]),np.array([s_dev,s_err_dev]),np.array([c_dev,c_err_dev]),np.array([x0_dev,x0_err_dev]),np.array([x1_dev,x1_err_dev]),sep_dev])
	sn_array_exp=np.array([np.array([mag_exp,mag_err_exp]),np.array([s_exp,s_err_exp]),np.array([c_exp,c_err_exp]),np.array([x0_exp,x0_err_exp]),np.array([x1_exp,x1_err_exp]),sep_exp])
	
	color_array_dev=np.array([np.array([ug_dev,ug_err_dev]),np.array([ur_dev,ur_err_dev]),np.array([ui_dev,ui_err_dev]),np.array([uz_dev,uz_err_dev]),np.array([gr_dev,gr_err_dev]),np.array([gi_dev,gi_err_dev]),np.array([gz_dev,gz_err_dev]),np.array([ri_dev,ri_err_dev]),np.array([rz_dev,rz_err_dev]),np.array([iz_dev,iz_err_dev])])
	color_array_exp=np.array([np.array([ug_exp,ug_err_exp]),np.array([ur_exp,ur_err_exp]),np.array([ui_exp,ui_err_exp]),np.array([uz_exp,uz_err_exp]),np.array([gr_exp,gr_err_exp]),np.array([gi_exp,gi_err_exp]),np.array([gz_exp,gz_err_exp]),np.array([ri_exp,ri_err_exp]),np.array([rz_exp,rz_err_exp]),np.array([iz_exp,iz_err_exp])])

	return sn_array_dev,sn_array_exp,color_array_dev,color_array_exp
	
	
	
	
	