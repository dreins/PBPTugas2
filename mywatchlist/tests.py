from django.test import TestCase
from django.urls import reverse, resolve
from mywatchlist.views import show_watchlist_html, show_watchlist_xml, show_watchlist_json
class TestUrls(TestCase):
    def testMyWatchlistHTML(self):
        htmlURLTesting = reverse('mywatchlist:show_watchlist_html')
        self.assertEqual(resolve(htmlURLTesting).func, show_watchlist_html)

    def testMyWatchlistXML(self):
        xmlURLTesting = reverse('mywatchlist:show_watchlist_xml')
        self.assertEqual(resolve(xmlURLTesting).func, show_watchlist_xml)

        
    def testMyWatchlistJSON(self):
        jsonURLTesting = reverse('mywatchlist:show_watchlist_json')
        self.assertEqual(resolve(jsonURLTesting).func,show_watchlist_json)
