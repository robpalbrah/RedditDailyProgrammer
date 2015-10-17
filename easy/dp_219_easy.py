"""
[2015-06-15] Challenge #218 [Easy] To-do list (Part 1)
https://tinyurl.com/rDP-219-Easy
"""

class ToDoList():
    """Creates a To-do list."""
    def __init__(self):
        self.to_do_list = []


    def user_input(self):
        """Handles user input and exit() command."""
        print("Welcome to the 'To-do list.'")
        print("Type help() for more information.")
        print("Type exit() to leave.")

        while True:
            try:
                commands = input('>')
            except EOFError:
                pass

            if ';' in commands:
                list_of_commands = commands.split(';')
            else:
                list_of_commands = [commands]

            for command in list_of_commands:
                if len(command) == 0 or command.isspace():
                    list_of_commands.remove(command)

            for command in list_of_commands:
                if 'exit' in command:
                    return None
                else:
                    self.call_function(command)


    def call_function(self, command):
        """Calls specific function depending on the user input."""

        if 'add' in command:
            self.add_item(self.retrieve_item(command))

        elif 'delete' in command:
            self.delete_item(self.retrieve_item(command))

        elif 'view' in command:
            self.view_list()

        elif 'help' in command:
            self.help()

        else:
            print('ERROR: Unknown command.')


    def add_item(self, item):
        """Adds item to the list."""
        if item not in self.to_do_list:
            self.to_do_list.append(item)
            print('%s was added to the list.' % item)
        else:
            print('%s already in the list' %item)


    def delete_item(self, item):
        """Deletes item from the list."""
        try:
            self.to_do_list.remove(item)
            print('%s was removed from the list.' % item)
        except ValueError:
            print('ERROR: %s is not in the list' % item)


    def view_list(self):
        """Shows all items in the list."""
        if self.to_do_list:
            print('To-do list:')
            for index, item in enumerate(self.to_do_list, start=1):
                print(index, item)
        else:
            print('To-do list is empty.')

    @classmethod
    def retrieve_item(cls, command):
        """Retrieves item in parenthesis from a given command"""
        item = command[command.find('(') + 2 : -2]
        return item


    def help(self):
        """Provides help for the user."""
        print('addItem():')
        print('\t', self.add_item.__doc__)
        print('deleteItem():')
        print('\t', self.delete_item.__doc__)
        print('viewList():')
        print('\t', self.view_list.__doc__)
        return None


if __name__ == '__main__':
    start_to_do_list = ToDoList()
    start_to_do_list.user_input()
    