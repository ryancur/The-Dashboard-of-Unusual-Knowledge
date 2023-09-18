from django import forms

ECON_GRAPH_CHOICES = [
    ("UNRATE", "Unemployment Rate"),
    ("GDP", "Gross Domestic Product"),
    ("MEDCPIM158SFRBCLE", "Median Consumer Price Index"),
    ("WM1NS", "M1 Money Supply"),
    ("A939RC0Q052SBEA", "GDP Per Capita"),
]

MKT_GRAPH_CHOICES = [
    ("SPY", "S&P500"),
    ("AAPL", "Apple"),
    ("MSFT", "Microsoft"),
    ("GOOG", "Google"),
    ("AMD", "Advanced Micro Devices (AMD)"),
    ("AMC", "AMC Entertainment Holdings"),
    ("AMZN", "Amazon.com"),
]


class EconGraphForm(forms.Form):
    graph_data = forms.CharField(
        label="What data do you want to see?",
        widget=forms.Select(choices=ECON_GRAPH_CHOICES),
    )


class MktGraphForm(forms.Form):
    graph_data = forms.CharField(
        label="What company stock do you want to see?",
        widget=forms.Select(choices=MKT_GRAPH_CHOICES),
    )
