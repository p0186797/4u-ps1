import math

def distance(coord1, coord2):
    '''((float, float), (float, float)) -> float
    Returns the distance between coord1 and coord2 
    where coord1 and coord2 are both a tuple of floats
    representing coordinates. Round the distance 
    to one decimal place.'''

    x1, y1 = coord1
    x2, y2 = coord2
    return round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 1)

def get_diagonals(lst_of_vertices):
    '''Takes in a list of tuples representing coordinates
    of the vertices of a polygon and returns a list
    of diagonals. Adjacent coordinates in the list are joined
    by a side. The first coordinate and the last coordinate
    are joined by a side. Diagonals connect non-adjacent coordinates.
    >>> get_diagonals([(3, 1), (4, -3), (2, 1), (-5, 2)])
    [1.0 ,10.3]
    '''
