# 2020_03_30,hzc
# add Econo 2L
#

# 2020_03_20, hzc
#
#


import numpy as np
import matplotlib.pyplot as plt
#
param={}
#
param["Test_2L_Buck"]["R_TH_HEATSINK"] = 0.10
param["Test_2L_Buck"]["T_TH_HEATSINK"] = 45.0
param["Test_2L_Buck"]["C_TH_HEATSINK"] = param["Test_2L_Buck"]["T_TH_HEATSINK"]/param["Test_2L_Buck"]["R_TH_HEATSINK"]

#
param["Test_3L"] = {}
param["Test_3L"]["R_TH_HEATSINK"] = 0.10
param["Test_3L"]["T_TH_HEATSINK"] = 45.0
param["Test_3L"]["C_TH_HEATSINK"] = param["Test_3L"]["T_TH_HEATSINK"] / param["Test_3L"]["R_TH_HEATSINK"]