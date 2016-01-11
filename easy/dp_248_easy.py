"""
[2016-01-04] Challenge #248 [Easy] Draw Me Like One Of Your Bitmaps
https://tinyurl.com/dp-248-easy
"""

import math

INPUT_FILE = "dp_248_easy_input.txt"
OUTPUT_FILE = "dp_248_easy_output.txt"

def make_bitmap(number_of_rows, number_of_columns, color = "0 0 0"):

    bitmap = dict()
    
    for row in range(number_of_rows):
        for column in range(number_of_columns):
            bitmap[(row, column)] = color
    
    return bitmap

    
def draw_point (bitmap, row, column, color):
    bitmap[(row, column)] = color

    
def draw_line(bitmap, color, row_st, col_st, row_fin, col_fin):

    if row_st == row_fin:
        for col in range(col_st, col_fin + 1):
            draw_point(bitmap, row_st, col, color)
    else: 
        line_length_sq = ((row_st - row_fin) ** 2 + 
                          (col_st - col_fin) ** 2)
                          
        for col in range(col_st + 0.5, (col_fin + 0.5) + 1):
            
            row = math.sqrt(line_length_sq - col ** 2) - 0.5
            row = math.ceil(row)
            
            draw_point(bitmap, row, column, color)

            
def draw_rect(bitmap, color, row_st, col_st, row_fin, col_fin):
    for row in range(row_st, row_fin + 1):
        for col in range(col_st, col_fin + 1):
            draw_point(bitmap, row, col, color)
            

def get_input() : pass
def handle_input(): pass 
def write_output(): pass