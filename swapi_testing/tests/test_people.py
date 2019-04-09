''' Testing Film page object '''

import pytest

from pages import people

# We call Film Page ones
GET_people = people.People().GET_people_page()


class TestPeople():

    @pytest.mark.tryfirst
    def test_check_people_response_code(self):
        assert GET_people.status_code is 200

    def test_check_people_response_body_not_empty(self):
        _r_body = GET_people.json()
        assert len(_r_body) > 0

    @pytest.mark.parametrize('people_profile_url', [(x['name'], x['url']) for x in GET_people.json()['results']])
    def test_check_link_to_people_acc_correct(self, people_profile_url):
        _profile_page = people.People().GET_one_people(url=people_profile_url[1])
        # Check repose status
        assert _profile_page.status_code is 200

        # Check Episode correct redirection correct
        assert people_profile_url[0] == _profile_page.json()['name']

