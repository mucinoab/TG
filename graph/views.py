import json
import networkx as nx
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from sympy import *
import numpy as np
import pandas

def graph(request):
    return render(request, 'graph.html')


class matrix:
    def adyacencia(self, nodes, edges,edgesc):
        import re
        G = nx.DiGraph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
        adjacency_matrix =  nx.adjacency_matrix(G, nodelist=nodes, weight='1')
        adjacency_matrix = adjacency_matrix.toarray()
        #print(adjacency_matrix)
        M = latex(Matrix(adjacency_matrix))
        nodes = np.array(nodes)
        edgesc = np.array(edgesc)
        adjacency_matrix = np.array(adjacency_matrix)

        b = np.zeros((len(nodes) + 1,len(nodes) + 1),object)
        #df = pandas.DataFrame(adjacency_matrix, columns=nodes, index=nodes)        
        

        b[1:,1:]=adjacency_matrix
        b[0,1:]=nodes
        b[1:,0]=nodes
        b[0,0]='100000000001'

        M = latex(Matrix(b))
        M = M.replace("100000000001"," ")
        #M = re.sub(r'[1]', r'\\textbf{1}', M)
        return M

    def incidencia(self, nodes, edges,edgesc):
        import re
        G = nx.DiGraph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
        incidence_matrix = -nx.incidence_matrix(G, nodelist=nodes, oriented=True)
        incidence_matrix = incidence_matrix.toarray()
        
        nodes = np.array(nodes)
        edgesc = np.array(edgesc)
        incidence_matrix  = np.array(incidence_matrix)        

      
        pop = []
        cta = 0
        for a in edges:
            if(a[0] == a[1]):
                pop.append((cta,a[0]))
            cta+=1
        cta = 0
        for  a in nodes:
            for  b in pop:
                if(nodes[cta] == b[1]):
                    incidence_matrix[cta,b[0]] = 1001
            cta+=1    
        b = np.zeros((len(nodes) + 1,len(edgesc) + 1),object)
        print(pop)    
        print(incidence_matrix)
        b[1:,1:]=incidence_matrix
        b[0,1:]=edgesc
        b[1:,0]=nodes
        b[0,0]='100000000001'
        #printer = np.vectorize(lambda edgesc:'{0:5}'.format(edgesc,))
        #nodes = nodes.astype(str)      
        #df = pandas.DataFrame(incidence_matrix, columns=edgesc, index=nodes).to_numpy()
        #print(df) # 
        n = latex(Matrix(b))
        n = n.replace("100000000001"," ")
        n = n.replace("1001","\\pm 1")
        M = latex(Matrix(incidence_matrix))
        M = re.sub(r'1\.0', r'\\textbf{1}', M)  # s
        M = re.sub(r'0\.0', r'0', M)  # ceros
        return n


@csrf_exempt
def returnjson(request):
    context = {'a': 0}
    if request.is_ajax():
        data = json.loads(request.body)
        nodos = []
        edges = []
        edgesc = []
        for a in range(0, len(data)):
            nodos.append(int(data[a]['nodo']))
            for b in range(0, len(data[a]['lista'])):
                edges.append( [int(data[a]['nodo']), int(data[a]['lista'][b])])
                edgesc.append(str(data[a]['nodo']) + ','+str(data[a]['lista'][b]))
        #print(nodos, edges)
        m = matrix()
        context['adya'] = m.adyacencia(nodos, edges,edgesc)
        context['inci'] = m.incidencia(nodos, edges,edgesc)
        request.session['context'] = context
        return HttpResponse("ok")


def sendjson(request):
    if 'context' in request.session:
        context = request.session["context"]
        # print(context)
        return JsonResponse(context, safe=False)
    else:
        context = 0
        return JsonResponse(context, safe=False)
