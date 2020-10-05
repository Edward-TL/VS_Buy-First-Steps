# All of them are made because the None case in numpy.
# In numpy, this raise an error, and in this case, that's not the case

def mean(array):
    summatory = 0
    n = 0
    for x in array:
        if x != None:
            summatory = summatory + x
            n += 1
    return summatory/n

def variance(array):
    average =  mean(array)
    s_sum = 0
    for x in array:
        if x != None:
            dif = x - average
            s_dif = dif**2
            s_sum = s_sum + s_dif
    n = len(array)

    return s_sum/n

# Standar desviation
def std(array):
    var = variance(array)
    
    return var**(1/2)

def max_with_none(array):
    if len(array) > 0 or array != None:
        max = 0
        for x in array:
            if x != None:
                if max < x:
                    max = x
        return max
    else:
        print(f"Risk with array: {array}, sending 'None' value")
        return None

def min_with_none(array):
    try:
        if len(array) > 0:
            n = 0
            min = None
            while min == None and n < len(array):
                min = array[n]
                n += 1
                
            for x in array:
                if x != None and min != None:
                    if x < min:
                        min = x
            return min

        else:
            print(f"Risk with array: {array}, sending '0' value")
            return 0
    except TypeError:
        raise TypeError(f"TypeError: object of type 'float' has no len() {array}")

def max_and_min(array):
    max = 0
    min = None
    n = 0
    while min == None and n < len(array):
        min = array[n]
        n += 1

    for x in array:
        if x != None:
            try:
                if max < x:
                    max = x
            except:
                max_error = f"'<' not supported between instances of 'float' and 'NoneType'. max = {max} | x = {x}"
                raise TypeError(max_error)
            try:
                if x < min:
                    min = x
            except:
                min_error = f"'<' not supported between instances of 'float' and 'NoneType'. x = {x} | min = {min}"
                raise TypeError(min_error)

    return max, min