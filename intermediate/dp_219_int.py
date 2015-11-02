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
        self.category = dict()


    def call_function(self, command):
        """Calls specific function depending on the user input."""

        if 'add' in command:
            self.add_item(self.retrieve_item(command))

        elif 'delete' in command:
            self.delete_item(self.retrieve_item(command))

        elif 'update' in command:
            self.update_item(self.retrieve_item(command))

        elif 'view' in command:
            self.view_list(self.retrieve_item(command))

        elif 'help' in command:
            self.help()

        else:
            print('ERROR: Unknown command.')


    def retrieve_item(cls, command):
        """Retrieves item and categories from the given command"""
        # Doesn't support use of commas and parenthesis in the item
        work_list = list()
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


    def add_item(self, work_list):
        """Adds item to the given category."""
        item = work_list[0]
        if len(work_list) > 1:
            cats_list = work_list[1:]
        else:
            cats_list = ['default']

        for cat in cats_list:

            if cat not in self.category.keys():
                self.category[cat] = list()

            if item not in self.category[cat]:
                self.category[cat].append(item)
                print('"%s" was added under the category %s' % (item, cat))

            else:
                print('"%s" already in the category %s' % (item, cat))


    def delete_item(self, work_list):
        """Deletes item from a category."""
        item = work_list[0]
        # Checks if item in the To-do list
        for cat in self.category:
            if item in self.category[cat]:
                break
        else:
            print("'%s' not in the list" % item)
            return

        if len(work_list) > 1:
            cats_list = work_list[1:]
        else:
            cats_list = list(self.category.keys())

        for cat in self.category:
            if cat in cats_list:
                try:
                    self.category[cat].remove(item)
                except ValueError:
                    pass

        # Removes empty categories from self.category
        for cat in list(self.category):
            if not self.category[cat]:
                del self.category[cat]


    def update_item(self, work_list):
        """Updates given item."""
        length = len(work_list)

        if length >= 2:
            item = work_list[0]
            new_item = work_list[1]
        else:
            print('Invalid input. Need at least two items')

        if length > 2:
            cats_list = work_list[2:]
        else:
            cats_list = list(self.category.keys())

        for cat in cats_list:
            if item in self.category[cat]:
                ind = self.category[cat].index(item)
                self.category[cat][ind] = new_item


    def view_list(self, work_list):
        """Shows categories and items in them."""
        if work_list == ['']:
            cats_list = list(self.category.keys())
        else:
            cats_list = work_list[:]

        if not cats_list:
            print('To-do list is empty')
            return

        cats_list.sort()

        for cat in cats_list:
            print('\n', '-' * 4, cat, '-' * 4)

            try:
                for item in self.category[cat]:
                    print('- ', item)
            except KeyError:
                print('Category "%s" is not in To-do list' % cat)

    def help(self):
        """Provides help for the user."""
        print('addItem():')
        print('\t', self.add_item.__doc__)
        print('deleteItem():')
        print('\t', self.delete_item.__doc__)
        print('updateItem():')
        print('\t', self.update_item.__doc__)
        print('viewList():')
        print('\t', self.view_list.__doc__)


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

        # Empty command
        self.assertEqual(unit.retrieve_item('viewItems()'), [''])

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
        self.assertTrue(unit.category == {})

        # Delete item from specific categories
        unit.add_item(['item1', 'cat1', 'cat2', 'cat3', 'cat4'])
        unit.delete_item(['item1', 'cat1', 'cat3'])
        self.assertTrue(unit.category ==
                        {'cat2': ['item1'], 'cat4': ['item1']})

        # Trying to delete item that is not in the list
        # Don't know how to check this case
        # unit.delete_item(['item3'])
        # self.assertRaises(ValueError, unit.delete_item(), ['item3'])

        # Delete item from all categories
        unit.add_item(['item2', 'cat3', 'cat2'])
        unit.delete_item(['item1', 'cat4'])
        self.assertTrue(unit.category ==
                        {'cat2': ['item1', 'item2'], 'cat3': ['item2']})

        unit.delete_item(['item2'])
        self.assertTrue(unit.category == {'cat2': ['item1']})


    def test_update_item(self):
        """Tests for update_item method."""
        unit = ToDoCategory()

        # Update item
        unit.add_item(['item1'])
        unit.add_item(['item2', 'cat1', 'cat2'])

        unit.update_item(['item1', 'new_item_1'])
        self.assertTrue(unit.category['default'] == ['new_item_1'])

        unit.update_item(['item2', 'new_item_2', 'cat2'])
        self.assertTrue(unit.category['cat1'] == ['item2'] and
                        unit.category['cat2'] == ['new_item_2'])



if __name__ == '__main__':
    #unittest.main()
    start_to_do_list = ToDoCategory()
    start_to_do_list.user_input()
