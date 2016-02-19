"""
[2016-01-04] Challenge #248 [Easy] Draw Me Like One Of Your Bitmaps
https://tinyurl.com/dp-248-easy
"""

import math

INPUT_FILE = "dp_248_easy_input.txt"
OUTPUT_FILE = "dp_248_easy_output.txt"

def get_dimentions(INPUT_FILE):
    with open(INPUT_FILE, 'r') as input_file:
        bitmap_size = input_file.readline().rstrip()
        num_of_cols = int(bitmap_size.split()[0])
        num_of_rows = int(bitmap_size.split()[1])
        
    return (num_of_cols, num_of_rows)

def make_bitmap(num_of_cols, num_of_rows):
        
    bitmap = dict()
    
    color = "0 0 0"
    
    for row in range(num_of_rows):
        for col in range(num_of_cols):
            bitmap[(row, col)] = color
    
    return bitmap

    
def draw_point (bitmap, row, col, color):
    print("point")
    bitmap[(row, col)] = color

    
def draw_line(bitmap, color, row_st, col_st, row_fin, col_fin):
    
    if row_st == row_fin:
    
        if col_st > col_fin:
            col_st, col_fin = col_fin, col_st
        
        for col in range(col_st, col_fin + 1):
            draw_point(bitmap, row_st, col, color)
    
    else: 
        line_length_sq = ((row_st - row_fin) ** 2 + 
                          (col_st - col_fin) ** 2)
        print("line_length_sq: %s" % line_length_sq) 
                          
        for col in range(0, abs(col_st - col_fin) + 1):
            col = col + 0.5
            row = math.sqrt(line_length_sq - (col ** 2)) - 0.5
            row = math.ceil(row)
            draw_point(bitmap, row, col, color)

            
def draw_rect(bitmap, color, row_st, col_st, row_fin, col_fin):

    if row_st > row_fin:
        row_st, row_fin = row_fin, row_st
        
    if col_st > col_fin:
        col_st, col_fin = col_fin, col_st

    for row in range(row_st, row_fin + 1):
        for col in range(col_st, col_fin + 1):
            draw_point(bitmap, row, col, color)
            

def get_input(bitmap, INPUT_FILE):
    with open(INPUT_FILE, 'r') as file:
        for line in file:
            handle_input(bitmap, line)

def handle_input(bitmap, input_string): 
    
    commands = input_string.rstrip().split()
    
    if "point" in commands:
        color = " ".join(commands[1:4])
        row = int(commands[4])
        col = int(commands[5])
        
        draw_point(bitmap, row, col, color)      
    
    elif "line" in commands or "rect" in commands:
        color = " ".join(commands[1:4])
        row_st = int(commands[4])
        col_st = int(commands[5])
        row_fin = int(commands[6])
        col_fin = int(commands[7])

        if "line" in commands:
            draw_line(bitmap, color, row_st, col_st, row_fin, col_fin)
        elif "rect" in commands:
            draw_rect(bitmap, color, row_st, col_st, row_fin, col_fin)
            
    else: pass

           
def write_output(bitmap, INPUT_FILE, OUTPUT_FILE): 
    bitmap_list = [bitmap[key] for key in sorted(bitmap)]
    
    num_of_cols, num_of_rows = get_dimentions(INPUT_FILE)
        
    with open(OUTPUT_FILE, 'w') as file:
        file.write("P3\n%d %d\n255\n" % (num_of_cols, num_of_rows))
        for row in range(num_of_rows):
            for element in bitmap_list[num_of_cols * row: 
                                   num_of_cols * row + num_of_cols -1]:
                file.writelines(str(element) + " ")
            file.writelines("\n")
        

    
if __name__ == '__main__':
    dimentions = get_dimentions(INPUT_FILE)
    bitmap = make_bitmap(dimentions[0], dimentions[1])
    
    get_input(bitmap, INPUT_FILE)
    write_output(bitmap, INPUT_FILE, OUTPUT_FILE)