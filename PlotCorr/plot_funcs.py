import numpy as np
from matplotlib import pyplot as plt
#import corner
from matplotlib import rcParams
from file_parse import *

rcParams["font.size"] = 14
#rcParams["font.family"] = "sans-serif"
#rcParams["font.sans-serif"] = ["Computer Modern Sans"]
rcParams["text.usetex"] = True
#rcParams["text.latex.preamble"] = r"\usepackage{cmbright}"

def plot_color(list1,list2):

	sdss_sn,sdss_color=get_colors(list1)
	snls_sn,snls_color=get_colors(list2)
		
	plt.clf()

	f,axarr=plt.subplots(10,4,sharex='col', sharey='row',figsize=(12,20))

	# Plot order: B mag, r mag, color, SALT s, SALT2 x0, SALT2 x1

	for i in range(0,len(sdss_color)):
		axarr[i,1].scatter(sdss_sn[0][0],sdss_color[i][0],color='blue',s=3)
		axarr[i,2].scatter(sdss_sn[1][0],sdss_color[i][0],color='blue',s=3)
		axarr[i,3].scatter(sdss_sn[2][0],sdss_color[i][0],color='blue',s=3)
		#axarr[i,4].scatter(sdss_sn[3][0],sdss_color[i][0],color='blue',s=3)
		#axarr[i,5].scatter(sdss_sn[4][0],sdss_color[i][0],color='blue',s=3)

	for i in range(0,len(snls_color)):
		axarr[i,0].scatter(snls_sn[0][0],snls_color[i][0],color='red',s=3)
		axarr[i,2].scatter(snls_sn[1][0],snls_color[i][0],color='red',s=3)
		axarr[i,3].scatter(snls_sn[2][0],snls_color[i][0],color='red',s=3)

	axarr[0,0].set_ylabel('u-g')
	axarr[1,0].set_ylabel('u-r')
	axarr[2,0].set_ylabel('u-i')
	axarr[3,0].set_ylabel('u-z')
	axarr[4,0].set_ylabel('g-r')
	axarr[5,0].set_ylabel('g-i')
	axarr[6,0].set_ylabel('g-z')
	axarr[7,0].set_ylabel('r-i')
	axarr[8,0].set_ylabel('r-z')
	axarr[9,0].set_ylabel('i-z')

	axarr[9,0].set_xlabel('Peak B mag')
	axarr[9,1].set_xlabel('Peak r mag')
	axarr[9,2].set_xlabel('SALT2 Color')
	axarr[9,3].set_xlabel('SALT Stretch')
	#axarr[9,4].set_xlabel('SALT2 x0')
	#axarr[9,5].set_xlabel('SALT2 x1')

	axarr[0,0].set_ylim(-1,5)
	axarr[1,0].set_ylim(-1,7)
	axarr[2,0].set_ylim(-1,7)
	axarr[3,0].set_ylim(-1,7)
	axarr[4,0].set_ylim(-1,3)
	axarr[5,0].set_ylim(-1,3)
	axarr[6,0].set_ylim(-1,3)
	axarr[7,0].set_ylim(-2,2)
	axarr[8,0].set_ylim(-3,3)
	axarr[9,0].set_ylim(-4,4)
	#axarr[9,4].set_xlim(-0.005,0.015)
	
	plt.show()
	#plt.savefig('host_colors.png',dpi=300,bbox_inches="tight")

