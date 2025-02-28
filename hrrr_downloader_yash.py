import boto3
from datetime import datetime, timedelta
from botocore import UNSIGNED
from botocore.config import Config

def object_fmt(init_time, sfc_or_prs, fcst_hr):
    part1 = f"hrrr.{init_time.strftime('%Y%m%d')}/conus/"
    part2 = f"hrrr.t{init_time.hour:02}z.wrf{sfc_or_prs}f{fcst_hr:02}.grib2"
    return part1 + part2

init_time = datetime(year=2021, month=1, day=1, hour=0)
fcst_hr = 1
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