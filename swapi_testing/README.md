<h1>Hello! </h1>
This is SWAPI (https://swapi.co/) API testing by Python 
<li>We are using Python3.6</li>
<li>pytest adn pytest-html module for reporting </li>
<li> a timer decorator implemented in /tests/conftes.py module as a fixture running with each method (test) in ckass,
This is some Pytest magic ... </li>
<li> Alos, I uses 'pytest.mark.parametrize' fixture to generate test data and run same test case for each data pair </li>

<h2> Run test </h2>
<li> User Linux or *Unix with Python3 re-installed </li>
<li> Run ./test_all.sh to lunch all tests tugether </li>
<li> Run ./test_fims.sh test_people.sh for Fims and People tests</li>

<h2> Test Cases </h2>
I made only some core tests like response code, response_body, etc.
I also check if it's possible to /modify /delete the record; check if data is correct, etc ... 
<br>My typecall scenario is:
<li> Smoke test</li>
<li> positive functional test</li>
<li> regression test/li>
<li> negative test/li>

<h3> Films (episodes) </h3>
<li> Check status code </li>
<li> Check response body not empty</li>
<li> Check All Episodes in reponse list</li>
<li> Check Episode url is avalaible and liead to defined page</li>

<h3> People (episodes) </h3>
<li> Check All Episodes in reponse list</li>
<li> Check response body not empty</li>
<li> Check Poeple url is avalaible and liead to defined page</li>
+ In this case we can test if each link is avalalble and data is correct ...

