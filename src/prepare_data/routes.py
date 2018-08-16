"""Contains functions for preparation of data on Safe Passage routes"""
import geopandas as gpd
import pandas as pd


def read_routes_file(shapefile_path, school_year):
    """Reads shapefile of Safe Passage route
    and adds the respective school year as a column

    Parameters
    ----------
    shapefile_path : str
        Path to shapefile which should be read

    school_year : str
        School year in the format of 'SYXXYY',
        for example 'SY1516' for school year 2015-2016

    Returns
    -------
    gpd.DataFrame
        Contains parsed shapefile as well as corresponding school year
        as column 'school_year'
    """
    routes = gpd.read_file(shapefile_path)
    routes['school_year'] = school_year
    return routes


def harmonize_dataframe(df):
    """Harmonizes column names and datatypes

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe to harmonize

    Returns
    -------
    pd.DataFrame
    """
    df = df.copy()
    df = df.rename(
        {
            'rt_num': 'route_number',
            'school_nam': 'school_name',
            'schoolid': 'school_id'
        },
        axis='columns')[[
            'school_name', 'school_id', 'school_year', 'route_number',
            'geometry'
        ]]
    df['route_number'] = df['route_number'].astype('int64')
    df['school_id'] = df['school_id'].astype('int64')
    return df


def check_school_name_id_unique(df):
    """Checks if school_name and school_id uniquely identify one another.

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe which should be checked,
        containing columns 'school_name' and 'school_id'

    Returns
    -------
    Nothing
    """
    combos = zip(df['school_name'].values.tolist(),
                 df['school_id'].values.tolist())
    combos = list(set(combos))
    schools, ids = zip(*combos)
    assert len(set(schools)) == len(schools)
    assert len(set(ids)) == len(ids)
    return


def harmonize_name(name, name_lookup):
    """Looks up harmonized school name

    Parameters
    ----------
    name : str
        The school name to harmonize.

    name_lookup : iterable of two-value array-likes
        School names where the first value of each item is
        harmonized name and second value is list of
        different version of that name.

    Returns
    -------
    str
        Harmonized name
    """
    name_harmonized = [k for k, v in name_lookup if name.upper() in v]
    try:
        assert len(name_harmonized) == 1
    except AssertionError:
        raise Exception("Could not harmonize school {}".format(name))
    # Return unpacked harmonized name
    return (name_harmonized[0])


def include_harmonized_name(row):
    """Includes harmonized name in variations list

    Parameters
    ----------
    row : pd.Series
        Needs to contain 'variations' and 'harmonized_name'

    Returns
    -------
    pd.Series
    """
    if not pd.isnull(row['variations']):
        row['variations'] = ([row['harmonized_name'].upper()] + list(
            map(str.upper, row['variations'].split('; '))))
    else:
        row['variations'] = [row['harmonized_name'].upper()]
    return row


def harmonize_all_names(df, col, school_name_path):
    """Harmonizes all school names for a given dataframe and column

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe which contains the column to be harmonized.

    col : str
        Name of the column which should be harmonized and is contained
        in df.

    school_name_path : str or pathlib.Path
        Path to file which contains different school name versions.

    Returns
    -------
    pd.DataFrame
        Original dataframe with given column harmonized.
    """
    # Load list of different school name versions
    harmonized_names = pd.read_excel(school_name_path)

    # Make sure that there are no missing values in certain columns
    assert (not harmonized_names[['SY_added', 'school_id', 'harmonized_name']]
            .isnull().any().any())

    # Adds harmonized_name to variations and makes all names upper case
    # Upper case allows for "case-insensitive" comparison later on
    harmonized_names = harmonized_names.apply(
        include_harmonized_name, axis='columns')

    # Convert to list of tuples
    name_lookup = list(
        zip(harmonized_names['harmonized_name'],
            harmonized_names['variations']))

    # Harmonize school names of routes dataset
    # using the above created name_lookup
    df.loc[:, col] = df['school_name'].apply(
        harmonize_name, args=(name_lookup, ))
    return df
