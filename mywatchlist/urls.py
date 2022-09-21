from django.urls import path
from mywatchlist.views import show_mywatchlist_msg, show_watchlist_html, show_watchlist_xml, show_watchlist_json

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist_msg, name='show_mywatchlist_msg'),
    path('html/', show_watchlist_html, name='show_watchlist_html'),
    path('xml/', show_watchlist_xml, name='show_watchlist_xml'),
    path('json/', show_watchlist_json, name='show_watchlist_json'),
]