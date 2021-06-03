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

    def __len__(self):
        """ Return the number of items in the linked list.

        >>> s = Link(1, Link(2, Link(3)))
        >>> len(s)
        3
        >>> s = Link.empty
        >>> len(s)
        0
        """
        return 1 + len(self.rest)

    def __getitem__(self, i):
        """Returning the element found at index i.

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1]
        2
        >>> s[2]
        3
        """
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

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



######################
#### Linked Lists ####
######################

def link_to_list(link):
    """Takes a Link and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    li = []
    if not link:
        return li
    else:
        li.append(link.first)
        li += link_to_list(link.rest)
    return li


def every_other(s):
    """Mutates a linked list so that all the odd-indiced elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    if not s or not s.rest:  #empty or single element linked list
        return
    s.rest = s.rest.rest  #set next linked list to the linked list after (we can do a similar implementation for deleting the even-numbered entries
    every_other(s.rest)


######################
#### Trees ####
######################

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



def leaves(t):
    """Returns a list of all the entries of the leaf nodes of the Tree t.

    >>> leaves(Tree(1))
    [1]
    >>> leaves(Tree(1, [Tree(2, [Tree(3)]), Tree(4)]))
    [3, 4]
    """
    li = []
    if not t:  #empty tree
        return li
    if not t.branches:  #tree with only 1 element and no branches
        li.append(t.entry)
        return li
    else:  #tree with branches
        for subtree in t.branches:  #go through every subtree in branches
            if not subtree.branches:  #if the subtree in branches of t have no branches themselves, append to li 
                li += [subtree.entry]  #append the value of the branchless nodes to li
            else:  #if subtrees have branches, then run the routine again for the subtree, this should search every subtree in t
                li+=leaves(subtree) 
        return li


def path(t, value):
    """
    >>> t = Tree(9, [Tree(7, [Tree(3), Tree(2)]), Tree(5)])
    >>> path(t, 2)
    [9, 7, 2]
    >>> path(t, 5)
    [9, 5]
    >>> path(t, 8)
    []
    """
    li = []
    if not t:  #absolutely trivial base case, empty tree
        return []
    if value == t.entry:  #necessary base case, if value meets some entry
        li += [t.entry]
        return li
    #most general case, search through every subtree and if it meets any of the base cases, it will append to the list, li
    for subtree in t.branches:
        li += path(subtree, value)
    if value in li:
        return [t.entry] + li
    else:
        return []


def find_level(t, level):
    """
    >>> t = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> find_level(t, 2)
    [4, 5, 7]
    >>> find_level(t, 1)
    [2, 6]
    >>> find_level(t, 5)
    []
    """
    #base cases
    li = []
    if level == 0:
        return [t.entry]
    #general case, reduce the tree by chopping off every node that is not that depth, one level at time
    if level > 0:
        for subtree in t.branches:
            li += find_level(subtree, level - 1)
    return li



