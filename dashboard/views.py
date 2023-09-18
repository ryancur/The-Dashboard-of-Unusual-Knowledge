from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


import plotly.express as px
import pyfredapi.series as pf
import yfinance as yf
import configparser

from dashboard.forms import EconGraphForm, MktGraphForm
from dashboard.models import Analysis

# import config
c = configparser.ConfigParser()
c.read("dashboard_config.cfg")

FRED_API_KEY = c["fred"]["api_key"]


@login_required
def analysis_list(request):
    analyses = Analysis.objects.all()
    context = {"analysis_list": analyses}
    return render(request, "dashboard/analysis_list.html", context)


@login_required
def show_graph(request, id):
    dashboard = get_object_or_404(Analysis, id=id)

    if dashboard.title.lower() == "economic data":
        graph_code_dict = {
            "UNRATE": "Unemployment Rate",
            "GDP": "Gross Domestic Product",
            "MEDCPIM158SFRBCLE": "Median Consumer Price Index",
            "WM1NS": "M1 Money Supply",
            "A939RC0Q052SBEA": "GDP Per Capita",
        }

        if request.method == "POST":
            form = EconGraphForm(request.POST)
            graph = None
            if form.is_valid():
                graph_id = form.cleaned_data["graph_data"]

                # dev - get data from FRED api
                df_graph_src = pf.get_series(series_id=graph_id, api_key=FRED_API_KEY)

                # reduce the dataframe down to only the data needed
                keep_cols = ["date", "value"]
                df = df_graph_src[keep_cols].copy()

                # plot the data with plotly
                fig = px.line(
                    df,
                    x="date",
                    y="value",
                    title=f"{graph_code_dict[graph_id]} in the United States",
                )
                graph = fig.to_html(
                    full_html=False, default_height=500, default_width=800
                )

        else:
            form = EconGraphForm()
            graph = None

        context = {"graph": graph, "form": form}
        return render(request, "dashboard/graph.html", context)

    elif dashboard.title.lower() == "market data":
        if request.method == "POST":
            form = MktGraphForm(request.POST)
            graph = None
            if form.is_valid():
                graph_ticker = form.cleaned_data["graph_data"]

                ticker_data = yf.Ticker(graph_ticker)

                hist = ticker_data.history(period="1y")
                hist.reset_index(inplace=True)

                # reduce the dataframe down to only the data needed
                keep_cols = ["Date", "Close"]
                df = hist[keep_cols].copy()

                # plot the data with plotly
                fig = px.line(
                    df,
                    x="Date",
                    y="Close",
                    title=f"Last Year of Daily Closing Prices for {graph_ticker}",
                )
                graph = fig.to_html(
                    full_html=False, default_height=500, default_width=800
                )

        else:
            form = MktGraphForm()
            graph = None

        context = {"graph": graph, "form": form}
        return render(request, "dashboard/graph.html", context)
