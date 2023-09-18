from django.urls import path
from dashboard.views import show_graph, analysis_list

urlpatterns = [
    path("", analysis_list, name="home"),
    path("graph/<int:id>", show_graph, name="show_graph"),
]
