import sys, os 
import subprocess
from nltk.corpus import wordnet

#accept user input
def get_user_input():
	print(sys.argv[1])

#return dependency tree
def create_dependency_tree():
	arg_list = sys.argv
	arg_list.pop(0)
	str1 = ' '.join(arg_list)
	p = subprocess.Popen("echo " + str1 + "| syntaxnet/demo.sh", stdout=subprocess.PIPE, shell=True)
	out = p.stdout.read()
	deptree = out.splitlines()
	return deptree

#retrieve root word and dependent object
def get_root_word(dependency_tree):
	root = dependency_tree[2].split()[0]
	return root

def get_dependent_object(dependency_tree):
	dobj = dependency_tree[3].split()[1]
	return dobj

#retrieve synonym for root word
def get_synonym(root):
	listofsyns = wordnet.synsets(root)
	synonym = listofsyns[3].name().split(".")[0]
	return synonym
