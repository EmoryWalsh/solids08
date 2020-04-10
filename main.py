from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
zbuffer = new_zbuffer()
color = [ 255, 255, 255 ]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]


parse_file( 'newscript', edges, polygons, csystems, screen, zbuffer, color )
#print_matrix(zbuffer)
