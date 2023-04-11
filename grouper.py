import torch
import numpy as np
import math
from collections import defaultdict
import argparse
import pickle
import copy


def SigmoidMembership(number_of_classes,x, grouping_volatility):
    return 1.0 / ( 1.0 + math.exp(-(x - (1.0 / number_of_classes*grouping_volatility)) / ( 1.0 / ( 10.0*number_of_classes*grouping_volatility ))) )
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
def ModelVisualSimilarityMetric(model_avgsoftmax_path, path_to_save_supergroup_pt, should_print_sg):
    # Load the average softmax
    model_avgsoftmax = torch.load( model_avgsoftmax_path )
    # Print number of classes
    number_of_classes = model_avgsoftmax.shape[0]
    print("Number of classes: {}".format(number_of_classes))
    
    l = []
    for i in range(number_of_classes):
        l.append([i])
        for j in range(i,number_of_classes):
            prob = SigmoidMembership(number_of_classes, model_avgsoftmax[i][0][j])
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
    ### Only print if flag is set
    if should_print_sg == True:
        for i in super_group_list:
            i.sort()
            print(i)
        
    ### Save to file
    with open(path_to_save_supergroup_pt,'wb') as f:
        pickle.dump(super_group_list, f)
        
    ### return group
    return super_group_list, len(super_group_list)