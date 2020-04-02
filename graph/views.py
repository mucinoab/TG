from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import networkx as nx
import json 

def graph(request):
    return render(request,'graph.html')
class matrix:
    def adyacencia(self,nodes,edges):
        G = nx.DiGraph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)        
        incidence_matrix = nx.incidence_matrix(G,nodelist= nodes, oriented=True) 
        adjacency_matrix = nx.adjacency_matrix(G,nodelist=nodes,weight = '1')
        print(incidence_matrix.toarray())
        print(A.toarray())

@csrf_exempt
def returnjson(request):
    if request.is_ajax():
        data = json.loads(request.body)
        nodos  = []
        edges = []
        for a in range (0,len(data)):
            nodos.append(data[a]['nodo'])
            for b in range(0,len(data[a]['lista'])):
                edges.append([data[a]['nodo'],   data[a]['lista'][b]])
        print(edges)
        print(nodos)
        ady = matrix()
        ady.adyacencia(nodos,edges)
        return HttpResponse("ok")


