# Author
Lianfeng (Richard) Luo

# Paranuara Challenge
Paranuara is a class-m planet. Those types of planets can support human life, for that reason the president of the Checktoporov decides to send some people to colonise this new planet and
reduce the number of people in their own country. After 10 years, the new president wants to know how the new colony is growing, and wants some information about his citizens. Hence he hired you to build a rest API to provide the desired information.

The government from Paranuara will provide you two json files (located at resource folder) which will provide information about all the citizens in Paranuara (name, age, friends list, fruits and vegetables they like to eat...) and all founded companies on that planet.
Unfortunately, the systems are not that evolved yet, thus you need to clean and organise the data before use.
For example, instead of providing a list of fruits and vegetables their citizens like, they are providing a list of favourite food, and you will need to split that list (please, check below the options for fruits and vegetables).

## New Features
Your API must provides these end points:
- Given a company, the API needs to return all their employees. Provide the appropriate solution if the company does not have any employees.
- Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends in common which have brown eyes and are still alive.
- Given 1 people, provide a list of fruits and vegetables they like. This endpoint must respect this interface for the output: `{"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}`

## Delivery
To deliver your system, you need to send the link on GitHub. Your solution must provide tasks to install dependencies, build the system and run. Solutions that does not fit this criteria **will not be accepted** as a solution. Assume that we have already installed in our environment Java, Ruby, Node.js, Python, MySQL, MongoDB and Redis; any other technologies required must be installed in the install dependencies task. Moreover well tested and designed systems are one of the main criteria of this assessement 

## Evaluation criteria
- Solutions written in Python would be preferred.
- Installation instructions that work.
- During installation, we may use different companies.json or people.json files.
- The API must work.
- Tests

Feel free to reach to your point of contact for clarification if you have any questions.

## Setup

### Installation

1. Install [Docker](https://store.docker.com/search?type=edition&offering=community) and [docker-compose](https://docs.docker.com/compose/install/#install-compose);
2. Use `docker-compose build` to build the docker environment.


### Configuration

Change the private info (database info mostly) in the `.env` file. \
MY_SECRET_KEY can be generate by simply run the `generate.py` file in app directory.\
<b>Note: `.env` provided is used as example.</b> 

### Run
1. Use `docker-compose up` to create and start the docker containers (It may take time to run).
2. Endpoint will be started at http://localhost:9000.


## API description
`1. /api/paranuara/company_employees/<int:company_id>/ (GET)`\
Given a company id, the API returns all their employees info. \
`2. /api/paranuara/special_common_friends/<int:pk1>/<int:pk2>/ (GET)`\
Given 2 people id, the API will provide their information (Name, Age, Address, phone) and the list of their friends in common which have brown eyes and are still alive.\
`3. /api/paranuara/food_info/<int:pk>/ (GET)`\
Given 1 people, the API will provide a list of fruits and vegetables they like.


## License

| Package Name                      | License                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------- |
| Django                            | [BSD](https://github.com/django/django/blob/master/LICENSE)                                 |
| djangorestframework               | [BSD](https://github.com/encode/django-rest-framework/blob/master/LICENSE.md)               |
| django-cors-headers               | [LICENSE](https://github.com/ottoyiu/django-cors-headers/blob/master/LICENSE)               |
| psycopg2-binary |[LICENSE](https://github.com/psycopg/psycopg2/blob/master/LICENSE)|
| django-redis |[LICENSE](https://github.com/niwinz/django-redis/blob/master/LICENSE)|
