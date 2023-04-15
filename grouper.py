import torch
import numpy as np
import math
from collections import defaultdict
import argparse
import pickle
import copy

grouping_volatility = 1.2
def set_grouping_volatility(num):
    global grouping_volatility
    grouping_volatility = num

def SigmoidMembership(number_of_classes,x, grouping_volatility):
    num = float(grouping_volatility)
    return 1.0 / ( 1.0 + math.exp(-(x - (1.0 / number_of_classes*num)) / ( 1.0 / ( 10.0*number_of_classes*num ))) )
def MakeDictionary(l):
    final_dict = defaultdict(list)
    for i in l:
        for j in i:
            for k in i:
                if k not in final_dict[j]:
                    final_dict[j].append(k)
                if j not in final_dict[k]:
                    final_dict[k].append(j)

    for i in final_dict:
        for j in final_dict[i]:
            for k in final_dict[j]:
                if k not in final_dict[i]:
                    final_dict[i].append(k)
    return final_dict
def ModelVisualSimilarityMetric(model_avgsoftmax_path, path_to_save_supergroup_pt):
    # Load the average softmax
    model_avgsoftmax = torch.load( model_avgsoftmax_path ,map_location=torch.device('cpu'))
    # Print number of classes
    number_of_classes = model_avgsoftmax.shape[0]
    
    l = []
    for i in range(number_of_classes):
        l.append([i])
        for j in range(i,number_of_classes):
            global grouping_volatility
            prob = SigmoidMembership(number_of_classes, model_avgsoftmax[i][0][j], grouping_volatility)
            if np.random.choice(2, 100000, p = [1 - prob, prob]).mean() > 0.5:
                if i != j:
                    l[i].append(j)

    final_dict 			= MakeDictionary(l)
    seen 				= []
    super_group_list 	= []
    for i in final_dict:
        if i not in seen:
            super_group_list.append(final_dict[i])
            for j in final_dict[i]:
                seen.append(j)
    
        
    ### Save to file
    with open(path_to_save_supergroup_pt,'wb') as f:
        pickle.dump(super_group_list, f)
        
    ### return group
    return super_group_list, len(super_group_list)