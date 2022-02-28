# 4u-ps1

Create a file called **zodiac.py** and upload it to this respository. In that file write the following functions:

```
def get_zodiac(date):
    '''(str) -> str
    Takes in a valid str birth date in the form 
    DD-MM-YYYY and returns the corresponding
    zodiac sign.
    >>> get_zodiac('12-11-2005')
    'Scorpio'
    '''
```

```
def get_compatibility(sign1, sign2):
    '''(str, str) -> bool
    Takes in 2 zodiac signs and returns True if they
    are compatible. Two zodiac signs are compatible
    if they belong to the same element.
    Fire: Aries, Leo, Sagittarius
    Earth: Taurus, Virgo, Capricorn
    Air: Gemini, Libra, Aquarius
    Water: Cancer, Scorpio, Pisces
    >>> get_compatibility("Aries", "Sagittarius")
    True
    >>> get_compatibility("Taurus", "Libra")
    False
    '''
```

Create a file called **frequency.py** and upload it to this repository. In that file write the following functions:

```
def most_frequent_helper(letter, lst_of_words):
    '''(str, lst) -> int
    Returns the number of times letter occurs in 
    lst_of_words.
    >>> most_frequent_helper("e", ["apple", "at", "cream", "car", "pea", "special"])
    4
    '''
```

```
def most_frequent(lst_of_words):
    '''(list) -> list
    Given a list of words find the most frequently 
    occuring letter in the list of words. Returns
    a list of the most frequently occuring letters.
    >>> most_frequent(["apple", "at", "cream", "car", "pea", "special"]
    ['a']
    >>> most_frequent(["cream", "special"])
    ['c', 'e', 'a']
    '''
```

In the file **diagonal.py** add the below function and upload it to this repository.

```
def get_diagonals(lst_of_vertices):
    '''Takes in a list of tuples representing coordinates
    of the vertices of a polygon and returns a list
    of diagonals. Adjacent coordinates in the list are joined
    by a side. The first coordinate and the last coordinate
    are joined by a side. Diagonals connect non-adjacent coordinates.
    >>> get_diagonals([(3, 1), (4, -3), (2, 1), (-5, 2)])
    [1.0 ,10.3]
    '''
```
