

TREEDATA = [['F', 'B', 'A'],
    ['F', 'B', 'D', 'C'],
    ['F', 'B', 'D', 'E'],
    ['F', 'G', 'I', 'H']]

def createTree(allTransactionsMatrix):
    root = {}
    for transaction in allTransactionsMatrix:
        tempDict = root
        for item in transaction:
            tempDict = tempDict.setdefault(item, {})
    return root


def inOrderTraversal(pyTree):
    tempArray = []
    for key, value in pyTree.items():
        print(key)
        tempArray.append(key)
        if value == {}:
            print(tempArray)

def levelOrder(pyTree):
    tempLevel = []
    for key, value in pyTree.items():
        tempLevel.append(key)
        if (pyTree[key] != {}):
            levelOrder(pyTree[key])
    print(tempLevel)



def preOrderTraversal(pyTree):
    for key, value in pyTree.items():
        print(key)
        if isinstance(value, dict):
            preOrderTraversal(value)


def postOrderTraversal(pyTree):
    for key, value in pyTree.items():
        if isinstance(value, dict):
            preOrderTraversal(value)
        print(key)


def getDepth(pyTree, level=1):
    if not isinstance(pyTree, dict) or not pyTree:
        return level
    return max(getDepth(pyTree[item], level + 1) for item in pyTree)

import json
pyTree = createTree(TREEDATA)
print(json.dumps(pyTree, indent=5))
# print(getDepth(pyTree))
print('PREORDER')
preOrderTraversal(pyTree)
print('POSTORDER')
postOrderTraversal(pyTree)
# print("INORDER")
# inOrderTraversal(pyTree)
print("LEVELORDER")