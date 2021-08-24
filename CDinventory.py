#------------------------------------------#
# Title: CDinventory.py
# Desc: Created a file to 
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Larkin, 2021-Aug-15, Edited File, converted to structure format
# Larkin, 2021-Aug-23, Edited File, added Error handling, pickling
#------------------------------------------#

# -- DATA -- #
import pickle

strChoice = '' # User input
dicTbl = []  # list of dicationaries to hold data
dicRow = {}  # dictionary of data row
strFileName = 'CDInventory.dat'  # data storage file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:
    '''Adding and deleting items from the CD inventory table stored during run time'''
    # TODone add functions for processing here

    @staticmethod
    def add_CD(cdID, title, artist, table):
        '''Function to add CD to 2D table, list of dics
        Args:
            cdID (string): string to add to dictionary
            title (string): string to add to dictionary
            artist (string): string to add to dictionary
            table (list of Dics): Table of dics to add new dictionary to
        Returns:
            table (list of Dics): Table with added CD
        '''
       
        dicRow = {'ID': cdID, 'Title': title, 'Artist': artist}
        if table[0]['ID'] == None:
            table = [dicRow]
        else: 
            table.append(dicRow)
        return table
        
    @staticmethod
    def delete_CD(cdID, table):
        '''Function to delete CD in ED table, list of dics
        Args:
            cdID (Integer): ID number for CD in dictionary to delete from table
            table (list of dics): Table of dictionaries to delete dic from
        Returns:
            blnCDRemoved (boolean): Boolean to allow program to know if CD was deleted
            table (list of dics): updated table after CD deletion
        '''
        intRowNr = -1
        blnCDRemoved = False
        if table[0]['ID'] == None:
            blnCDRemoved = False
        else: 
            
            for row in table:
                intRowNr += 1
                if int(row['ID']) == cdID:
                    if len(table) == 1:
                        data = {'ID': None, 'Title': None, 'Artist': None}
                        table.append(data)
                    del table[intRowNr]
                    blnCDRemoved = True
                    break
        return blnCDRemoved, table
    
    @staticmethod
    def sort_CD(table):
        '''Function to sort list of dictionarires
        Args:
            table (list of dictionaries): List of CDs to be sorted
        Returns:
            sorted_table (list of dictionaries): sorted list of CDs'''
        if table[0]['ID'] == None:
            sorted_table = table 
        else:
            sorted_table = sorted(table, key = lambda i: i['ID'])
        return sorted_table
    
    @staticmethod
    def compare_CD(cdID, table):
        '''Function to compare new CD ID with existing IDs
        Args:
            cdID (integer): ID of CD to be added
            table (list of dics): Table of existing CDs
        Returns:
            cdID (integer): returns CD ID once it is unique
        '''
        print(table[0]['ID'])
        if table[0]['ID'] == None:
            print('There are no CDs to compare.')
        else:
            boolean = True
            while boolean:
                for i in range(len(table)):
                    j = table[i]['ID']
                    if j == cdID:
                        boolean2 = True
                        while boolean2:
                            try:
                                cdID = int(input('CD ID ' + str(cdID) + ' already exists, input a unique CD ID: '))
                                boolean2 = False
                            except ValueError as e:
                                print('The following error was encountered:', e)
                                print('The CD ID must be a number.')
                    elif i == len(table) - 1:
                        boolean = False
        return cdID