def plot_sep(list1,list2):

	sdss_sn,sdss_sep=get_separation(list1)
	snls_sn,snls_sep=get_separation(list2)
			
	plt.clf()

	f,axarr=plt.subplots(2,4,sharex='col', sharey='row',figsize=(12,4))

	# Plot order: B mag, r mag, color, SALT s, SALT2 x0, SALT2 x1

	for i in range(0,len(sdss_sep)):
		axarr[i,1].scatter(sdss_sn[0][0],sdss_sep[i],color='blue',s=3)
		axarr[i,2].scatter(sdss_sn[1][0],sdss_sep[i],color='blue',s=3)
		axarr[i,3].scatter(sdss_sn[2][0],sdss_sep[i],color='blue',s=3)
		#axarr[i,4].scatter(sdss_sn[3][0],sdss_sep[i],color='blue',s=3)
		#axarr[i,5].scatter(sdss_sn[4][0],sdss_sep[i],color='blue',s=3)
	
	for i in range(0,len(snls_sep)):
		axarr[i,0].scatter(snls_sn[0][0],snls_sep[i],color='red',s=3)
		axarr[i,2].scatter(snls_sn[1][0],snls_sep[i],color='red',s=3)
		axarr[i,3].scatter(snls_sn[2][0],snls_sep[i],color='red',s=3)
	
	axarr[0,0].set_ylabel('Offset (")')
	axarr[1,0].set_ylabel('Offset (kpc)')
	
	axarr[1,0].set_xlabel('Peak B mag')
	axarr[1,1].set_xlabel('Peak r mag')
	axarr[1,2].set_xlabel('SALT2 Color')
	axarr[1,3].set_xlabel('SALT Stretch')
	#axarr[1,4].set_xlabel('SALT2 x0')
	#axarr[1,5].set_xlabel('SALT2 x1')

	#axarr[1,4].set_xlim(-0.005,0.015)
	
	plt.show()
	#plt.savefig('host_offset.png',dpi=300,bbox_inches="tight")
	
