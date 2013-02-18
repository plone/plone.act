# -*- coding: utf-8 -*-

from zope.testbrowser.browser import Browser


class BrowserLibrary(object):

    def __init__(self):
        self.browser = Browser()

    def open_browser(self, *args):
        return self.browser

    def go_to(self, url):
        return self.browser.open(url)

    def page_should_contain(self, text):
        assert text in self.browser.contents
