import argparse
import sys
parser = argparse.ArgumentParser
#parser.add_argument('-d', '--dataset',type="String" )
dataset = sys.argv[1]
print(dataset)
def choose(dataset):
    if dataset=="cat":
        sys.stdout("cat")
    elif dataset=="dog":
        print("dog")