# ML Weather Forecasting

This project aims to provide accurate weather forecasting using machine learning techniques.

## Table of Contents
- [Installation](#installation)
- [Data](#data)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ml-weather-forecasting.git
    cd ml-weather-forecasting
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Data

1. Data sourced from University of Utah:
    - [AWS HRRR Archive](https://registry.opendata.aws/noaa-hrrr-pds/) 
    - [University of Utah page](https://home.chpc.utah.edu/~u0553130/Brian_Blaylock/hrrr_FAQ.html)
    - [HRRR GRIB2 Tables](https://home.chpc.utah.edu/~u0553130/Brian_Blaylock/HRRR_archive/hrrr_sfc_table_f02-f18.html) (these show levels/steps/names for variables in grib2 data)

2. `hrrr_downloader.py` can be used to download one grib2 file

3. `hrrr_reader.py` will extract the desired variables from a grib2 file into an `xarray.Dataset`