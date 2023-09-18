import pandas as pd
import plotly.express as px
import pyfredapi.series as pf
import configparser

# import config
c = configparser.ConfigParser()
c.read("dashboard_config.cfg")

FRED_API_KEY = c["fred"]["api_key"]

if __name__ == "__main__":
    pd.set_option("display.max_columns", 100)

    # dev - get data from FRED api
    df_unrate_src = pf.get_series(series_id="UNRATE", api_key=FRED_API_KEY)

    # reduce the dataframe down to only the data needed
    keep_cols = ["date", "value"]
    df_unrate = df_unrate_src[keep_cols].copy()

    # rename columns
    new_col_names = {"date": "date", "value": "unemployment_rate"}

    # apply the new column names
    df_unrate.rename(columns=new_col_names, inplace=True)

    # plot the data with plotly
    fig = px.line(
        df_unrate,
        x="date",
        y="unemployment_rate",
        title="Unemployment Rate in the United States",
    )
    fig.show()

    """
    Things to do:
        - label the x and y axes
        - figure out how to render the plotly plots in an html template
    """
