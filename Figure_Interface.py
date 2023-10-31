#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 11:11:53 2023

@author: Tyler Langos
"""
#%%
""" Figure Interface """
#%%
'Step 8 - Figure_Interface is displayed'
# Screen is split into its own 3 panels - 
# a) Data Selection
#       Upper-left quadrant
#       User selects datasets or variables to display

# b) Figure Options
#       Lower-left quadrant
#       User chooses graph style (bar, line, pie, etc) & theme (colour)

# c) Figure Display & Customization
#       Right half
#       Displays data as it is added


# At any point the user can click the 'Back to Dashboard' button (top-center of
# the screen) to go back to the Dashboard_Interface. All progress in the panel
# will be saved so that when a user selects that panel again they will be
# exactly where they left off
#%%
'Step 8a - User Chooses Data'
# Dropdown menu of the datasets they've uploaded
# 'Add more data' (text) followed by '+' (button) appears. If they click the +,
# another dropdown menu will appear for them to choose another dataset

# Other data analysis options (i.e., groupby)

#%%
'Step 8b - User choses base figure options'
# First, the user will choose between 3 options - Graph, Table, *Map

'If they choose Graph:'
# A dropdown menu will appear will different graph types
# (line, bar, pie, etc) in alphabetical order. 
# *Hovering over an option from this menu displays a jpeg of a simplified
# example of that type of graph
# Once the user chooses an option, queries necessary for creating the specific
# graph will be displayed (e.g., 'Bar Graph' would query for the Y-axis and X-axis)
#### This part will take a long time, as most types of graph will require a 
#### unique set of queries

'If they choose Table:'
# Same as above, skipping the 'selecting a type' step

'If they choose Map*'
# We can't feasibly create a Map Layout Editor with how little time we have,
# but it could be appealing, similarly to the 'Load Dashboards' button.

#%%
'Step 8c - Customizing the Figure'

'Displaying the figure'
# Once the user has entered enough information in the prior panels, the graph/table/map
# will be displayed in the right panel.  It will also update each time a change 
# is  made to the prior panels

'Customizing the figure'
# Users may right-click any individual feature on the figure to open a dropdown
# list of editable features (e.g., text, fill colour, outline colour)



