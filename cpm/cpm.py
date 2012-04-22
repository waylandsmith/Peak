#!/usr/bin/env python

def print_CPM():
    CPM = """
------------------------------------------------------------------------------------------
Part|	Description	    | Inherits	|	Needs	|	Effort	|	Timespan |
1| Plan Game            | --    	|	3       |       4 hours	|	1 week   |
2| Define Rules   	| 2             |	1   	|	3 hours |       2 days   |
3| Configure Libraries  | --            |   --  	|	10 hours|	1.5 weeks|
4| Create Assets        | 1,2,6         |	1,2 	|	8 hours |	2 weeks  |
5| Code Game        	| 3,2,1 	|	3,2 	|	20 hours|	3 weeks  |
6| Create Story         | 1     	|	1   	|	4 hours |	1 week   |
7| Packaging & Polish   | 3,4,5,6       |	4,5,6	|	3 hours |	3 days   |
------------------------------------------------------------------------------------------
End date:  May 07, 2012
Weeks Remaining: 5
Days Remaining  35

Order of steps:
Play around with and configure libraries and tools - Now to April 13
Plan a game based on what we're able to do with the initial step - April 4 to April 11
Define the rules to that game - April 11 to April 13
Delve into asset, code, and story creation simultaneously piece-by-piece - April 13 to May 4
Package what works - May 4 to May 7

"""

    print CPM
    
print_CPM()

