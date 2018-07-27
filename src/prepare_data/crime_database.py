"""Contains various helper functions to load crimes from the SQL database."""
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine


def get_engine(sqldb_path='data/processed/crimes.db', wal=False):
    """Sets up a SQL alchemy engine

    Creates a SQL alchemy engine and can set
    the journal mode to write-ahead logging.

    Parameters
    ----------
    sqldb_path : str, optional (default='data/processed/crimes.db')
        Path to SQL database, defaults to relative path
        to crimes database from project root. Useful to change
        for example when using Jupyter notebooks in other directories.

    wal : boolean, optional (default=False)
        If True, write-ahead logging will be enabled
        to allow simultaneous read and write access on SQL database.

    Returns
    -------
    SQLAlchemy engine
        Prepared sql alchemy engine
    """
    sqldb_path = Path(sqldb_path)
    assert sqldb_path.is_file()
    disk_engine = create_engine('sqlite:///' + str(sqldb_path))
    if wal:
        # Set journal_mode to write-ahead logging to allow for simultaneous
        # writing and reading access to database
        disk_engine.execute('PRAGMA journal_mode = wal')
    return disk_engine


def load_relevant_crimes(min_date,
                         max_date=None,
                         sqldb_path='data/processed/crimes.db',
                         chunksize=None,
                         disk_engine=None,
                         **kwargs):
    """Loads relevant violent and property crimes

    Wrapper around load_crimes which only loads violent and property crimes.
    Furthermore this function provides an easier interface to load
    relevant columns. If add_violent_col is True an additional column is
    added to the returned dataset with a dummy which is 1 for a violent crime
    and 0 for a property crime.

    Parameters
    ----------
    min_date : str, format = "YYYY-MM-DD"
        Min date which should be loaded

    max_date : str, format = "YYYY-MM-DD", optional (default=None)
        Max date which should be loaded

    sqldb_path : str, optional (default='data/processed/crimes.db')
        Path to SQL database, defaults to relative path
        to crimes database from project root. Useful to change
        for example when using Jupyter notebooks in other directories.

    chunksize : int, optional (default=None)
        If specified, return an iterator where chunksize
        is the number of rows to include in each chunk.

    kwargs : keyword arguments, optional
        Further keyword arguments directly passed on to pd.read_sql_query call

    Returns
    -------
    pd.DataFrame
        Dataframe containing loaded crimes
    """
    # FBI codes of the relevant categories
    violent_crime = {
        '01A': 'Homicide 1st & 2nd Degree',
        '02': 'Criminal Sexual Assault',
        '03': 'Robbery',
        '04A': 'Aggravated Assault',
        '04B': 'Aggravated Battery'
    }
    property_crime = {
        '05': 'Burglary',
        '06': 'Larceny',
        '07': 'Motor Vehicle Theft',
        '09': 'Arson'
    }

    crime_categories = list(violent_crime.keys()) + list(property_crime.keys())

    if max_date:
        df = load_crimes(
            """SELECT ID, Date, Longitude, Latitude, "Primary Type", "FBI Code"
        FROM crimes
        WHERE "FBI Code" IN {}
        AND Date BETWEEN "{}" and "{}"
        """.format(tuple(crime_categories), min_date, max_date),
            sqldb_path=sqldb_path,
            chunksize=chunksize,
            **kwargs)
    else:
        df = load_crimes(
            """SELECT ID, Date, Longitude, Latitude, "Primary Type", "FBI Code"
        FROM crimes
        WHERE "FBI Code" IN {}
        AND Date >= "{}"
        """.format(tuple(crime_categories), min_date),
            sqldb_path=sqldb_path,
            chunksize=chunksize,
            **kwargs)
    df['violent'] = df['FBI Code'].isin(list(violent_crime.keys())) * 1
    return df


def load_crimes(query_command,
                sqldb_path='data/processed/crimes.db',
                chunksize=None,
                disk_engine=None,
                **kwargs):
    """Loads crimes from SQlite database

    Executes query_command on crimes SQLite database.

    Parameters
    ----------
    query_command : str
        The SQL query to execute (name of table is 'crimes').

    sqldb_path : str, optional (default='data/processed/crimes.db')
        Path to SQL database, defaults to relative path
        to crimes database from project root. Useful to change
        for example when using Jupyter notebooks in other directories.

    chunksize : int, optional (default=None)
        If specified, return an iterator where chunksize
        is the number of rows to include in each chunk.

    kwargs : keyword arguments, optional
        Further keyword arguments directly passed on to pd.read_sql_query call

    Returns
    ------
    pd.DataFrame
        Dataframe containing loaded crimes

    Example
    -------
    >>> load_crimes('SELECT * FROM crimes LIMIT 3')
    """
    if disk_engine is None:
        disk_engine = get_engine(sqldb_path)
    # If date selected, parse it
    if ('Date' in query_command) or ('SELECT *' in query_command):
        df = pd.read_sql_query(
            query_command,
            disk_engine,
            parse_dates={'Date': '%Y-%m-%d %H:%M:%S.%f'},
            chunksize=chunksize,
            **kwargs)
    else:
        df = pd.read_sql_query(
            query_command, disk_engine, chunksize=chunksize, **kwargs)
    return df
