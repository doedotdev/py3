from queue import *
import json
import itertools
import math


class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.parent = ""
        self.freq = 1
        self.path = []

    def get(self):
        return self.val

    def set(self, val):
        self.val = val

    def getChild(self, val):
        for each in self.children:
            if each.val == val:
                return each

    def getChildren(self):
        childArray = []
        for each in self.children:
            childArray.append(each.val)
        return childArray

    def printStats(self):
        print("Value: " + str(self.val) + " | " +
              "Frequency: " + str(self.freq) + " | " +
              "Parent: " + str(self.parent) + " | " +
              "Children: " + ','.join(self.getChildren())
              )


class PythonTree:
    def __init__(self):
        self.root = Node("*root*")
        self.root.parent = "NONE"
        self.root.path = ["*root*"]
        self.totalTreeNodes = 1
        self.totalInsertions = 1
        self.treeDepth = 0
        self.visualDict = {self.root.get()}

    def setVisualDict(self, passedMatrix):
        root = dict()
        for transaction in passedMatrix:
            tempDict = root
            for item in transaction:
                if item in tempDict.keys():
                    tempDict[item]['count'] += 1
                tempDict = tempDict.setdefault(item, {'count': 1})
        self.visualDict = root

    def addByMatrix(self, passedMatrix):

        self.setVisualDict(passedMatrix)

        for subArray in passedMatrix:
            currentNode = self.root
            tempLength = len(subArray)
            if tempLength > self.treeDepth:
                self.treeDepth = tempLength
            tempPath = [self.root.get()]
            for each in subArray:
                self.totalInsertions += 1
                if each in currentNode.getChildren():
                    tempPath.append(each)
                    currentNode = currentNode.getChild(each)
                    currentNode.freq += 1
                else:
                    self.totalTreeNodes += 1
                    tempNode = Node(each)
                    tempParent = currentNode.get()
                    currentNode.children.append(tempNode)
                    currentNode = tempNode
                    currentNode.parent = tempParent
                    currentNode.path = tempPath
                    currentNode.path.append(each)



    def preOrder(self, currentNode, retArray):
        retArray.append(currentNode.get())
        for each in currentNode.children:
            self.preOrder(each, retArray)
        return retArray

    def preOrderTraversal(self):
        return self.preOrder(self.root, [])

    def inOrder(self, currentNode, retArray):
        whole = len(currentNode.children)
        half = math.ceil(whole / 2)

        for each in itertools.islice(currentNode.children, 0, half):
            self.inOrder(each, retArray)
        retArray.append(currentNode.get())
        for each in currentNode.children[half:]:
            self.inOrder(each, retArray)

        return retArray

    def inOrderTraversal(self):
        return self.inOrder(self.root, [])

    def postOrder(self, currentNode, retArray):
        for each in currentNode.children:
            self.postOrder(each, retArray)
        retArray.append(currentNode.get())
        return retArray

    def postOrderTraversal(self):
        return self.postOrder(self.root, [])

    def levelOrderTraversal(self):
        currentNode = self.root
        q = Queue()
        q.put(currentNode)
        output = []
        while q.qsize() > 0:
            currentNode = q.get()
            output.append(currentNode.val)
            for each in currentNode.children:
                q.put(each)
        return output

    def getStatsTraversal(self):
        currentNode = self.root

        mostFrequent = []
        leastFrequent = []
        maxVal = currentNode.freq
        minVal = currentNode.freq

        q = Queue()
        q.put(currentNode)
        while q.qsize() > 0:
            currentNode = q.get()
            currentNode.printStats()
            # Max Checks
            if currentNode.freq > maxVal:
                mostFrequent = [currentNode.get()]
                maxVal = currentNode.freq
            if currentNode.freq == maxVal:
                if currentNode.get() not in mostFrequent:
                    mostFrequent.append(currentNode.get())
            # Min Checks
            if currentNode.freq < minVal:
                leastFrequent = [currentNode.get()]
                minVal = currentNode.freq
            if currentNode.freq == minVal:
                if currentNode.get() not in leastFrequent:
                    leastFrequent.append(currentNode.get())

            for each in currentNode.children:
                q.put(each)
        return mostFrequent, leastFrequent, maxVal, minVal

    def getTreeStats(self):
        print("***Including the *root* node***\n")
        mostFrequent, leastFrequent, maxVal, minVal = self.getStatsTraversal()
        print("\nTotal Nodes: " + str(self.totalTreeNodes))
        print("Total Insertions ( greater than or equal to total Nodes ): " + str(self.totalInsertions))
        print("Depth of Tree: " + str(self.treeDepth))
        print("Most Frequent Nodes: " + str(mostFrequent) + " appeared (" + str(maxVal) + ") time(s)")
        print("Least Frequent Nodes: " + str(leastFrequent) + " appeared (" + str(minVal) + ") time(s)")
        avg = float(self.totalInsertions / self.totalTreeNodes)
        print("Average Node Frequency " + str(avg) + " (totalNodes/ totalInsertions")
        print(json.dumps(self.visualDict, indent=5))


# myTree = PythonTree()
# myTree.addByMatrix([['F', 'B', 'A'],
#                     ['F', 'B', 'D', 'C'],
#                     ['F', 'B', 'D', 'E'],
#                     ['F', 'G', 'I', 'J'],
#                     ['F', 'G', 'I', 'H']])
#
# print("\nPRE ORDER TRAVERSAL")
# print(myTree.preOrderTraversal())
#
# print("\nLEVEL ORDER TRAVERSAL")
# print(myTree.levelOrderTraversal())
#
# print("\nIN ORDER TRAVERSAL")
# print(myTree.inOrderTraversal())
#
# print("\nPOST ORDER TRAVERSAL")
# print(myTree.postOrderTraversal())
#
# print("\nTREE STATS")
# myTree.getTreeStats()
