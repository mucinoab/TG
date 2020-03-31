from django.shortcuts import render
from networkx import networkx as nx
import matplotlib.pyplot as plt

# Create your views here.
def inicio_views (request):
    return render (request,'graph.html')

def grafica():
	G = nx.Graph()
	G.add_edges_from([(1, 2), (1, 3)])
	


