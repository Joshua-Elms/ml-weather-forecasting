from datetime import datetime, timedelta
import xarray as xr
import cfgrib

def object_fmt(init_time, sfc_or_prs, fcst_hr):
    part1 = f"hrrr.{init_time.strftime('%Y%m%d')}/conus/"
    part2 = f"hrrr.t{init_time.hour:02}z.wrf{sfc_or_prs}f{fcst_hr:02}.grib2"
    return part1 + part2

init_time = datetime(year=2021, month=1, day=1, hour=0)
fcst_hr = 18
bucket = "noaa-hrrr-bdp-pds"
sfc_or_prs = 'sfc' # sfc or prs
typeOfLevel = 'surface' if sfc_or_prs == 'sfc' else 'isobaricInhPa'
stepType = 'instant' # instant, max, or accum, but we only want instant
save_path = f"{init_time.strftime('%Y%m%d')}_f{fcst_hr:02}_{sfc_or_prs}.grib2"

ds = xr.open_dataset(save_path, engine='cfgrib', filter_by_keys={'stepType': stepType, 'typeOfLevel': typeOfLevel})

breakpoint()

print('something')