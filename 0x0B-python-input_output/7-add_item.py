#!/usr/bin/python3

"""
    Program that save the arguments passed in command line
    as a json file.
"""
import sys
import json
save_json = __import__("5-save_to_json_file").save_to_json_file
load_json = __import__("6-load_from_json_file").load_from_json_file


# get the arguments passed.
args = sys.argv
# delete the name of program.
del args[0]

# get the old arguments.
old = None
try:
    old = load_json("add_item.json")
except Exception as e:
    pass

# add the new args to the old args list
if (old):
    old += args
else:
    old = args

# save the arguments to json file.
save_json(old, "add_item.json")
