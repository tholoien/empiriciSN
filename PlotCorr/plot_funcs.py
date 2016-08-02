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

	# Plot order: SALT2 x0, SALT2 x1, SALT2 c, Separation

	for i in range(0,len(sdss_color)):
		axarr[i,0].scatter(sdss_sn[3][0],sdss_color[i][0],color='blue',s=3)
		axarr[i,1].scatter(sdss_sn[4][0],sdss_color[i][0],color='blue',s=3)
		axarr[i,2].scatter(sdss_sn[2][0],sdss_color[i][0],color='blue',s=3)
		axarr[i,3].scatter(sdss_sn[5],sdss_color[i][0],color='blue',s=3)
		#axarr[i,4].scatter(sdss_sn[3][0],sdss_color[i][0],color='blue',s=3)
		#axarr[i,5].scatter(sdss_sn[4][0],sdss_color[i][0],color='blue',s=3)

	for i in range(0,len(snls_color)):
		axarr[i,0].scatter(snls_sn[3][0],snls_color[i][0],color='red',s=3)
		axarr[i,1].scatter(snls_sn[4][0],snls_color[i][0],color='red',s=3)
		axarr[i,2].scatter(snls_sn[2][0],snls_color[i][0],color='red',s=3)
		axarr[i,3].scatter(snls_sn[5],snls_color[i][0],color='red',s=3)

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

	axarr[9,0].set_xlabel('SALT2 x0')
	axarr[9,1].set_xlabel('SALT2 x1')
	axarr[9,2].set_xlabel('SALT2 Color')
	axarr[9,3].set_xlabel('$\log{R/R_e}$')
	#axarr[9,3].set_xlabel('SALT Stretch')
	#axarr[9,4].set_xlabel('SALT2 x0')
	#axarr[9,5].set_xlabel('SALT2 x1')

	axarr[0,0].set_ylim(-0.5,3)
	axarr[1,0].set_ylim(-1,4.5)
	axarr[2,0].set_ylim(-1,5)
	axarr[3,0].set_ylim(-1,5)
	axarr[4,0].set_ylim(-0.5,1.5)
	axarr[5,0].set_ylim(-1,2)
	axarr[6,0].set_ylim(-1,3)
	axarr[7,0].set_ylim(-0.5,1)
	axarr[8,0].set_ylim(-0.5,1.5)
	axarr[9,0].set_ylim(-0.5,1)
	#axarr[9,4].set_xlim(-0.005,0.015)
	axarr[9,0].set_xscale('log')
	axarr[9,0].set_xlim(1e-6,2e-2)
	
	plt.show()
	#plt.savefig('host_colors.png',dpi=300,bbox_inches="tight")

def plot_sep(list1,list2):

	sdss_sn,sdss_sep=get_separation(list1)
	snls_sn,snls_sep=get_separation(list2)
			
	plt.clf()

	f,axarr=plt.subplots(3,3,sharex='col', sharey='row',figsize=(12,6))

	# Plot order: SALT2 x0, SALT2 x1, SALT2 c, Separation

	for i in range(0,len(sdss_sep)):
		axarr[i,0].scatter(sdss_sn[3][0],sdss_sep[i],color='blue',s=3)
		axarr[i,1].scatter(sdss_sn[4][0],sdss_sep[i],color='blue',s=3)
		axarr[i,2].scatter(sdss_sn[2][0],sdss_sep[i],color='blue',s=3)
		#axarr[i,4].scatter(sdss_sn[3][0],sdss_sep[i],color='blue',s=3)
		#axarr[i,5].scatter(sdss_sn[4][0],sdss_sep[i],color='blue',s=3)
	
	for i in range(0,len(snls_sep)):
		axarr[i,0].scatter(snls_sn[3][0],snls_sep[i],color='red',s=3)
		axarr[i,1].scatter(snls_sn[4][0],snls_sep[i],color='red',s=3)
		axarr[i,2].scatter(snls_sn[2][0],snls_sep[i],color='red',s=3)
	
	axarr[0,0].set_ylabel('Offset (")')
	axarr[1,0].set_ylabel('Offset (kpc)')
	axarr[2,0].set_ylabel('$\log{R/R_e}$')
	
	axarr[2,0].set_xlabel('SALT2 x0')
	axarr[2,1].set_xlabel('SALT2 x1')
	axarr[2,2].set_xlabel('SALT2 Color')
	
	axarr[2,0].set_xscale('log')
	axarr[2,0].set_xlim(1e-6,2e-2)
	
	axarr[0,0].set_yscale('log')
	axarr[1,0].set_yscale('log')
	axarr[0,0].set_ylim(0.01,40)
	axarr[1,0].set_ylim(0.01,1000)
	#axarr[1,4].set_xlabel('SALT2 x0')
	#axarr[1,5].set_xlabel('SALT2 x1')

	#axarr[1,4].set_xlim(-0.005,0.015)
	
	plt.show()
	#plt.savefig('host_offset.png',dpi=300,bbox_inches="tight")
	
