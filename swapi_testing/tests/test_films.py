''' Testing Film page object '''


import pytest

from pages import films

# We call Film Page ones
GET_films_request = films.FilmPage().GET_films_page()




class TestFilm():
    @pytest.mark.trylast
    def test_page_response_code_200(self):
        assert GET_films_request.status_code is 200

    def test_response_body_not_empty(self):
        _response_body = GET_films_request.json()

        assert len(_response_body) > 0

    def test_episode_counter_equal_to_content_list(self):
        _counter = GET_films_request.json()['count']
        _episode_list = [x for x in GET_films_request.json()['results']]

        assert len(_episode_list) == _counter

    @pytest.mark.trylast
    # Test data preparation
    # Episode list from https://en.wikipedia.org/wiki/List_of_Star_Wars_films_and_television_series
    @pytest.mark.parametrize('Episode_in_list',
                             ['A New Hope',
                              'The Empire Strikes Back',
                              'Return of the Jedi',
                              'The Phantom Menace',
                              'Attack of the Clones',
                              'Revenge of the Sith',
                              'The Force Awakens',
                              'The Last Jedi'])
    def test_content_all_epizods_in_list(self, Episode_in_list):
        # In this case we check if all Episodes from SW Wiki is in SWAPI response
        _episode_list = [x['title'] for x in GET_films_request.json()['results']]

        assert Episode_in_list in _episode_list


    # Test data preparation
    # Get Episode name and Episode link from Films page
    @pytest.mark.parametrize('episode_page', [(x['title'], x['url']) for x in GET_films_request.json()['results']])
    def test_episode_link_is_correct(self, episode_page):
        _episode_page = films.FilmPage().GET_one_film(url=episode_page[1])
        # Check repose status
        assert _episode_page.status_code is 200

        # Check Episode correct redirection correct
        assert episode_page[0] == _episode_page.json()['title']
