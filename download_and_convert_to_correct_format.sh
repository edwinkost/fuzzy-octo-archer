#!/bin/bash

# This is for downloading from http://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_hd.pl?dir=%2Fgfs.2014120300%2Fmaster
# In this example, the (initial) date/time chosen is 2014120300 (as the satarting point for the forecasting).

for h in {00..99..3}; 
do
	wget "http://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_hd.pl?file=gfs.t00z.mastergrb2f$h&lev_surface=on&lev_2_m_above_ground=on&var_PRATE=on&var_TMP=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.2014120300%2Fmaster"
	rm *.grib2;
	mv filter* tmp.grib2;
	ncl_convert2nc tmp.grib2;
	cdo remapbil,mygrid tmp.nc tmp2.nc;
	rm tmp.nc
	mv tmp2.nc date_2014120300_forecasting_$h.nc;
	rm *.grib2;
done

for h in {102..300..3}; 
do
	wget "http://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_hd.pl?file=gfs.t00z.mastergrb2f$h&lev_surface=on&lev_2_m_above_ground=on&var_PRATE=on&var_TMP=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.2014120300%2Fmaster"
	rm *.grib2;
	mv filter* tmp.grib2;
	ncl_convert2nc tmp.grib2;
	cdo remapbil,mygrid tmp.nc tmp2.nc;
	rm tmp.nc
	mv tmp2.nc date_2014120300_forecasting_$h.nc;
	rm *.grib2;
done


