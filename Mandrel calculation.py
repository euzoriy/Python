# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:37:27 2019

@author: ievgenz
#"""
#/* MANDREL.C   M. W. Klotz   2/05
#
#Computing mandrel size for spring winding.  Based on Kozo Hiraoka's article in
#"Home Shop Machinist", July/August 1987, pg. 30.
#/* vmark..------------ global variable declarations ----------------------- */
#int wt;			//wire type index
c0 = [ 0.980364,0.012436 ]#;		//constant coefficient
c1 = [ -0.012436,-0.11018 ]#;		//first order coefficient
#dbl id;			//spring internal diameter (in)
#dbl ds;			//average spring diameter (in)
#dbl dw;			//wire diameter (in)
#dbl fact;		//empirical factor (nd)
#dbl dm;			//mandrel diameter (in)

print ("Kozo Hiraoka's SPRING WINDING MANDREL DIAMETER CALCULATION\n")

w_t=float(input("Wire type: music wire (0) or phosphorus bronze (1):\n>>> "))
if (w_t != 1):
    w_t = 0
d_w = float(input("Wire diameter, in\n>>> "))
i_d = float(input("Spring inside diameter, in\n>>> "))
d_s = i_d + d_w			#spring average diameter

fact = c0[w_t] + c1[w_t] * d_s / d_w	#empirical factor
d_m = fact * d_s - d_w			#mandrel diameter

print (format("\nRecommended mandrel diameter = %.3lf in\n"% d_m))
