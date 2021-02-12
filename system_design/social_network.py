"""
9.2 Social Network: How would you design the data structures for a very large social network 
like Facebook or Linkedln? Describe how you would design an algorithm to show the shortest path between
two people (e.g., Me -> Bob -> Susan -> Jason -> You).
"""

# Optimizations: store people in same geographic location on same server
# Could cache previously searched paths from 1 person to another
class Person(object):
    self.ID = None
    self.name = None
    self.connections = [Person1, Person2]

class Servers(object):
    self.machines = {'1': Machine1, '2': Machine2}
    self.person_to_machine = {'1': '1', '2': '2'}  # person1 on machine 1, person2 on machine 2, etc.

    def get_person_with_ID(person_ID):
        machine_ID = self.person_to_machine[person_ID]
        machine = self.get_machine_with_ID(machine_ID)
        return machine.get_person_with_ID(person_ID) 

    def get_machine_with_ID(machine_ID):
        return self.machines[machine_ID]
    

class Machine(object):
    self.ID
    self.persons = {'1': Person1, '2': Person2}

    def get_person_with_ID(person_id):
        return self.persons[id]


def bidirectional_BFS(src, dst):
    visited = set()  # don't mark node as visited, just keep track in hash table/set
    # {Person1, Person2, ...}

