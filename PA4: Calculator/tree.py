# author: Arthur Wei
# date: November 14, 2022
# file: tree.py a python file that creates a tree class that can be used to create an expression tree
# input: Data to be inserted into the tree
# output: Data that is popped from the tree and the value of the expression

from stack import Stack


class BinaryTree:
    def __init__(self, rootObj=None):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def __str__(self):
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s


class ExpTree(BinaryTree):

    def make_tree(postfix) -> BinaryTree:
        Stack1 = Stack()  # create a stack
        for symb in postfix:  # for each symbol in the postfix expression
            if symb.isdigit() or symb.replace('.', '', 1).isdigit():  # if symb is a number or a float
                Stack1.push(ExpTree(symb))
            else:
                temp = ExpTree(symb)
                temp.rightChild = Stack1.pop()
                temp.leftChild = Stack1.pop()
                Stack1.push(temp)
        return Stack1.pop()

    def preorder(tree):  # preorder traversal
        s = ''
        if tree != None:
            s += str(tree.getRootVal())
            s += ExpTree.preorder(tree.getLeftChild())
            s += ExpTree.preorder(tree.getRightChild())
        return s

    def inorder(tree):  # inorder traversal
        s = ''
        if tree != None:
            if tree.leftChild != None:
                s += '(' + ExpTree.inorder(tree.getLeftChild())
            s += str(tree.getRootVal())
            if tree.rightChild != None:
                s += ExpTree.inorder(tree.getRightChild()) + ')'
        return s

    def postorder(tree):  # postorder traversal
        s = ''
        if tree != None:
            s += ExpTree.postorder(tree.getLeftChild())
            s += ExpTree.postorder(tree.getRightChild())
            s += str(tree.getRootVal())
        return s

    def evaluate(tree):  # evaluate the expression tree
        if tree == None:  # if the tree is empty return None
            return None
        else:
            left = ExpTree.evaluate(tree.getLeftChild())
            right = ExpTree.evaluate(tree.getRightChild())
            if tree.getRootVal() == '+':
                return left + right
            elif tree.getRootVal() == '-':
                return left - right
            elif tree.getRootVal() == '*':
                return left * right
            elif tree.getRootVal() == '/':
                return left / right
            elif tree.getRootVal() == '^':
                return left ** right
            else:
                # if the root value is a number return it as a float else return 0
                return float(tree.getRootVal() if tree.getRootVal() != None else 0)

    def __str__(self):
        return ExpTree.inorder(self)


# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':

    # test a BinaryTree

    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild() == None
    assert r.getRightChild() == None
    assert str(r) == 'a()()'

    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'

    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'

    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'

    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'

    # test an ExpTree

    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)
    print(tree)
    assert str(tree) == '(5+(2*3))'
    print('inorder:', ExpTree.inorder(tree))
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    print('postorder:', ExpTree.postorder(tree))
    assert ExpTree.preorder(tree) == '+5*23'
    print('preorder:', ExpTree.preorder(tree))
    assert ExpTree.evaluate(tree) == 11.0

    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0
    print("All tests passed")
