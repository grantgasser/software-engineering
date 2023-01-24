"""
input_obj = {
    "name": "Arthur",
    "age": 30,
    "delivery_address": {
        "street": "1600 Penn Ave",
        "city": "DC",
        "zip": "12345"
    },
    "purchases": [
        {
            "product": "chair",
            "price": 100
        },
        {
            "product": "desk",
            "price": 500
        }
    ]
}

=>

{
    numbers: 3,
    strings: 6,
    arrays: 1,
    object: 3
}
"""

def count_types(json_obj):
    count = {
        "numbers": 0,
        "strings": 0,
        "arrays": 0,
        "objects": 0
    }

    def helper(obj):
        for key, val in obj.items():
            if isinstance(val, dict):
                count["objects"] += 1
                helper(val)
            elif isinstance(val, list):
                count["arrays"] += 1
                for e in val:
                    if isinstance(e, dict):
                        count["objects"] += 1
                    if isinstance(e, list):
                        count["arrays"] += 1
                    helper(e)
            elif isinstance(val, int) or isinstance(val, float):
                count["numbers"] += 1
            elif isinstance(val, str):
                count["strings"] += 1

        return

    helper(json_obj)

    return count


input_obj = {
    "name": "Arthur",
    "age": 30,
    "delivery_address": {
        "street": "1600 Penn Ave",
        "city": "DC",
        "zip": "12345"
    },
    "purchases": [
        {
            "product": "chair",
            "price": 100
        },
        {
            "product": "desk",
            "price": 500
        }
    ]
}

print(count_types(input_obj))

