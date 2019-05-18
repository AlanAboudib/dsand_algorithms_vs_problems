# A RouteTrie will store our routes and their associated handlers
class RouteTrie:


    def __init__(self, root_handler, not_found_handler):


        self.not_found_handler = not_found_handler
        
        ## add a root node (with '/' as string)
        self.root = RouteTrieNode(string = '/', handler = root_handler)
        

    def insert(self, path, handler):
        ## Add a path to the RouteTrie
        ## 'path' is a list of strings. e.g, /home/page, the path
        ## is ['home', 'page']
        ## we assign the handler to only the leaf (deepest) node of this path
        
        # keep track of the last inserted or traversed node
        last_node = self.root
        
        # start insertion
        for i, string in enumerate(path):
            
            # first check whether the string is already there
            node = last_node.find(string)
            if node:
                last_node = node
            else:
                # insert the string as a node

                if i == len(path) - 1:
                    # we assign handler to the last node added
                    last_node = last_node.insert(string, handler)
                else:
                    last_node = last_node.insert(string, self.not_found_handler)
                

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        
        # keep track of the last traversed node
        last_node = self.root
        
        # traverse the Trie
        for string in path:


            node = last_node.find(string)

            if node is not None:
                last_node = node
            else:
                return self.not_found_handler
            
        return last_node.handler
        
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:

    def __init__(self, string, handler = '404 Page Not Found'):
        ## Initialize this node in the Trie
        
        # set the node's string
        self.string = string

        # the handler
        self.handler = handler
        
        # a dictionary of child nodes (RouteTrieNode objects)
        # indxed by the string each one
        self.children = {}
    
    def insert(self, string, handler):
        
        ## Add a child node in this RouteTrieNode
        self.children[string] = RouteTrieNode(string, handler)
        
        # return a reference to the inserted node
        return self.children[string]
    
    def find(self, string):
        
        ## get the child with 'string'
        if string in self.children:
            return self.children[string]
        else:
            return None
        

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes

        self.rt = RouteTrie(root_handler, not_found_handler)

        

    def add_handler(self, route, handler):
        # Add a handler for a path

        # get only the strings between the slashes
        path = self.split_path(route)

        self.rt.insert(path, handler)
        
    

    def lookup(self, route):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        # get the route strings

        # deal with the route ''
        if route == '':
            return self.rt.root.not_found_handler
        
        # deal with the route '/'
        if route == '/':
            return self.rt.root.handler

        path = self.split_path(route)

        # find the handler for that path
        handler =  self.rt.find(path)

        return handler

    def split_path(self, route):
        # split the path into parts for 
        # both the add_handler and lookup functions.


        # split the route into a list of strings (excluding slashes)
        path = route.split('/')

        # remove any empty strings in 'path' resulting from slashes at the beginning or the end
        path = [string for string in path if string != '']

        return path
        

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "404 page found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("")) # should return 'not found handler'





