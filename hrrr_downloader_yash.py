import boto3
import os
from datetime import datetime, timedelta
from botocore import UNSIGNED
from botocore.config import Config
'''
def object_fmt(init_time, sfc_or_prs, fcst_hr):
    part1 = f"hrrr.{init_time.strftime('%Y%m%d')}/conus/"
    part2 = f"hrrr.t{init_time.hour:02}z.wrf{sfc_or_prs}f{fcst_hr:02}.grib2"
    return part1 + part2
for k in range(14,25):
    init_time = datetime(year=2021, month=1, day=2, hour=0)
    fcst_hr = k
    get_idx = True
    bucket = "noaa-hrrr-bdp-pds"
    sfc_or_prs = 'sfc'
    save_path = f"{init_time.strftime('%Y%m%d')}_f{fcst_hr:02}_{sfc_or_prs}.grib2"
    obj = object_fmt(init_time, sfc_or_prs, 1)
    # Create an unsigned S3 client (for public buckets)
    s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))

    # Download the files
    s3.download_file(bucket, obj, save_path)
    if get_idx:
        s3.download_file(bucket, obj + ".idx", save_path + ".idx")

    print(f"Downloaded {obj} & *.idx to {save_path}")
for j in range(3,18):
    for i in range(0,25):
        init_time = datetime(year=2021, month=1, day=j, hour=0)
        fcst_hr = i
        get_idx = True
        bucket = "noaa-hrrr-bdp-pds"
        sfc_or_prs = 'sfc'
        save_path = f"{init_time.strftime('%Y%m%d')}_f{fcst_hr:02}_{sfc_or_prs}.grib2"
        obj = object_fmt(init_time, sfc_or_prs, 1)
        # Create an unsigned S3 client (for public buckets)
        s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))

        # Download the files
        s3.download_file(bucket, obj, save_path)
        if get_idx:
            s3.download_file(bucket, obj + ".idx", save_path + ".idx")

        print(f"Downloaded {obj} & *.idx to {save_path}")
'''
#Testing 

def object_fmt(init_time, sfc_or_prs, fcst_hr):
    part1 = f"hrrr.{init_time.strftime('%Y%m%d')}/conus/"
    part2 = f"hrrr.t{init_time.hour:02}z.wrf{sfc_or_prs}f{fcst_hr:02}.grib2"
    return part1 + part2

def download_hrrr_data(start_date, end_date, init_hours, fcst_hours, sfc_or_prs='sfc', bucket='noaa-hrrr-bdp-pds', get_idx=True, save_dir='hrrr_data'):
    # Create save directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)
    
    s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
    current_date = start_date
    while current_date <= end_date:
        for init_hour in init_hours:
            init_time = datetime(current_date.year, current_date.month, current_date.day, init_hour)
            for fcst_hr in fcst_hours:
                obj = object_fmt(init_time, sfc_or_prs, fcst_hr)
                # Construct full save path including directory
                save_filename = f"{init_time.strftime('%Y%m%d_%H')}z_f{fcst_hr:02}_{sfc_or_prs}.grib2"
                save_path = os.path.join(save_dir, save_filename)
                try:
                    s3.download_file(bucket, obj, save_path)
                    if get_idx:
                        idx_save_path = os.path.join(save_dir, save_filename + ".idx")
                        s3.download_file(bucket, obj + ".idx", idx_save_path)
                    print(f"Downloaded {obj} & *.idx to {save_path}")
                except Exception as e:
                    print(f"Error downloading {obj}: {e}")
        current_date += timedelta(days=1)
#Training
#start_date = datetime(2021, 3, 1)
#end_date = datetime(2021, 6, 1)
#init_times = [0]
#fcst_hours = range(0,25)
#download_hrrr_data(start_date, end_date, init_times, fcst_hours)

#Testing Jan 5-6 2025 Winter Storm
start_date = datetime(2025, 1, 5)
end_date = datetime(2021, 1, 6)
init_times = [0]
fcst_hours = range(0,25)
download_hrrr_data(start_date, end_date, init_times, fcst_hours, save_dir='mod_testing')

#Testing Jun 18-19 2021 Storm Complex
#start_date = datetime(2021, 6, 18)
#end_date = datetime(2021, 6, 19)
#init_times = [0]
#fcst_hours = range(0,25)
#download_hrrr_data(start_date, end_date, init_times, fcst_hours, save_dir='mod_testing')

#Testing Jan 31- Feb 2 2011 Winter Storm (Groundhog day blizzard)
#start_date = datetime(2011, 1, 31)
#end_date = datetime(2011, 2, 2)
#init_times = [0]
#fcst_hours = range(0,25)
#download_hrrr_data(start_date, end_date, init_times, fcst_hours, save_dir='mod_testing')

#Testing Dec 22 2022 Winter Storm
#start_date = datetime(2022, 12, 22)
#end_date = datetime(2022, 12, 22)
#init_times = [0]
#fcst_hours = range(0,25)
#download_hrrr_data(start_date, end_date, init_times, fcst_hours, save_dir='mod_testing')

#Testing Mar 31- Apr 1 2023 Tornado Outbreak
#start_date = datetime(2023, 3, 31)
#end_date = datetime(2023, 4, 1)
#init_times = [0]
#fcst_hours = range(0,25)
#download_hrrr_data(start_date, end_date, init_times, fcst_hours, save_dir='mod_testing')