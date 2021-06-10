######################
# Required Questions #
######################

# Lambdas

def compose(f, g):
    """Write a function that takes in 2 single-argument functions, f and g, and returns another lambda function 
    that takes in a single argument x. The returned function should return the output of applying f(g(x)). 
    Hint: The staff solution is only 1 line!

    Return the composition function which given x, computes f(g(x)). 

    >>> add_two = lambda x: x + 2  		# adds 2 to x
    >>> square = lambda x: x ** 2 		# squares x
    >>> a = compose(square, add_two) 	# (x + 2 ) ^ 2
    >>> a(5) 
    49
    >>> mul_ten = lambda x: x * 10 		# multiplies 10 with x
    >>> b = compose(mul_ten, a) 		# ((x + 2 ) ^ 2) * 10
    >>> b(5)
    490
    >>> b(2)
    160
    """
    func = lambda f: lambda g: lambda x: f(g(x))
    return func(f)(g)
    


def mul_by_num(num):
    """
    Returns a function that takes one argument and returns num
    times that argument.
    >>> x = mul_by_num(5)
    >>> y = mul_by_num(2)
    >>> x(3)
    15
    >>> y(-4)
    -8
    """
    func = lambda f: lambda x: num*x
    return func(x)
    


## Data Abstraction


# Treat all the following code as being behind an abstraction layer, you shouldn't need to look at it!

def make_city(name, lat, lon):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    >>> get_lat(city)
    0
    >>> get_lon(city)
    1
    """
    if change_abstraction.changed:
        return {"name" : name, "lat" : lat, "lon" : lon}
    else:
        return [name, lat, lon]

def get_name(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    """
    if change_abstraction.changed:
        return city["name"]
    else:
        return city[0]

def get_lat(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lat(city)
    0
    """
    if change_abstraction.changed:
        return city["lat"]
    else:
        return city[1]

def get_lon(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lon(city)
    1
    """
    if change_abstraction.changed:
        return city["lon"]
    else:
        return city[2]

def change_abstraction(change):
    change_abstraction.changed = change

change_abstraction.changed = False


from math import sqrt
def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    return sqrt( (get_lat(city_1) - get_lat(city_2))**2 + (get_lon(city_1) - get_lon(city_2))**2 )

def closer_city(lat, lon, city1, city2):
    """
    Returns the name of either city1 or city2, whichever is closest to
    coordinate (lat, lon).

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    dist_adv1 = sqrt((get_lat(city_1) - lat)**2 + (get_lon(city_1) - lon)**2)
    dist_adv2 = sqrt((get_lat(city_2) - lat)**2 + (get_lon(city_2) - lon)**2)
    
    if dist_adv1 > dist_adv2:
        return get_name(city2)
    elif dist_adv1 == dist_adv2:
        return
    else:
        return get_name(city1)

def check_abstraction():
    """
    There's nothing for you to do for this function, it's just here for the extra doctest
    >>> change_abstraction(True)
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    >>> change_abstraction(False)
    """


## Dictionaries

def counter(message):
    """ Returns a dictionary of each word in message mapped
    to the number of times it appears in the input string.

    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    word_list = message.split()
    diction = dict()
    for word in message.split():
        diction[word] = 0
        
    for char in message.split():
        diction[char] += 1
    return diction

# Required Practice Problems.
def lab04_practice_problems():
  """
  Fill in the values for these two variables.
  You will get the special code from the study tool when you complete all questions from lab.
  This code will be unique to your okpy email and this lab.
  Go here to practice: https://codestyle.herokuapp.com/cs88/lab04
  """
  okpy_email = "my_examil@berkeley.edu"
  practice_result_code = "xxxx...xxxxx"
  return (okpy_email, practice_result_code)
