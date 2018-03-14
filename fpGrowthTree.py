from collections import defaultdict, OrderedDict
from itertools import islice
from treeClass import PythonTree
import json


class FrequentPatternGrowthTree:
    def __init__(self, dataMatrix):
        self.data = dataMatrix
        self.k = 3
        self.initialFrequencyDict = self.getInitialFrequencies()
        self.topKFrequencies = self.getTopKFrequencies()
        self.frequencySortedTransactions = self.getFrequencySortedTransactions()
        self.pythonTree = self.createPythonTree()

    def getInitialFrequencies(self):
        frequencyDict = defaultdict(int)
        for i in range(len(self.data)):
            trans = self.data[i]
            for i in range(len(trans)):
                frequencyDict[trans[i]] += 1

        orderedDict = OrderedDict(sorted(frequencyDict.items(), key=lambda t: t[1], reverse=True))
        return orderedDict

    def printInitialFrequencies(self):
        print("\nFREQUENCIES")
        print(json.dumps(self.initialFrequencyDict, indent=5))

    def getTopKFrequencies(self):
        if self.k == -1:  # use all frequencies and items if is -1
            return list(self.initialFrequencyDict)
        else:
            return list(islice(self.initialFrequencyDict, self.k))

    def printTopKFrequencies(self):
        print("\nTOP K FREQUENCIES WHERE K = " + str(self.k))
        print(json.dumps(self.topKFrequencies, indent=5))

    def getFrequencySortedTransactions(self):
        masterList = []
        for tempArray in self.data:
            tempDict = {}  # new this up every time
            for j in range(len(tempArray)):
                if tempArray[j] in self.topKFrequencies:
                    tempDict[tempArray[j]] = self.initialFrequencyDict[tempArray[j]]
                    # else do not put item in list beacuse it is not top N
            masterList.append(list(OrderedDict(sorted(tempDict.items(), key=lambda t: t[1], reverse=True)).keys()))

        return masterList

    def printFrequencySortedTransactions(self):
        print("\nTRANSACTIONS IN FREQUENCY ORDER")
        for line in self.frequencySortedTransactions:
            print(line)

    def createPythonTree(self):
        tempTree = PythonTree()
        tempTree.addByMatrix(self.frequencySortedTransactions)
        return tempTree

    def getTreeStats(self):
        self.pythonTree.getTreeStats()

    def getAllItemsSetsWithFrequencyFromTree(self):
        return 4


# TRANSACTIONS = [['A', 'B', 'C', 'E', 'G', 'H'],
#                 ['A', 'B', 'E', 'F', 'M'],
#                 ['B', 'C', 'D', 'E', 'G', 'M'],
#                 ['A', 'B', 'C', 'H'],
#                 ['C', 'D', 'E', 'F', 'M'],
#                 ['A', 'B', 'C', 'E', 'H'],
#                 ['B', 'C', 'E', 'G', 'H', 'M']]

TRANSACTIONS = [['A', 'B', 'C', 'E', 'G', 'H'],
                ['A', 'B', 'E', 'F', 'M'],
                ['B', 'C', 'D', 'E', 'G', 'M']]

fpGrowthTree = FrequentPatternGrowthTree(TRANSACTIONS)
fpGrowthTree.printInitialFrequencies()
fpGrowthTree.printTopKFrequencies()
fpGrowthTree.printFrequencySortedTransactions()
fpGrowthTree.getTreeStats()



# def makeTree(allTransactionsMatrix):
#     root = dict()
#     for transaction in allTransactionsMatrix:
#         tempDict = root
#         for item in transaction:
#             if item in tempDict.keys():
#                 tempDict[item]['count'] = tempDict[item]['count'] + 1
#             tempDict = tempDict.setdefault(item, {'count': 1})
#     return root
#
#
# print("\nFP-GROWTH TREE")
# fpGrowthTree = (makeTree(masterList))
# print(json.dumps(fpGrowthTree, indent=5))

#
#
# print("\nGET ITEM SETS OUT OF FP-GROWTH TREE BY TRAVERSAL + RECURSION")
# rebuildMasterArray = []
#
#
# def recursivePrintitems(tree, builder):
#     for key, value in tree.items():
#         if tree[key] == {}:
#             tempBuilder = builder
#             builder += ',' + key
#             rebuildMasterArray.append(builder[1:].split(','))
#             builder = tempBuilder
#         else:
#             recursivePrintitems(tree[key], builder + "," + key)
#
# recursivePrintitems(fpGrowthTree, "")
#
#
# print("\nPOSSIBLE PATH TO AN ITEM")
#
# pathsTo = []
# for each in rebuildMasterArray:
#     tempPath = []
#     for i in each:
#         tempPath.append(i)
#         pathsTo.append(list(tempPath))
#
# allPathsToDict = {}
# for each in pathsTo:
#     if each[-1] in allPathsToDict:
#         if each[:-1] not in allPathsToDict[each[-1]]['paths']:
#             allPathsToDict[each[-1]]['paths'].append(each[:-1])
#     else:
#         allPathsToDict[each[-1]] = {
#             'paths': [each[:-1]]
#         }
#
#
# print(json.dumps(allPathsToDict, indent=5))
