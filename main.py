#from colours import *

def kto255(r:int, g:int, b:int):
    if r not in range(0, 255):
        raise ValueError(f’r not in range 0-255. r = {r}’)
    elif g not in range(0, 255):
        raise ValueError(f’g not in range 0-255. g = {g}’)
    elif b not in range(0, 255):
        raise ValueError(f’b not in range 0-255. b = {b}’)
    
    if r == 0 and g == 0 and b == 0:
        raise ValueError(‘Cannot process perfect black’)
    elif r >= g:
        if r >= b:
            if r != 0:
                k = (r/255)
    elif g >= r:
        if g >= b:
            if g != 0:
                k = (g/255)
    elif b >= r:
        if b >= g:
            if b != 0:
                k = (b/255)
    return(r: uniform(r/k), g: uniform(g/k), b: uniform(b/k))
    
def mto255(r:int, g:int, b:int):
    if r not in range(0, 255):
        raise ValueError(f’r not in range 0-255. r = {r}’)
    elif g not in range(0, 255):
        raise ValueError(f’g not in range 0-255. g = {g}’)
    elif b not in range(0, 255):
        raise ValueError(f’b not in range 0-255. b = {b}’)
        
    if r == 0 and g == 0 and b == 0:
        raise ValueError(‘Cannot process perfect black’)
    elif r >= g:
        if r >= b:
            if r != 0:
                m = (255-r)
    elif g >= r:
        if g >= b:
            if g != 0:
                m = (255-r)
    elif b >= r:
        if b >= g:
            if b != 0:
                m = (255-b)
    return(r: uniform(r+m), g: uniform(g+m), b: uniform(b+m))