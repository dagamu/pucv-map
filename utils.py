def scale_tuple( tuple1 : tuple, scalar : float ):
    result = [ x * scalar for x in [*tuple1] ]
    return result

def sum_tuples( tuple1 : tuple , tuple2 : tuple ):
    result = []
    for i, x in enumerate(tuple1):
        other_value = tuple2[i]
        result.append( x + other_value )
    return result