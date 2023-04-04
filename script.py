import argparse
import sys

dataset = sys.argv[1]

print(dataset)

# Choose dataset based on argument
def choose(dataset):
    if dataset == "cat":
        print("cat")
    elif dataset == "dog":
        print("dog")
    elif dataset =="ship":
        print("ship")
    elif dataset =="car":
        print("car")
    else:
        print(f"Unknown dataset: {dataset}")

choose(dataset)
