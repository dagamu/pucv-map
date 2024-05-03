import pygame

def scale_tuple( tuple1 : tuple, scalar : float ):
    result = [ x * scalar for x in [*tuple1] ]
    return result

def sum_tuples( tuple1 : tuple , tuple2 : tuple ):
    result = []
    for i, x in enumerate(tuple1):
        other_value = tuple2[i]
        result.append( x + other_value )
    return result

def alpha_gradient( surface, function ):
    s_size = surface.get_size()
    result = pygame.image.frombytes(pygame.image.tobytes(surface, 'RGBA'), s_size, "RGBA")
    for x in range(s_size[0]):
        for y in range(s_size[1]):
            a = result.get_at((x, y))
            a[3] = pygame.math.clamp( function(x,y), 0, 250 )
            result.set_at((x, y), a)
    return result

def get_rect_polygon( points ):
    
    x = [ p[0] for p in points ]
    y = [ p[1] for p in points ]
    
    w = max(x) - min(x)
    h = max(y) - min(y)
    
    return [ min(x), min(y), w, h ]