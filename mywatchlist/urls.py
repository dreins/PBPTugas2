from django.urls import path
from mywatchlist.views import show_mywatchlist_html, show_watchlist_xml, show_watchlist_json

app_name = 'mywatchlist'

urlpatterns = [
    path('html/', show_mywatchlist_html, name='mywatchlist'),
    path('xml/', show_watchlist_xml, name='mywatchlist'),
    path('json/', show_watchlist_json, name='mywatchlist'),
]