def plot_prof(list1,list2):
	sdss_sn_dev,sdss_sn_exp,sdss_sb_dev,sdss_sb_exp=get_profiles(list1)
	snls_sn_dev,snls_sn_exp,snls_sb_dev,snls_sb_exp=get_profiles(list2)
			
	plt.clf()

	f,axarr=plt.subplots(10,4,sharex='col', sharey='row',figsize=(12,20))

	# Plot order: SALT2 x0, SALT2 x1, SALT2 c, Separation
	
	axarr[0,0].scatter(sdss_sn_dev[3][0],sdss_sb_dev[0][0],color='blue',s=3)
	axarr[0,1].scatter(sdss_sn_dev[4][0],sdss_sb_dev[0][0],color='blue',s=3)
	axarr[0,2].scatter(sdss_sn_dev[2][0],sdss_sb_dev[0][0],color='blue',s=3)
	axarr[0,3].scatter(sdss_sn_dev[5],sdss_sb_dev[0][0],color='blue',s=3)
	axarr[0,0].scatter(snls_sn_dev[3][0],snls_sb_dev[0][0],color='red',s=3)
	axarr[0,1].scatter(snls_sn_dev[4][0],snls_sb_dev[0][0],color='red',s=3)
	axarr[0,2].scatter(snls_sn_dev[2][0],snls_sb_dev[0][0],color='red',s=3)
	axarr[0,3].scatter(snls_sn_dev[5],snls_sb_dev[0][0],color='red',s=3)

	axarr[1,0].scatter(sdss_sn_exp[3][0],sdss_sb_exp[0][0],color='blue',s=3)
	axarr[1,1].scatter(sdss_sn_exp[4][0],sdss_sb_exp[0][0],color='blue',s=3)
	axarr[1,2].scatter(sdss_sn_exp[2][0],sdss_sb_exp[0][0],color='blue',s=3)
	axarr[1,3].scatter(sdss_sn_exp[5],sdss_sb_exp[0][0],color='blue',s=3)
	axarr[1,0].scatter(snls_sn_exp[3][0],snls_sb_exp[0][0],color='red',s=3)
	axarr[1,1].scatter(snls_sn_exp[4][0],snls_sb_exp[0][0],color='red',s=3)
	axarr[1,2].scatter(snls_sn_exp[2][0],snls_sb_exp[0][0],color='red',s=3)
	axarr[1,3].scatter(snls_sn_exp[5],snls_sb_exp[0][0],color='red',s=3)

	axarr[2,0].scatter(sdss_sn_dev[3][0],sdss_sb_dev[1][0],color='blue',s=3)
	axarr[2,1].scatter(sdss_sn_dev[4][0],sdss_sb_dev[1][0],color='blue',s=3)
	axarr[2,2].scatter(sdss_sn_dev[2][0],sdss_sb_dev[1][0],color='blue',s=3)
	axarr[2,3].scatter(sdss_sn_dev[5],sdss_sb_dev[1][0],color='blue',s=3)
	axarr[2,0].scatter(snls_sn_dev[3][0],snls_sb_dev[1][0],color='red',s=3)
	axarr[2,1].scatter(snls_sn_dev[4][0],snls_sb_dev[1][0],color='red',s=3)
	axarr[2,2].scatter(snls_sn_dev[2][0],snls_sb_dev[1][0],color='red',s=3)
	axarr[2,3].scatter(snls_sn_dev[5],snls_sb_dev[1][0],color='red',s=3)
	
	axarr[3,0].scatter(sdss_sn_exp[3][0],sdss_sb_exp[1][0],color='blue',s=3)
	axarr[3,1].scatter(sdss_sn_exp[4][0],sdss_sb_exp[1][0],color='blue',s=3)
	axarr[3,2].scatter(sdss_sn_exp[2][0],sdss_sb_exp[1][0],color='blue',s=3)
	axarr[3,3].scatter(sdss_sn_exp[5],sdss_sb_exp[1][0],color='blue',s=3)
	axarr[3,0].scatter(snls_sn_exp[3][0],snls_sb_exp[1][0],color='red',s=3)
	axarr[3,1].scatter(snls_sn_exp[4][0],snls_sb_exp[1][0],color='red',s=3)
	axarr[3,2].scatter(snls_sn_exp[2][0],snls_sb_exp[1][0],color='red',s=3)
	axarr[3,3].scatter(snls_sn_exp[5],snls_sb_exp[1][0],color='red',s=3)
	
	axarr[4,0].scatter(sdss_sn_dev[3][0],sdss_sb_dev[2][0],color='blue',s=3)
	axarr[4,1].scatter(sdss_sn_dev[4][0],sdss_sb_dev[2][0],color='blue',s=3)
	axarr[4,2].scatter(sdss_sn_dev[2][0],sdss_sb_dev[2][0],color='blue',s=3)
	axarr[4,3].scatter(sdss_sn_dev[5],sdss_sb_dev[2][0],color='blue',s=3)
	axarr[4,0].scatter(snls_sn_dev[3][0],snls_sb_dev[2][0],color='red',s=3)
	axarr[4,1].scatter(snls_sn_dev[4][0],snls_sb_dev[2][0],color='red',s=3)
	axarr[4,2].scatter(snls_sn_dev[2][0],snls_sb_dev[2][0],color='red',s=3)
	axarr[4,3].scatter(snls_sn_dev[5],snls_sb_dev[2][0],color='red',s=3)

	axarr[5,0].scatter(sdss_sn_exp[3][0],sdss_sb_exp[2][0],color='blue',s=3)
	axarr[5,1].scatter(sdss_sn_exp[4][0],sdss_sb_exp[2][0],color='blue',s=3)
	axarr[5,2].scatter(sdss_sn_exp[2][0],sdss_sb_exp[2][0],color='blue',s=3)
	axarr[5,3].scatter(sdss_sn_exp[5],sdss_sb_exp[2][0],color='blue',s=3)
	axarr[5,0].scatter(snls_sn_exp[3][0],snls_sb_exp[2][0],color='red',s=3)
	axarr[5,1].scatter(snls_sn_exp[4][0],snls_sb_exp[2][0],color='red',s=3)
	axarr[5,2].scatter(snls_sn_exp[2][0],snls_sb_exp[2][0],color='red',s=3)
	axarr[5,3].scatter(snls_sn_exp[5],snls_sb_exp[2][0],color='red',s=3)

	axarr[6,0].scatter(sdss_sn_dev[3][0],sdss_sb_dev[3][0],color='blue',s=3)
	axarr[6,1].scatter(sdss_sn_dev[4][0],sdss_sb_dev[3][0],color='blue',s=3)
	axarr[6,2].scatter(sdss_sn_dev[2][0],sdss_sb_dev[3][0],color='blue',s=3)
	axarr[6,3].scatter(sdss_sn_dev[5],sdss_sb_dev[3][0],color='blue',s=3)
	axarr[6,0].scatter(snls_sn_dev[3][0],snls_sb_dev[3][0],color='red',s=3)
	axarr[6,1].scatter(snls_sn_dev[4][0],snls_sb_dev[3][0],color='red',s=3)
	axarr[6,2].scatter(snls_sn_dev[2][0],snls_sb_dev[3][0],color='red',s=3)
	axarr[6,3].scatter(snls_sn_dev[5],snls_sb_dev[3][0],color='red',s=3)

	axarr[7,0].scatter(sdss_sn_exp[3][0],sdss_sb_exp[3][0],color='blue',s=3)
	axarr[7,1].scatter(sdss_sn_exp[4][0],sdss_sb_exp[3][0],color='blue',s=3)
	axarr[7,2].scatter(sdss_sn_exp[2][0],sdss_sb_exp[3][0],color='blue',s=3)
	axarr[7,3].scatter(sdss_sn_exp[5],sdss_sb_exp[3][0],color='blue',s=3)
	axarr[7,0].scatter(snls_sn_exp[3][0],snls_sb_exp[3][0],color='red',s=3)
	axarr[7,1].scatter(snls_sn_exp[4][0],snls_sb_exp[3][0],color='red',s=3)
	axarr[7,2].scatter(snls_sn_exp[2][0],snls_sb_exp[3][0],color='red',s=3)
	axarr[7,3].scatter(snls_sn_exp[5],snls_sb_exp[3][0],color='red',s=3)
	
	axarr[8,0].scatter(sdss_sn_dev[3][0],sdss_sb_dev[4][0],color='blue',s=3)
	axarr[8,1].scatter(sdss_sn_dev[4][0],sdss_sb_dev[4][0],color='blue',s=3)
	axarr[8,2].scatter(sdss_sn_dev[2][0],sdss_sb_dev[4][0],color='blue',s=3)
	axarr[8,3].scatter(sdss_sn_dev[5],sdss_sb_dev[4][0],color='blue',s=3)
	axarr[8,0].scatter(snls_sn_dev[3][0],snls_sb_dev[4][0],color='red',s=3)
	axarr[8,1].scatter(snls_sn_dev[4][0],snls_sb_dev[4][0],color='red',s=3)
	axarr[8,2].scatter(snls_sn_dev[2][0],snls_sb_dev[4][0],color='red',s=3)
	axarr[8,3].scatter(snls_sn_dev[5],snls_sb_dev[4][0],color='red',s=3)
	
	axarr[9,0].scatter(sdss_sn_exp[3][0],sdss_sb_exp[4][0],color='blue',s=3)
	axarr[9,1].scatter(sdss_sn_exp[4][0],sdss_sb_exp[4][0],color='blue',s=3)
	axarr[9,2].scatter(sdss_sn_exp[2][0],sdss_sb_exp[4][0],color='blue',s=3)
	axarr[9,3].scatter(sdss_sn_exp[5],sdss_sb_exp[4][0],color='blue',s=3)
	axarr[9,0].scatter(snls_sn_exp[3][0],snls_sb_exp[4][0],color='red',s=3)
	axarr[9,1].scatter(snls_sn_exp[4][0],snls_sb_exp[4][0],color='red',s=3)
	axarr[9,2].scatter(snls_sn_exp[2][0],snls_sb_exp[4][0],color='red',s=3)
	axarr[9,3].scatter(snls_sn_exp[5],snls_sb_exp[4][0],color='red',s=3)
	
	
	axarr[0,0].set_ylabel('u deV')
	axarr[1,0].set_ylabel('u Exp')
	axarr[2,0].set_ylabel('g deV')
	axarr[3,0].set_ylabel('g Exp')
	axarr[4,0].set_ylabel('r deV')
	axarr[5,0].set_ylabel('r Exp')
	axarr[6,0].set_ylabel('i deV')
	axarr[7,0].set_ylabel('i Exp')
	axarr[8,0].set_ylabel('z deV')
	axarr[9,0].set_ylabel('z Exp')
	
	axarr[9,0].set_xlabel('SALT2 x0')
	axarr[9,1].set_xlabel('SALT2 x1')
	axarr[9,2].set_xlabel('SALT2 Color')
	axarr[9,3].set_xlabel('$\log{R/R_e}$')
	
	axarr[9,0].set_xscale('log')
	axarr[9,0].set_xlim(1e-6,2e-2)
	
	axarr[0,0].set_ylim(-0.01,0.035)
	axarr[1,0].set_ylim(-0.1,1.5)
	axarr[2,0].set_ylim(-0.01,0.08)
	axarr[3,0].set_ylim(-0.2,4)
	axarr[4,0].set_ylim(-0.02,0.2)
	axarr[5,0].set_ylim(-0.5,7)
	axarr[6,0].set_ylim(-0.03,0.25)
	axarr[7,0].set_ylim(-0.5,8)
	axarr[8,0].set_ylim(-0.04,0.35)
	axarr[9,0].set_ylim(-1,12)
	#axarr[4,4].set_xlabel('SALT2 x0')
	#axarr[4,5].set_xlabel('SALT2 x1')

	#axarr[1,4].set_xlim(-0.005,0.015)
	plt.show()
	#plt.imshow('host_prof.png',dpi=300,bbox_inches="tight")

