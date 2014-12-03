
import pcraster as pcr
import netCDF4 as nc
import numpy as np

pcr.setclone("Global_CloneMap_30min.map")



# for precipitation
#
# example how to read netcdf file 'date_2014120300_forecasting_99.nc' for the variable name 'PRATE_P8_L1_GLL0_avg3h'
test = nc.Dataset("date_2014120300_forecasting_99.nc")
field = test.variables['PRATE_P8_L1_GLL0_avg3h'][:,:]    # unit: kg m-2 s-1  
#
# convert to pcraster object
map_99 = pcr.numpy2pcr(pcr.Scalar,field,1e20)
pcr.report(map_99,"test.map")
#
# calculating precipitation for day 1 and convert it to m/day (Note: water density is 1000 kg/m3)
# pre_day_1 = ((map_03 + map_06 + map_09 + map_12 + map_15 + map_18 + map_21 + map_24)/8) * (24. * 3600.)/1000.
#
# calculating precipitation for day 2 and convert it to m/day (Note: water density is 1000 kg/m3)
# pre_day_2 = ((map_27 + map_30 + map_33 + map_36 + map_39 + map_42 + map_45 + map_48)/8) * (24. * 3600.)/1000.
#
# continue until the last day of forecasting hours that are available




# for temperature
#
# example how to read netcdf file 'date_2014120300_forecasting_99.nc' for the variable name 'TMP_P0_L103_GLL0'
test = nc.Dataset("date_2014120300_forecasting_99.nc")
field = test.variables['TMP_P0_L103_GLL0'][:,:]    # unit: K
#
# convert to pcraster object
map_99 = pcr.numpy2pcr(pcr.Scalar,field,1e20)
pcr.report(tmp_99,"test.map")

# calculating temperature for day 1 and convert it to Celcius
# tmp_day_1 = ((map_03 + map_06 + map_09 + map_12 + map_15 + map_18 + map_21 + map_24)/8) - 272.15.
#
# calculating temperature for day 2 and convert it to Celcius
# tmp_day_2 = ((map_27 + map_30 + map_33 + map_36 + map_39 + map_42 + map_45 + map_48)/8) - 272.15
#
# continue until the last day of forecasting hours that are available




# then convert it to netcdf files
