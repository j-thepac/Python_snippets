"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases.

docker:
docker run -it --name likes -v $PWD:/home/app -w /home/app -p 5000:5000 python:3.9-slim python likes.py

docker build -t likes:v1 .
docker-compose up

"""
def likes(names):
    if(len(names)==0):return 'no one likes this'
    elif(len(names)==1):return '{} likes this'.format(names[0])
    elif(len(names)==2):return '{} and {} like this'.format(names[0],names[1])
    elif(len(names)==3):return '{}, {} and {} like this'.format(names[0],names[1],names[2])
    else:
        return '{}, {} and {} others like this'.format(names[0],names[1],len(names)-2)

assert(likes([])== 'no one likes this')
assert(likes(['Peter'])== 'Peter likes this')
assert(likes(['Jacob', 'Alex'])== 'Jacob and Alex like this')
assert(likes(['Max', 'John', 'Mark'])== 'Max, John and Mark like this')
assert(likes(['Alex', 'Jacob', 'Mark', 'Max'])== 'Alex, Jacob and 2 others like this')

print("done")