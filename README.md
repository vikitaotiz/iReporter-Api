# iReporter-API

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

 | Method         | Endpoint               | Description              |
 |----------------|------------------------|--------------------------|
 | Get            | api/v1/incidences      | Gets all incidences      |
 | Get            | api/v1/incidence/1     | Get single a incidence   |
 | Post           | api/v1/incidences      | Creates an incidence     |
 | Put            | api/v1/incidence/1     | Updates an incidence     |
 | Delete         | api/v1/incidence/1     | Deletes single incidence |
