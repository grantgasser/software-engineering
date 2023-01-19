"""
Given json object, build the schema of the
object and return as a string.
Ex.
input1 = {
    "name": "Grant",
    "age": 26,
    "cigarette": [
        {
            "name": "Camel",
            "price": 4.5
        },
        {
            "name": "Lucky Strike",
            "price": 4.9
        }
    ],
    
    "address": {
        "street1": "123 floral st",
        "city": "Cupertino",
        "zipcode": 12345
    }
}
=> a String like so:
'
Object
--- name: string
--- age: number
--- cigarette: Array
------ Object
--------- name: string
--------- price: number
--- address: Object
------ street1: string
------ city: string
------ zipcode: number
'
"""

def build_schema(json_obj, indent=1):
    schema = ""
    indent_str = "---"
    indent_str = indent_str*indent + " "

    for key, val in json_obj.items():
        if isinstance(val, dict):
            schema += indent_str + str(key) + ": Object\n"
            schema += build_schema(val, indent+1)
        elif isinstance(val, list):
            schema += indent_str + str(key) + ": Array\n"
            if isinstance(val[0], dict) or isinstance(val[0], list):
                schema += build_schema(val[0], indent+1)
            else:
                schema += indent_str + str(key) + ": " + type(val).__name__ + "\n"
        else:
            # types that don't require recursion (int, str, etc.)
            schema += indent_str + str(key) + ": " + type(val).__name__ + "\n"

    return schema


input1 = {
    "name": "Grant",
    "age": 26,
    "cigarette": [
        {
            "name": "Camel",
            "price": 4.5
        },
        {
            "name": "Lucky Strike",
            "price": 4.9
        }
    ],
    "address": {
        "street1": "123 floral st",
        "city": "Cupertino",
        "zipcode": 12345
    }
}

print(build_schema(input1))