
import pcraster as pcr
import netCDF4 as nc
import numpy as np

pcr.setclone("Global_CloneMap_30min.map")

# read netcdf file for the variable name: date_2014120300_forecasting_99.nc
test = nc.Dataset("date_2014120300_forecasting_99.nc")
field = test.variables['PRATE_P8_L1_GLL0_avg3h'][:,:]

# convert to pcraster object
map = pcr.numpy2pcr(pcr.Scalar,field,1e20)
pcr.report(map,"test.map")

