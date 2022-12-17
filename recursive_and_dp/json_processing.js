/*
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

--------
Notes

string
number
object
Array
*/

var input1 = {
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

// TODO: array works a bit different, check for 'Array' and only look at first object
// assume all objects in the array are the same
function buildSchema(input, indent = 0) {
    var schema = '';

    for (key of Object.keys(input)) {
        if (getDataType(input[key]) == 'object') {
            schema += 'Object\n' + buildSchema(input[key], indent + 1);
        } else {
            schema += '---'.repeat(indent) + key + ': ' + getDataType(input[key]) + '\n';
        }
    }


    return schema;
}

function getDataType(data) {
    return typeof data;
}

console.log(buildSchema(input1));
