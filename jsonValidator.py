# test_jsonschema_unix.py
# A program to try the jsonschema Python library.
# Uses it to validate some JSON data.
# Follows the Unix convention of writing normal output to the standard
# output (stdout), and errors to the standard error output (stderr).
# Author: Vasudev Ram
# Copyright 2015 Vasudev Ram

from __future__ import print_function
import sys
import json
import jsonschema
from jsonschema import validate

# Create the schema, as a nested Python dict,
# specifying the data elements, their names and their types.
# "type": "object",
#     "required": [ "storage" ],
#     "properties": {
#         "storage": {
#             "type": "object",
schema = {
    "type": "object",
    "required": ["PC"],
    "properties": {
        "PC": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "Name": {"type": "string"},
                    "Species": {"type": "string"},
                },
            },
        },
    },
}

print("Testing use of jsonschema for data validation.")
print("Using the following schema:")
print(schema)
print("Pretty-printed schema:")
print(json.dumps(schema, indent=4))

# The data to be validated:
# Two records OK, three records in ERROR.
data = [
    {"PC": [{"Name": "Waldrich", "Species": "Human"},
            {"Name": "Umgi'Got", "Species": "Dwarf"}]
     }
]

# data = \
#     [
#         {"name": "Apples", "price": 10},
#         {"name": "Bananas", "price": 20},
#         {"name": "Cherries", "price": "thirty"},
#         {"name": 40, "price": 40},
#         {"name": 50, "price": "fifty"}
#     ]

print("Raw input data:")
print(data)
print("Pretty-printed input data:")
print(json.dumps(data, indent=4))

print("Validating the input data using jsonschema:")
for idx, item in enumerate(data):
    try:
        validate(item, schema)
        sys.stdout.write("Record #{}: OK\n".format(idx))
    except jsonschema.exceptions.ValidationError as ve:
        sys.stderr.write("Record #{}: ERROR\n".format(idx))
        sys.stderr.write(str(ve) + "\n")
