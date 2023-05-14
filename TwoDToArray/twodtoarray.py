"""
Create a function that takes an array of letters, and combines them into words in a sentence.

The array will be formatted as so:

[
  ['J','L','L','M'],
  ['u','i','i','a'],
  ['s','v','f','n'],
  ['t','e','e','']
]
The function should combine all the 0th indexed letters to create the word 'just', all the 1st indexed letters to create the word 'live', etc.

Shorter words will have an empty string in the place once the word has already been mapped out (see the last element in the last element in the array).

Examples:

[
  ['J','L','L','M'],
  ['u','i','i','a'],
  ['s','v','f','n'],
  ['t','e','e','']
] // => "Just Live Life Man"

[ 
  [ 'T', 'M', 'i', 't', 'p', 'o', 't', 'c' ],
  [ 'h', 'i', 's', 'h', 'o', 'f', 'h', 'e' ],
  [ 'e', 't', '', 'e', 'w', '', 'e', 'l' ],
  [ '', 'o', '', '', 'e', '', '', 'l' ],
  [ '', 'c', '', '', 'r', '', '', '' ],
  [ '', 'h', '', '', 'h', '', '', '' ],
  [ '', 'o', '', '', 'o', '', '', '' ],
  [ '', 'n', '', '', 'u', '', '', '' ],
  [ '', 'd', '', '', 's', '', '', '' ],
  [ '', 'r', '', '', 'e', '', '', '' ],
  [ '', 'i', '', '', '', '', '', '' ],
  [ '', 'a', '', '', '', '', '', '' ]
] // => "The Mitochondria is the powerhouse of the cell"


"""
def arr_adder2(arr):
    res=[]
    for i in range(0,len(arr[0])):
        temp=""
        for j in range(0,len(arr)):
            temp=temp+arr[j][i]
        res.append(temp)
    print (res)
    return " ".join(res) 

def arr_adder(arr):
    from itertools import product
    res=[]
    for i,j in product(range(0,len(arr[0])), range(0,len(arr)) ):
        if(j==0):temp=""
        temp=temp+arr[j][i]
        if(j==len(arr)-1):res.append(temp)
    print (res)
    return " ".join(res)  


assert(arr_adder([
        ['J','L','L','M'],
        ['u','i','i','a'],
        ['s','v','f','n'],
        ['t','e','e','' ]
    ])=="Just Live Life Man")


assert(arr_adder([
    ['T','M','i','t','p','o','t','c'],
    ['h','i','s','h','o','f','h','e'],
    ['e','t','', 'e','w','', 'e','l'],
    ['', 'o','', '', 'e','', '', 'l'],
    ['', 'c','', '', 'r','', '', '' ],
    ['', 'h','', '', 'h','', '', '' ],
    ['', 'o','', '', 'o','', '', '' ],
    ['', 'n','', '', 'u','', '', '' ],
    ['', 'd','', '', 's','', '', '' ],
    ['', 'r','', '', 'e','', '', '' ],
    ['', 'i','', '', '', '', '', '' ],
    ['', 'a','', '', '', '', '', '' ]
])== "The Mitochondria is the powerhouse of the cell");
