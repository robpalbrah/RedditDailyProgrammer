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
    
    def add_item(self, work_list):
        """Adds item to the given category."""
        item = work_list[0]
        cats_list = check_categories(work_list)        
        
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
                work_list[index] = work_list[index].lstrip().rstrip()
                work_list[index] = work_list[index].replace('"', '')
        
        else:
            work_list = [command.replace('"', '')]
            
        return work_list

    def delete_item(work_list):
        """Deletes item from a category."""
        
    def check_categories(work_list):
        """Checks if any non-default categories present"""
        if len(work_list) > 1:
            cats_list = [cat for cat in work_list[1:]]
        else:
            cats_list = ['default']
        return cats_list    

        
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
        
    def test_delete_item(self):
        """Tests for delete_item method."""
        unit = ToDoCategory()
        
        # Delete item from default category
        unit.add_item(['item'])
        unit.delete_item(['item'])
        self.assertTrue(unit.categories == {})
        
        # Delete item from specific categories
        unit.add_item(['item1', 'cat1', 'cat2', 'cat3', 'cat4'])
        unit.delete(['item1', 'cat1', 'cat3'])
        self.assertTrue(unit.categories == 
                        {'cat2': ['item1'], 'cat4': ['item1']})

        # Delete item from all categories                         
        unit.add_item(['item2', 'cat3', 'cat2'])
        unit.delete_item(['item1', 'cat4'])
        self.assertTrue(unit.categories ==
                        {'cat2': ['item1', 'item2'], 'cat3': ['item2']})
                        
        unit.delete_item(['item2'])
        self.assertTrue(unit.categories == {'cat2': ['item1']})
        
        # Trying to delete item that is not in the list 
        unit.delete_item(['item3'])
        self.assertRaises(ValueError, unit.delete_item(), ['item3']) 
        
        
if __name__ == '__main__':
    unittest.main()