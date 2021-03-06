# iReporter-API  [![Build Status](https://travis-ci.org/vikitaotiz/iReporter-Api.svg?branch=Develop)](https://travis-ci.org/vikitaotiz/iReporter-Api) [![Coverage Status](https://coveralls.io/repos/github/vikitaotiz/iReporter-Api/badge.svg?branch=Develop)](https://coveralls.io/github/vikitaotiz/iReporter-Api?branch=Develop) <a href="https://codeclimate.com/github/vikitaotiz/iReporter-Api/maintainability"><img src="https://api.codeclimate.com/v1/badges/ed442f4546f8461aa8af/maintainability" /></a>

Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention

***How to manually test***
- $ pip install virtualenv
- NB This install virtualenv Globally(virtual environment allows you to create independent environment isolated from your actual physical machine)
- $ virtualenv -p python3 env
- $ source env/Scripts/activate
- Clone this repository: https://github.com/vikitaotiz/iReporter-Api.git
- navigate into the repository after cloning
- $ git checkout Develop to switch from master to this branch
- $ pip install -r requirements.txt
- $ python run.py

# Endpoints are

 | Method         | Endpoint                | Description              |
 |----------------|-------------------------|--------------------------|
 | Get            | api/v1/incidences       | Gets all incidences      |
 | Get            | api/v1/incidences/1     | Get a single incidence   |
 | Post           | api/v1/incidences       | Creates an incidence     |
 | Put            | api/v1/incidences/1     | Updates an incidence     |
 | Delete         | api/v1/incidences/1     | Deletes single incidence |
 | Post           | api/v1/incidences/login | Logins in a user         |
 | Post           | api/v1/incidences/register | Creates a user        |


#
# Heroku
[View It Here](https://ireporter-app-api.herokuapp.com/api/v1/incidences)
# Author
Victor Otieno
# Licence
MIT
