"""
You will be given an array of objects representing data about developers who have signed up to attend the next coding meetup that you are organising.

Given the following input array:

list1 = [
  { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 22, 'language': 'JavaScript', 'githubAdmin': 'yes' },
  { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 49, 'language': 'Ruby', 'githubAdmin': 'no' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 34, 'language': 'JavaScript', 'githubAdmin': 'yes' },
  { 'firstName': 'Piotr', 'lastName': 'B.', 'country': 'Poland', 'continent': 'Europe', 'age': 128, 'language': 'JavaScript', 'githubAdmin': 'no' }
  ]
write a function that when executed as findAdmin(list1, 'JavaScript') returns only the JavaScript developers who are GitHub admins:

[
  { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 22, 'language': 'JavaScript', 'githubAdmin': 'yes' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 34, 'language': 'JavaScript', 'githubAdmin': 'yes' }
]
Notes:

The original order should be preserved.
If there are no GitHub admin developers in a given language then return an empty array [].
The input array will always be valid and formatted as in the example above.
The strings representing whether someone is a GitHub admin will always be formatted as 'yes' and 'no' (all lower-case).
The strings representing a given language will always be formatted in the same way (e.g. 'JavaScript' will always be formatted with upper-case 'J' and 'S'.


docker:
docker run -it --name gitadmin -v $PWD:/home/app -w /home/app python:3.8-slim python GitAdmin.py

dockerbuild
 docker build -t gitadmin:v1 .
 docker run -it 1386bd18d973

docker-compose up
"""

class Person:
    def __init__(self,firstName,lastName,country,continent,age,language,githubAdmin):
        self.firstName=firstName
        self.lastName = lastName
        self.country = country
        self.continent = continent
        self.age = age
        self.language = language
        self.githubAdmin = githubAdmin


def find_admin(lst, lang):
    persons=[Person(**prop) for prop in lst]
    filteredResult =list(filter(lambda person: person.githubAdmin=="yes" and person.language==lang ,persons))
    result= list(map(lambda person:person.__dict__,filteredResult))
    return result


list1 = [
    {'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 22,
     'language': 'JavaScript', 'githubAdmin': 'yes'},
    {'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 49,
     'language': 'Ruby', 'githubAdmin': 'no'},
    {'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 34,
     'language': 'JavaScript', 'githubAdmin': 'yes'},
    {'firstName': 'Piotr', 'lastName': 'B.', 'country': 'Poland', 'continent': 'Europe', 'age': 128,
     'language': 'JavaScript', 'githubAdmin': 'no'}
]

answer1 = [
    {'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 22,
     'language': 'JavaScript', 'githubAdmin': 'yes'},
    {'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 34,
     'language': 'JavaScript', 'githubAdmin': 'yes'}
]



assert(find_admin(list1, 'JavaScript') ==answer1)
print("done")