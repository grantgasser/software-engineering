"""
9.5

Cache: Imagine a web server for a simplified search engine. This system has 100 machines to
respond to search queries, which may then call out using processSearch(string query)
to another cluster of machines to actually get the result. The machine which responds to a given
query is chosen at random!, so you cannot guarantee that the same machine will always respond to
the same request. The method processSearch is very expensive. Design a caching mechanism
to cache the results of the most recent queries. Be sure to explain how you would update the cache
when data changes.
"""

# NOTE: this code is assuming 1 machine
class Node(object):
    def __init__(self):
        self.query = None
        self.result = None
        self.next = None
        self.prev = None

class Cache(object):
    def __init__(self):
        self.map_query_to_result = {}  # map query to node containing result
        self.MAX_SIZE = 10
        self.head = Node()
        self.tail = Node()
        self.size = 0

     def move_to_front(self, node):
         # move most recent query and result to front
         pass

    def remove_node_from_linked_list(node):
        pass

    def get_results(query):
        # get result node of query
        result = self.map_query_to_result[query]

        if not result: 
            return None
        else:
            self.move_to_front(result)
            return result

    def insert_results(query, results):
        # insert result string of query into list and hash map
        result_node = self.map_query_to_result.get(query)
        if result_node:
            # update results
            result_node.results = results
            self.move_to_front(result_node)
            return

        # create new node w/ result string, move to front, and add to hash map
        new_node = Node(results)
        self.move_to_front(new_node)
        self.map_query_to_result[query] = new_node

        if self.size > self.MAX_SIZE:
            # remove tail
            del self.map_query_to_result[self.tail.query]
            self.remove_node_from_linked_list(self.tail)

"""
If cache is too large to live on 1 machine:

(3) can divide up cache s.t. each machine holds a different part. 
When machine i is given a query, it would figure out which machine
should hold the results via hash(query) % 100 = j. Then it would
send of the query to machine j. Machine j checks its cache and returns
if there, else, runs processSearch(query). Then updates its cache 
afterwards.
"""