class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to retrieve and unserialize data from saved file

       Accesses and unserializes data from a data file

        Args:
            file_name (string): name of file used to get data from 
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            dataTbl (list of dictionaries): Holds CD file inputs
        """
        table.clear()  # this clears existing data and allows to load data from file
        try: 
            with open(file_name, 'rb') as file:
                dataTbl = pickle.load(file)
        except FileNotFoundError as e:
            print('The following error was encountered:', e)
            with open(file_name, 'wb') as file:
                print(file_name, 'has been created!')
                data = [{'ID': None, 'Title': None, 'Artist': None}]
                pickle.dump(data, file)
                dataTbl = data
        return dataTbl

    @staticmethod
    def write_file(file_name, table):
        '''Function to save serialized user data to a file using the pickle function
        
        Serializes object that is entered into table
        
        Args: 
            file_name: Name of file to save serialized table to 
            table: 2D data structure (list of dictionaries) that holds data during run time
        Returns:
            None.
        '''
        # TODone Add code here
    
        with open(file_name, 'wb') as file:
            pickle.dump(table, file)
            

# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x
        """
        choice = ''
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        #print('\n')  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('\n======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        if table[0]['ID'] == None:
             print()
        else: 
            for row in table:
                print('{}\t{} (by: {})'.format(*row.values()))
        print('======================================\n')

    # TODone add I/O functions as needed
    @staticmethod
    def input_CD():
        '''Get user input for CD to add
        Args:
            None
        Returns:
            strID (integer): string of user input for new CD ID
            strTitle (string): string with user input for new CD title
            strArtist (string): string with user input for new CD artist
            '''
        boolean = True
        while boolean:
            try:
                cdID = int(input('What is the CD\'s ID? ').strip())
                boolean = False
            except ValueError as e:
                print('The following error was encountered:', e)
                print('The CD ID must be a number.')
        title = input('What is the CD\'s title? ').strip()
        artist = input('What is the Artist\'s name? ').strip()
        return cdID, title, artist
    
    @staticmethod
    def input_ID(table):
        '''Function to get CD ID for deleted CD
        Args:
            table (list of dics): to test if inital value is None
        Returns:
            intIDDel (integer): number of ID to delete
        '''
        if table[0]['ID'] == None:
            print('There are no CDs to remove.\n')
            intIDDel = 0
        else: 
            boolean = True
            while boolean:
                try:
                    intIDDel = int(input('Which ID would you like to delete? ').strip())
                    boolean = False
                except ValueError as e:
                    print('The following error was encountered:', e)
                    print('The CD ID must be a number.')
        return intIDDel
    
    @staticmethod
    def cd_status(boolean):
        '''Function to determine if CD was removed from stack
        Args:
            boolean (bool): Determines if CD is still there or not
        Returns:
            None
        '''
        if blnCDRmvd:
            print('\nThe CD was removed.\n')
        else:
            print('\nCould not find this CD!\n')
    

# 1. When program starts, read in the currently saved Inventory
dicTbl = FileProcessor.read_file(strFileName, dicTbl)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice.lower() == 'x':
        break
    # 3.2 process load inventory
    if strChoice.lower() == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('Type \'y\' to continue and reload from file; otherwise reload will be cancelled:\n')
        if strYesNo.lower() == 'y':
            print('reloading...')
            dicTbl = FileProcessor.read_file(strFileName, dicTbl)
            IO.show_inventory(dicTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(dicTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice.lower() == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        # TODone move IO code into function
        strID, strTitle, strArtist = IO.input_CD()
        # Compare supplied CD ID to existing CD IDs
        strID = DataProcessor.compare_CD(strID, dicTbl)
        # 3.3.2 Add item to the table
        # TODone move processing code into function
        dicTbl = DataProcessor.add_CD(strID, strTitle, strArtist, dicTbl)
        # Sorts CD inventory 
        dicTbl = DataProcessor.sort_CD(dicTbl)
        IO.show_inventory(dicTbl)
        print('You must save the file to keep this change.')
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice.lower() == 'i':
        IO.show_inventory(dicTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice.lower() == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(dicTbl)
        # 3.5.1.2 ask user which ID to remove
        intIDDel = IO.input_ID(dicTbl)
        # 3.5.2 search thru table and delete CD
        # TODone move processing code into function
        blnCDRmvd, dicTbl = DataProcessor.delete_CD(intIDDel, dicTbl)
        # Tell user if CD was able to be removed or not
        if dicTbl[0]['ID'] != None:
            IO.cd_status(blnCDRmvd)
        if blnCDRmvd:
            dicTbl = DataProcessor.sort_CD(dicTbl)
        # Show the inventory with the CD removed
            IO.show_inventory(dicTbl)
            print('You must save the file to keep this change.')
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice.lower() == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(dicTbl)
        strYesNo = input('Type \'y\' to save data to file; otherwise save will be cancelled:\n').strip().lower()
        # 3.6.2 Process choice
        if strYesNo.lower() == 'y':
            # 3.6.2.1 save data
            # TODone move processing code into function
            FileProcessor.write_file(strFileName, dicTbl)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')