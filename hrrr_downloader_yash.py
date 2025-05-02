import boto3
from datetime import datetime, timedelta
from botocore import UNSIGNED
from botocore.config import Config

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

#Testing 

def object_fmt(init_time, sfc_or_prs, fcst_hr):
    part1 = f"hrrr.{init_time.strftime('%Y%m%d')}/conus/"
    part2 = f"hrrr.t{init_time.hour:02}z.wrf{sfc_or_prs}f{fcst_hr:02}.grib2"
    return part1 + part2

def download_hrrr_data(start_date, end_date, init_hours, fcst_hours, sfc_or_prs='sfc', bucket='noaa-hrrr-bdp-pds', get_idx=True):
    s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
    current_date = start_date
    while current_date <= end_date:
        for init_hour in init_hours:
            init_time = datetime(current_date.year, current_date.month, current_date.day, init_hour)
            for fcst_hr in fcst_hours:
                obj = object_fmt(init_time, sfc_or_prs, fcst_hr)
                save_path = f"{init_time.strftime('%Y%m%d_%H')}z_f{fcst_hr:02}_{sfc_or_prs}.grib2"
                try:
                    s3.download_file(bucket, obj, save_path)
                    if get_idx:
                        s3.download_file(bucket, obj + ".idx", save_path + ".idx")
                    print(f"Downloaded {obj} & *.idx to {save_path}")
                except Exception as e:
                    print(f"Error downloading {obj}: {e}")
        current_date += timedelta(days=1)
