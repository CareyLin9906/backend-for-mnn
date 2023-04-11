import argparse
import sys
import grouper


data = sys.argv[1]
"""
dummy variables:
class number = 5
path of average softmax matrix: root_avgsoftmax.pth
"""
grouping_volatility = sys.argv[2]
softmaxMatrix = "root_avgsoftmax.pth"
classNumber = 5
sigmoidMembership = grouper.SigmoidMembership(classNumber, softmaxMatrix, grouping_volatility)


print(data)
print(grouping_volatility)