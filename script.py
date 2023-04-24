import argparse
import sys
import grouper


data = sys.argv[1]
grouping_volatility = sys.argv[2]
avgsoftmax = "Kuzu49_root_avgsoftmax.pth"
if data == "Kuzu_49":
    avgsoftmax = "Kuzu49_root_avgsoftmax.pth"
elif data == "Kuzu_Kanji":
    avgsoftmax = "KuzuKanji_root_avgsoftmax.pth"
classNumber = 5
pickled_filename = avgsoftmax.replace('.pth','.pickle')
grouper.set_grouping_volatility(grouping_volatility)
super_group_list, number_of_groups = grouper.ModelVisualSimilarityMetric(avgsoftmax, pickled_filename)

print(super_group_list)
print("/",number_of_groups)