def plot_prof(list1,list2):
	sdss_sn_all,sdss_sn_ser,sdss_sn_exp,sdss_sn_dev,sdss_ser_ind,sdss_ser_sb,sdss_exp_sb,sdss_dev_sb=get_profiles(list1)
	snls_sn_all,snls_sn_ser,snls_sn_exp,snls_sn_dev,snls_ser_ind,snls_ser_sb,snls_exp_sb,snls_dev_sb=get_profiles(list2)
		
	plt.clf()

	f,axarr=plt.subplots(5,4,sharex='col', sharey='row',figsize=(12,10))

	# Plot order: B mag, r mag, color, SALT s, SALT2 x0, SALT2 x1
	
	axarr[0,1].scatter(sdss_sn_ser[0][0],sdss_ser_ind[0],color='blue',s=3)
	axarr[0,2].scatter(sdss_sn_ser[1][0],sdss_ser_ind[0],color='blue',s=3)
	axarr[0,3].scatter(sdss_sn_ser[2][0],sdss_ser_ind[0],color='blue',s=3)
	#axarr[0,4].scatter(sdss_sn_ser[3][0],sdss_ser_ind[0],color='blue',s=3)
	#axarr[0,5].scatter(sdss_sn_ser[4][0],sdss_ser_ind[0],color='blue',s=3)
	
	axarr[0,0].scatter(snls_sn_ser[0][0],snls_ser_ind[0],color='red',s=3)
	axarr[0,2].scatter(snls_sn_ser[1][0],snls_ser_ind[0],color='red',s=3)
	axarr[0,3].scatter(snls_sn_ser[2][0],snls_ser_ind[0],color='red',s=3)
	
	axarr[1,1].scatter(sdss_sn_all[0][0],sdss_ser_ind[1],color='blue',s=3)
	axarr[1,2].scatter(sdss_sn_all[1][0],sdss_ser_ind[1],color='blue',s=3)
	axarr[1,3].scatter(sdss_sn_all[2][0],sdss_ser_ind[1],color='blue',s=3)
	#axarr[1,4].scatter(sdss_sn_all[3][0],sdss_ser_ind[1],color='blue',s=3)
	#axarr[1,5].scatter(sdss_sn_all[4][0],sdss_ser_ind[1],color='blue',s=3)
	
	axarr[1,0].scatter(snls_sn_all[0][0],snls_ser_ind[1],color='red',s=3)
	axarr[1,2].scatter(snls_sn_all[1][0],snls_ser_ind[1],color='red',s=3)
	axarr[1,3].scatter(snls_sn_all[2][0],snls_ser_ind[1],color='red',s=3)
	
	axarr[2,1].scatter(sdss_sn_ser[0][0],sdss_ser_sb[0],color='blue',s=3)
	axarr[2,2].scatter(sdss_sn_ser[1][0],sdss_ser_sb[0],color='blue',s=3)
	axarr[2,3].scatter(sdss_sn_ser[2][0],sdss_ser_sb[0],color='blue',s=3)
	#axarr[2,4].scatter(sdss_sn_ser[3][0],sdss_ser_sb[0],color='blue',s=3)
	#axarr[2,5].scatter(sdss_sn_ser[4][0],sdss_ser_sb[0],color='blue',s=3)
	
	axarr[2,0].scatter(snls_sn_ser[0][0],snls_ser_sb[0],color='red',s=3)
	axarr[2,2].scatter(snls_sn_ser[1][0],snls_ser_sb[0],color='red',s=3)
	axarr[2,3].scatter(snls_sn_ser[2][0],snls_ser_sb[0],color='red',s=3)
	
	axarr[3,1].scatter(sdss_sn_exp[0][0],sdss_exp_sb[0],color='blue',s=3)
	axarr[3,2].scatter(sdss_sn_exp[1][0],sdss_exp_sb[0],color='blue',s=3)
	axarr[3,3].scatter(sdss_sn_exp[2][0],sdss_exp_sb[0],color='blue',s=3)
	#axarr[3,4].scatter(sdss_sn_exp[3][0],sdss_exp_sb[0],color='blue',s=3)
	#axarr[3,5].scatter(sdss_sn_exp[4][0],sdss_exp_sb[0],color='blue',s=3)
	
	axarr[3,0].scatter(snls_sn_exp[0][0],snls_exp_sb[0],color='red',s=3)
	axarr[3,2].scatter(snls_sn_exp[1][0],snls_exp_sb[0],color='red',s=3)
	axarr[3,3].scatter(snls_sn_exp[2][0],snls_exp_sb[0],color='red',s=3)
	
	axarr[4,1].scatter(sdss_sn_dev[0][0],sdss_dev_sb[0],color='blue',s=3)
	axarr[4,2].scatter(sdss_sn_dev[1][0],sdss_dev_sb[0],color='blue',s=3)
	axarr[4,3].scatter(sdss_sn_dev[2][0],sdss_dev_sb[0],color='blue',s=3)
	#axarr[4,4].scatter(sdss_sn_dev[3][0],sdss_dev_sb[0],color='blue',s=3)
	#axarr[4,5].scatter(sdss_sn_dev[4][0],sdss_dev_sb[0],color='blue',s=3)
	
	axarr[4,0].scatter(snls_sn_dev[0][0],snls_dev_sb[0],color='red',s=3)
	axarr[4,2].scatter(snls_sn_dev[1][0],snls_dev_sb[0],color='red',s=3)
	axarr[4,3].scatter(snls_sn_dev[2][0],snls_dev_sb[0],color='red',s=3)
	
	
	axarr[0,0].set_ylabel('Sersic n')
	axarr[1,0].set_ylabel('Sersic n (all)')
	axarr[2,0].set_ylabel('$I(r)_{Ser}$ (nm/arcsec)')
	axarr[3,0].set_ylabel('$I(r)_{Exp}/I_0$')
	axarr[4,0].set_ylabel('$I(r)_{deV}/I_0$')
	
	axarr[4,0].set_xlabel('Peak B mag')
	axarr[4,1].set_xlabel('Peak r mag')
	axarr[4,2].set_xlabel('SALT2 Color')
	axarr[4,3].set_xlabel('SALT Stretch')
	#axarr[4,4].set_xlabel('SALT2 x0')
	#axarr[4,5].set_xlabel('SALT2 x1')

	#axarr[1,4].set_xlim(-0.005,0.015)
	plt.show()
	#plt.imshow('host_prof.png',dpi=300,bbox_inches="tight")
