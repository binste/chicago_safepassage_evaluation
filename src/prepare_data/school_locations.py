"""Contains functions for preparation of data on school locations"""
import re

import geopandas as gpd
import pandas as pd
from pandas.api.types import is_numeric_dtype, is_string_dtype


def split_school(group, moved_schools):
    """Splits schools by changing name and id

    Adds 'OLD ' tag in front of school names for all years
    before they moved to another location
    (only if school actually moved at one point), as well as
    changes school id for old part by changing first number with a 9
    (no original school number, all 6 digits, starts with 9,
    therefore there should be no conflict and school_id stays unique).

    Parameters
    ----------
    group : pandas groupby object

    moved_schools : dict
        Contains names of moved schools as keys
        and observation number of first school year at new
        location as value.

    Returns
    -------
    pandas groupby object
        Modified group
    """
    school_names = group['school_name'].values
    school_name_original = school_names[0]
    # Only do it for schools which actually moved
    if school_name_original in moved_schools.keys():
        # Observation number where new location starts
        pos_change = moved_schools[school_name_original]
        # Change all school name entries up to that observation
        school_names[:pos_change] = 'OLD ' + school_name_original
        group['school_name'] = school_names
        # Change all school id entries up to that observation
        ids = group['school_id'].values
        id_original = ids[0]
        ids[:pos_change] = int('9' + str(id_original)[1:])
        group['school_id'] = ids
    return group


def take_last_values(group):
    """Overwrite all coordinates and addresses with most recent ones
    for all schools.

    Parameters
    ----------
    group : pandas groupby object

    Returns
    -------
    pandas groupby object
        Modified group
    """
    group['lat'] = group['lat'].values[-1]
    group['lon'] = group['lon'].values[-1]
    group['address'] = group['address'].values[-1]
    return group


def uppercase_school_categories(name):
    """Adjusts school names by certain conventions

    Changes Hs -> HS and Es -> ES in school name
    as well as handles some specific cases.

    Parameters
    ----------
    name : str
        School name which should be harmonized.

    Returns
    -------
    str
        Modified school name
    """
    name = re.sub('\sHs(?![A-Za-z0-9])', ' HS', name)
    name = re.sub('\sEs(?![A-Za-z0-9])', ' ES', name)
    name = re.sub('^Cics\s', 'CICS ', name)
    name = re.sub('^Yccs\s', 'YCCS ', name)
    return name


def check_dtypes(df):
    """Checks datatypes of columns: lat, lon, school_id, school_name

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe containing the above mentioned columns.

    Returns
    -------
    Nothing
    """
    # Make sure that coordinates and school ids are all numeric
    assert all(map(is_numeric_dtype, [df['lat'], df['lon'], df['school_id']]))
    # and that school names are characters
    assert is_string_dtype(df['school_name'])
    return


def load_locations(path, school_year):
    """Loads school locations from .csv file and harmonizes column names.

    Parameters
    ----------
    path : str or pathlib.Path
        Path to .csv file containing school locations which should be loaded.

    school_year : str, example = "SY1415"
        Name of school year which is contained in .csv file.

    Returns
    -------
    pd.DataFrame
        Processed school locations
    """
    sch_loc = pd.read_csv(path)
    sch_loc.drop('the_geom', axis='columns', inplace=True)
    # Harmonize names
    if school_year == 'SY1516':
        sch_loc.rename(
            {
                'Lat': 'lat',
                'Long': 'lon',
                'School_ID': 'school_id',
                'Address': 'address',
                'Short_Name': 'school_name'
            },
            axis='columns',
            inplace=True)
    elif school_year in ['SY1415', 'SY1314']:
        sch_loc.rename(
            {
                'SCHOOL_ID': 'school_id',
                'SCHOOL_NM': 'school_name',
                'SCH_ADDR': 'address',
                'GRADE_CAT': 'Grade_Cat',
                'GRADES': 'Grades',
                'SCH_TYPE': 'Governance',
                'X': 'lon',
                'Y': 'lat'
            },
            axis='columns',
            inplace=True)
    sch_loc['school_year'] = school_year
    # Check for correct data types
    check_dtypes(sch_loc)
    return sch_loc