def plot_loc_color(list1,list2):
	sdss_sn_dev,sdss_sn_exp,sdss_loc_color_dev,sdss_loc_color_exp=get_local_colors(list1)
	snls_sn_dev,snls_sn_exp,snls_loc_color_dev,snls_loc_color_exp=get_local_colors(list2)
	
	plt.clf()

	f,axarr=plt.subplots(20,4,sharex='col', sharey='row',figsize=(12,40))

	for i in range(0,len(sdss_loc_color_dev)):
		axarr[i*2,0].scatter(sdss_sn_dev[3][0],sdss_loc_color_dev[i][0],color='blue',s=3)
		axarr[i*2,1].scatter(sdss_sn_dev[4][0],sdss_loc_color_dev[i][0],color='blue',s=3)
		axarr[i*2,2].scatter(sdss_sn_dev[2][0],sdss_loc_color_dev[i][0],color='blue',s=3)
		axarr[i*2,3].scatter(sdss_sn_dev[5],sdss_loc_color_dev[i][0],color='blue',s=3)
	
	for i in range(0,len(sdss_loc_color_exp)):
		axarr[i*2+1,0].scatter(sdss_sn_exp[3][0],sdss_loc_color_exp[i][0],color='blue',s=3)
		axarr[i*2+1,1].scatter(sdss_sn_exp[4][0],sdss_loc_color_exp[i][0],color='blue',s=3)
		axarr[i*2+1,2].scatter(sdss_sn_exp[2][0],sdss_loc_color_exp[i][0],color='blue',s=3)
		axarr[i*2+1,3].scatter(sdss_sn_exp[5],sdss_loc_color_exp[i][0],color='blue',s=3)
		
	for i in range(0,len(snls_loc_color_dev)):
		axarr[i*2,0].scatter(snls_sn_dev[3][0],snls_loc_color_dev[i][0],color='red',s=3)
		axarr[i*2,1].scatter(snls_sn_dev[4][0],snls_loc_color_dev[i][0],color='red',s=3)
		axarr[i*2,2].scatter(snls_sn_dev[2][0],snls_loc_color_dev[i][0],color='red',s=3)
		axarr[i*2,3].scatter(snls_sn_dev[5],snls_loc_color_dev[i][0],color='red',s=3)
	
	for i in range(0,len(snls_loc_color_exp)):
		axarr[i*2+1,0].scatter(snls_sn_exp[3][0],snls_loc_color_exp[i][0],color='red',s=3)
		axarr[i*2+1,1].scatter(snls_sn_exp[4][0],snls_loc_color_exp[i][0],color='red',s=3)
		axarr[i*2+1,2].scatter(snls_sn_exp[2][0],snls_loc_color_exp[i][0],color='red',s=3)
		axarr[i*2+1,3].scatter(snls_sn_exp[5],snls_loc_color_exp[i][0],color='red',s=3)

	axarr[0,0].set_ylabel('u-g (deV)')
	axarr[1,0].set_ylabel('u-g (Exp)')
	axarr[2,0].set_ylabel('u-r (deV)')
	axarr[3,0].set_ylabel('u-r (Exp)')
	axarr[4,0].set_ylabel('u-i (deV)')
	axarr[5,0].set_ylabel('u-i (Exp)')
	axarr[6,0].set_ylabel('u-z (deV)')
	axarr[7,0].set_ylabel('u-z (Exp)')
	axarr[8,0].set_ylabel('g-r (deV)')
	axarr[9,0].set_ylabel('g-r (Exp)')
	axarr[10,0].set_ylabel('g-i (deV)')
	axarr[11,0].set_ylabel('g-i (Exp)')
	axarr[12,0].set_ylabel('g-z (deV)')
	axarr[13,0].set_ylabel('g-z (Exp)')
	axarr[14,0].set_ylabel('r-i (deV)')
	axarr[15,0].set_ylabel('r-i (Exp)')
	axarr[16,0].set_ylabel('r-z (deV)')
	axarr[17,0].set_ylabel('r-z (Exp)')
	axarr[18,0].set_ylabel('i-z (deV)')
	axarr[19,0].set_ylabel('i-z (Exp)')

	axarr[19,0].set_xlabel('SALT2 x0')
	axarr[19,1].set_xlabel('SALT2 x1')
	axarr[19,2].set_xlabel('SALT2 Color')
	axarr[19,3].set_xlabel('$\log{R/R_e}$')
	
	axarr[19,0].set_xscale('log')
	axarr[19,0].set_xlim(1e-6,2e-2)
	
	axarr[0,0].set_ylim(-5,12)
	axarr[1,0].set_ylim(-10,13)
	axarr[2,0].set_ylim(-6,12)
	axarr[3,0].set_ylim(-10,13)
	axarr[4,0].set_ylim(-7,13)
	axarr[5,0].set_ylim(-13,14)
	axarr[6,0].set_ylim(-8,13)
	axarr[7,0].set_ylim(-10,13)
	axarr[8,0].set_ylim(-6,6)
	axarr[9,0].set_ylim(-7,7)
	axarr[10,0].set_ylim(-7,7)
	axarr[11,0].set_ylim(-7,7)
	axarr[12,0].set_ylim(-7,7)
	axarr[13,0].set_ylim(-7,7)
	axarr[14,0].set_ylim(-6,6)
	axarr[15,0].set_ylim(-6,6)
	axarr[16,0].set_ylim(-6,6)
	axarr[17,0].set_ylim(-6,6)
	axarr[18,0].set_ylim(-1,1)
	axarr[19,0].set_ylim(-1,1)


	plt.show()
