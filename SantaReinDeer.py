"""
Happy Holidays fellow Code Warriors!

Now, Dasher! Now, Dancer! Now, Prancer, and Vixen! On, Comet! On, Cupid! On, Donder and Blitzen! That's the order Santa wanted his reindeer...right? What do you mean he wants them in order by their last names!? Looks like we need your help Code Warrior!
Sort Santa's Reindeer

Write a function that accepts a sequence of Reindeer names, and returns a sequence with the Reindeer names sorted by their last names.
Notes:

    It's guaranteed that each string is composed of two words
    In case of two identical last names, keep the original order

Examples

For this input:

[
  "Dasher Tonoyan",
  "Dancer Moore",
  "Prancer Chua",
  "Vixen Hall",
  "Comet Karavani",
  "Cupid Foroutan",
  "Donder Jonker",
  "Blitzen Claus"
]

You should return this output:

[
  "Prancer Chua",
  "Blitzen Claus",
  "Cupid Foroutan",
  "Vixen Hall",
  "Donder Jonker",
  "Comet Karavani",
  "Dancer Moore",
  "Dasher Tonoyan",
]
"""


def sort_reindeer(reindeer_names):
    return sorted(reindeer_names, key=lambda x: sortFn(x))


def sortFn(name):
    sp = name.split(" ")
    return sp[1]


assert(sort_reindeer(['Kenjiro Mori', 'Susumu Tokugawa', 'Juzo Okita', 'Akira Sanada'])==['Kenjiro Mori', 'Juzo Okita', 'Akira Sanada', 'Susumu Tokugawa'])
assert(sort_reindeer([])==[])
assert(sort_reindeer(['Yasuo Kodai', 'Kenjiro Sado', 'Daisuke Aihara', 'Susumu Shima', 'Akira Sanada', 'Yoshikazu Okita', 'Shiro Yabu', 'Sukeharu Nanbu', 'Sakezo Yamamoto', 'Hikozaemon Ohta', 'Juzo Mori', 'Saburo Tokugawa'])==['Daisuke Aihara', 'Yasuo Kodai', 'Juzo Mori', 'Sukeharu Nanbu', 'Hikozaemon Ohta', 'Yoshikazu Okita', 'Kenjiro Sado', 'Akira Sanada', 'Susumu Shima', 'Saburo Tokugawa', 'Shiro Yabu', 'Sakezo Yamamoto'])
assert(sort_reindeer(['Daisuke Mori', 'Shiro Sanada', 'Saburo Shima', 'Juzo Yabu', 'Sukeharu Yamamoto'])==['Daisuke Mori', 'Shiro Sanada', 'Saburo Shima', 'Juzo Yabu', 'Sukeharu Yamamoto'])
assert(sort_reindeer(["Sukeharu Yamamoto", "Juzo Yabu", "Saburo Shima", "Shiro Sanada", "Daisuke Mori"])==['Daisuke Mori', 'Shiro Sanada', 'Saburo Shima', 'Juzo Yabu', 'Sukeharu Yamamoto'])