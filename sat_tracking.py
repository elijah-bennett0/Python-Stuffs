# tracks position of every operational GPS satellite in space
from skyfield.api import Topos, load

gps_sats_url = 'http://celestrak.com/NORAD/elements/gps-ops.txt'
sats = load.tle_file(gps_sats_url)

ts = load.timescale()
time = ts.now()

for sat in sats:
	geo = sat.at(time)
	sp = geo.subpoint()
	
	# gross print 
	print("[+] Satellite: %s | Lat: %s | Long: %s | Elevation (m): %.2f" 
	% (sat.name, str(sp.latitude).ljust(16), str(sp.longitude).ljust(17), 
	sp.elevation.m))
