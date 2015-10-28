"""
[2015-06-17] Challenge #219 [Intermediate] To-do list (Part 2)
https://tinyurl.com/dp-219-int
"""
import unittest
import sys
sys.path.insert(0, r"C:\code\GitHub\rDP\Easy")

import dp_219_easy

class ToDoCategory(dp_219_easy.ToDoList):
    """To-do class with sorting by category."""
    def __init__(self):
        self.category = {}
    
    def add_item(self, input_list):
        """Adds item to the given category."""
        item = input_list[0]
        # Checks if any non-default categories present  
        if len(input_list) > 1:
            cats_list = [cat for cat in input_list[1:]]
        else:
            cats_list = ['default']
        
        for cat in cats_list:
            
            if cat not in self.category.keys():
                self.category[cat] = []
                
            if item not in self.category[cat]:
                self.category[cat].append(item)
                print('"%s" was added under the category %s' % (item, cat))
            
            else:
                print('"%s" already in the category %s' % (item, cat))
                
    def retrieve_item(cls, command):
        """Retrieves item and categories from the given command"""
        # Doesn't support use of commas and parenthesis in the item
        work_list = [] 
        # Removing function call and parenthesis from user input
        command = command[command.find('(') + 1 : command.find(')')]
        
        if ',' in command:
            work_list = command.split(',')
            
            # Removing leading and trailing spaces
            for index in range(len(work_list)):
                work_list[index].lstrip().rstrip()
        
        else:
            work_list = [command]
            
        return work_list

            
class ToDoCategoryTestCase(unittest.TestCase):
    """Tests for ToDoCategory class methods."""
    
    def test_add_item(self):
        """Tests for add_item method."""
        unit = ToDoCategory()
        
        # Item in default category
        unit.add_item(['default item'])
        self.assertEqual(unit.category['default'], ['default item'])
        
        # Item in custom category
        unit.add_item(['custom item 1', 'cat1', 'cat2'])
        self.assertEqual(unit.category['cat1'], ['custom item 1'])
        self.assertEqual(unit.category['cat2'], ['custom item 1'])
        
        # Add existing item
        unit.add_item(['custom item 1', 'cat1'])
        self.assertEqual(unit.category['cat1'], ['custom item 1'])
        
        # Add additional items to a custom category
        unit.add_item(['custom item 2', 'cat2'])
        self.assertEqual(unit.category['cat2'],
                         ['custom item 1', 'custom item 2'])

    def test_retrieve_item(self):
        """Tests for retrieve_item method"""
        unit = ToDoCategory()
        
        # One item
        self.assertEqual(unit.retrieve_item('addItem("item")'), ["item"])
        
        # Item and category 
        self.assertEqual(unit.retrieve_item('addItem("item" , "cat1")'),
                                            ["item", "cat1"])
                                            
        # Item and multiple categories 
        self.assertEqual(unit.retrieve_item('addItem("item","cat1", "cat2")'),
                                            ["item", "cat1", "cat2"])
                                            
if __name__ == '__main__':
    unittest.main()