## Linked Lists ##

# Linked List Class
class Link:
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s
    Link(1, Link(2, Link(3)))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

def print_link(link):
    """Print elements of a linked list link.
    
    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> link1 = Link(1, Link(Link(2), Link(3)))
    >>> print_link(link1)
    <1 <2> 3>
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print_link(link1)
    <3 <4> 5 6>
    """
    print('<' + helper(link).rstrip() + '>')
    
def helper(link):
    if link == Link.empty:
        return ''
    elif isinstance(link.first, Link):
        return '<' + helper(link.first).rstrip() + '> ' + helper(link.rest)
    else:
        return str(link.first) +' '+  helper(link.rest)

# Q2
def list_to_link(lst):
    """Takes a Python list and returns a Link with the same elements.

    >>> link = list_to_link([1, 2, 3])
    >>> print_link(link)
    <1 2 3>
    """
    if len(lst) == 1:
        return Link(lst[0])
    else:
        return Link(lst[0], list_to_link(lst[1:]))


# Q3
def reverse(link):
    """Returns a Link that is the reverse of the original.

    >>> print_link(reverse(Link(1)))
    <1>
    >>> link = Link(1, Link(2, Link(3)))
    >>> new = reverse(link)
    >>> print_link(new)
    <3 2 1>
    >>> print_link(link)
    <1 2 3>
    """
    #set new link as the linked list of first element
    new_link = Link(link.first)
    while link.rest is not Link.empty:
        link = link.rest  #set the original link to link sans first element
        new_link = Link(link.first, new_link)  #define new_link recursively
    return new_link


#Trees

# Tree Class
class Tree:
    def __init__(self, entry, branches=()):
        self.entry = entry
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.entry, branches_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.entry) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

    def is_leaf(self):
        return not self.branches



# Q4 
def search(t, value):
    """Searches for and returns the Tree whose entry is equal to value if
    it exists and None if it does not. Assume unique entries.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> search(t, 10)
    >>> search(t, 5)
    Tree(5)
    >>> search(t, 1)
    Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    """

    if t.entry == value:
        return t
    for tree in t.branches:
        branches = search(tree, value)
        if branches is not None:
            return branches
    return None

# Q5
def cumulative_sum(t):
    """Return a new Tree, where each entry is the sum of all entries in the
    corresponding subtree of t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative = cumulative_sum(t)
    >>> t
    Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(Tree(1))
    Tree(1)
    """
    li = []  #initialize an empty list
    new_entry = 0  #keep track of new entries
    for subtree in t.branches:  #get a list of every subtree of t
        li += [cumulative_sum(subtree)]
    for tree in li:  #replace each node with the sum of all of the nodes in its subtrees
        new_entry += tree.entry
    new_entry += t.entry  #add to final entry of tree
    return Tree(new_entry, li)  #create new tree with node with new entry, this will be called recursively in the creation of li

