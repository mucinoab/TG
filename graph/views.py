from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from sympy import *
import networkx as nx
import json 
import numpy as np

init_printing(use_unicode=True)
def graph(request):
    return render(request,'graph.html')
class matrix:
    def adyacencia(self,nodes,edges):
        G = nx.DiGraph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)        
        adjacency_matrix = nx.adjacency_matrix(G,nodelist=nodes,weight = '1')
        adjacency_matrix = adjacency_matrix.toarray()
        M = Matrix(adjacency_matrix)
        return(latex(M))

    def incidencia(self,nodes,edges):
        G = nx.DiGraph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)      
        incidence_matrix = nx.incidence_matrix(G,nodelist= nodes, oriented=True) 
        incidence_matrix = incidence_matrix.toarray()
        M = Matrix(incidence_matrix)
        return(latex(M))
        #print(incidence_matrix.toarray())


@csrf_exempt
def returnjson(request):
    context = {'a':0}
    if request.is_ajax():
        data = json.loads(request.body)
        nodos  = []
        edges = []
        for a in range (0,len(data)):
            nodos.append(data[a]['nodo'])
            for b in range(0,len(data[a]['lista'])):
                edges.append([data[a]['nodo'],   data[a]['lista'][b]])
        m = matrix()
        context['adya'] = m.adyacencia(nodos,edges)
        context['inci'] = m.incidencia(nodos,edges)
        request.session['context'] = context
        return HttpResponse("ok")

def sendjson(request):
    context = request.session["context"]
    print(context)
    return JsonResponse(context,safe=False) 