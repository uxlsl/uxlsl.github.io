from io import  StringIO
from itertools import zip_longest


class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

def total(tree):
    if tree == None:
        return 0
    return total(tree.left) + total(tree.right) + tree.cargo


def print_tree(tree):
    if tree is None:
        return
    print(tree.cargo, end=' ')
    print_tree(tree.left)
    print_tree(tree.right)


def print_tree_indented(tree, level=0):
    if tree == None:
        return
    print_tree_indented(tree.right, level+1)
    print(' '*level +str(tree.cargo))
    print_tree_indented(tree.left, level+1)


def print_tree_indented_f(tree, f, level=0):
    if tree == None:
        return
    print_tree_indented_f(tree.right, f, level+1)
    f.write(' '*level +str(tree.cargo) + '\n')
    print_tree_indented_f(tree.left, f,  level+1)


def reverse_lists(lst):
    lst.reverse()
    lst1 = []
    for i in lst:
        i = i.replace('\n', ' ')
        lst1.append([j if j != '' else ' ' for j in i.split(' ') ])
    print (lst1)
    for i in zip_longest(*lst1, fillvalue=' '):
        print(''.join(i))


def print_tree_plot(tree):
    f = StringIO()
    print_tree_indented_f(tree, f)
    f.seek(0)
    lsts = f.readlines()
    reverse_lists(lsts)

left = Tree(2)
right = Tree(3)

tree = Tree(1, left, right)

print(total(tree))


tree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))
print_tree(tree)
print()

print_tree_indented(tree)
print()

print_tree_plot(tree)



def get_token(token_list, expected):
    if token_list[0] == expected:
        del token_list[0]
        return True
    else:
        return False


def get_product(token_list):
    a = get_number(token_list)
    if get_token(token_list, '*'):
        b = get_product(token_list)       # this line changed
        return Tree ('*', a, b)
    else:
        return a


def get_sum(token_list):
    a = get_product(token_list)
    if get_token(token_list, '+'):
        b = get_sum(token_list)
        return Tree ('+', a, b)
    else:
        return a


def get_number(token_list):
    if get_token(token_list, '('):
        x = get_sum(token_list)         # get the subexpression
        get_token(token_list, ')')      # remove the closing parenthesis
        return x
    else:
        x = token_list[0]
        if type(x) != type(0): return None
        token_list[0:1] = []
        return Tree (x, None, None)


lst = ['(', 3, '+', 7, ')' , '*', 9, 'end']

tree = get_sum(lst)
print_tree_plot(tree)

token_list = [9, '*', '(', 11, '+', 5, ')', '*', 7, 'end']
print(token_list)
tree = get_sum(token_list)
print('ok')
print_tree_plot(tree)
