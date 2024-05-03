from option import Option


class Menu:
    """
    Each Menu instance represents a list of options.  Each option is just
    a prompt, and an action (text string) to take if that option is selected.
    Each prompt has exactly one corresponding action.  The text of the action
    is returned, with the expectation that the calling routine will use the
    Python exec function to perform the user-selected action.
    """
    def __init__(self, name: str, prompt: str, options: [Option]):
        # A descriptive name of the menu.  No uniqueness is enforced.
        self.name = name
        # The prompt to show at the top of the menu each time it is displayed.
        self.prompt = prompt
        # The list of options for the user to choose from.
        self.options = options

    def menu_prompt(self) -> str:
        """
        Display the available options and their results and prompt the user for which
        option they will take.
        :return:        The text to be executed in the calling function.
        """
        results: bool = False                   # Flag to show if we are done
        final: int = -1                         # The chosen option
        n_options: int = len(self.options)      # Find the total number of options
        while not results:                      # Loop until user makes valid entry
            print(self.prompt)                  # Display the menu prompt
            index: int = 0                      # Option counter for display purposes
            for option in self.options:         # Show the list of options
                index += 1                      # Remember which option we're showing
                print("%3d - %s" % (index, option.get_prompt()))
            try:                                # Protect from non-integer input
                final = int(input('-->'))
                if final < 1 or final > n_options:  # Protect from out of range input
                    print("Choice is out of range, try again.")
                    results = False
                else:
                    results = True
            except ValueError:
                print("Not a valid integer, try again.")
        return self.options[final - 1].get_action()

    def last_action(self):
        """
        Find the last action in the menu.  By convention, this is the
        option that exits from this menu.  It does not have to be literally
        "exit", it could be any operation, including "pass".  But it
        signifies that the user has elected to quit.  At least so goes
        the normal convention.
        :return:    The text of the very last action in the options list.
        """
        return self.options[len(self.options) - 1].get_action()
