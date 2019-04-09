''' This is a Page Object'''
''' Each Functional page should be defined separably'''

import requests

from pages.basepage import BaseClass


class People(BaseClass):

    def __init__(self):
        BaseClass.__init__(self)
        self._url = self._host + self._schema

    def GET_people_page(self):
        sufix = 'people/'
        response = requests.get(
            url=(self._url + sufix),
            headers=self._header
        )
        return response

    def GET_one_people(self, url):
        response = requests.get(
            url=url,
            headers=self._header
        )
        return response
