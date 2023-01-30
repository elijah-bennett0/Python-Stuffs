# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import pyodbc
from time import sleep
from colorama import Style, Fore, Back, init

class prints:
    def good(s):
        print(Style.BRIGHT + Fore.GREEN + '[+] ' + Style.RESET_ALL + s)
    def bad(s):
        print(Style.BRIGHT + Fore.RED + '[-] ' + Style.RESET_ALL + s)
    def warning(s):
        print(Style.BRIGHT + Fore.YELLOW + '[!] ' + Style.RESET_ALL + s)
    def info(s):
        print(Style.BRIGHT + Fore.BLUE + '[*] ' + Style.RESET_ALL + s)
        
def main():
    '''
    1. Connect to db
    2. Search db
    3. Display Search results
    '''
    db = connect_to_database()
    query = input('[\'exit\' to quit] Search query: ')
    while query.lower() != 'exit':
        results = search(query, db)
        display_results(results)
        query = input('[\'exit\' to quit] Search query: ')
    prints.warning('Exiting in 3 seconds!')
    sleep(3)
    

# Error: InterfaceError: ('IM002', u'[IM002] [Microsoft][ODBC Driver Manager] Data source name not found and no default driver specified (0) (SQLDriverConnect)')".
# Solution: Install Microsoft Access Database Engine 2010 
def connect_to_database(): # returns the full database
    conn_str = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\Users\benneeli3\Desktop\2016.accdb'
            ) # String used to connect to access db file
    cnxn = pyodbc.connect(conn_str) # setting up a connection using the connection string
    crsr = cnxn.cursor() # the cursor that executes db commands
    crsr.execute('select * from Table1') # select everything from Table1
    database = crsr.fetchall()
    return database

# Id: everything[0][0]
# Users: everything[0][1]
# Pwds: everything[0][2]
def search(query, db):
    results = ''
    for row in db: # for each row in the database
        if row[1] == query: # if the rows usr equals query
            results = row # this is the result
            break
        else:
            pass # if it's not, keep searching
    return results

def display_results(results):
    if results == '':
        prints.bad('Query not found!')
    else:
        prints.good('User: %s | Password: %s' % (results[1], results[2]))
        
if __name__ == '__main__': # If this file is the main file, run main function
    init() # Initiate colorama
    main()