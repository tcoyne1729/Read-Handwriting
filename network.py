import numpy as np

class Network(object):
    """Create a neural network with a list [a,b,c,...,d] which gives a inputs, d outputs and all others are the number of neurons at each other level"""
    
    def __init__(self,nodes):
        self.layers = len(nodes)
        self.neuronlist = nodes
		#new content
