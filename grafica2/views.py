from django.shortcuts import render
import json

import networkx as nx
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from sympy import *


def grafica2(request):
    return render(request, 'grafica2.html')


class matrix:
    def adyacencia(self, nodes, edges):
        import re
        G = nx.DiGraph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
        adjacency_matrix = nx.adjacency_matrix(G, nodelist=nodes, weight='1')
        adjacency_matrix = adjacency_matrix.toarray()
        M = latex(Matrix(adjacency_matrix))
        M = re.sub(r'[1]', r'\\textbf{1}', M)

        return M

    def incidencia(self, nodes, edges):
        import re
        G = nx.DiGraph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
        incidence_matrix = nx.incidence_matrix(G, nodelist=nodes, oriented=True)
        incidence_matrix = incidence_matrix.toarray()
        M = latex(Matrix(incidence_matrix))
        M = re.sub(r'1\.0', r'\\textbf{1}', M)  # s
        M = re.sub(r'0\.0', r'0', M)  # ceros

        return M


@csrf_exempt
def returnjson(request):
    context = {'a': 0}
    if request.is_ajax():
        data = json.loads(request.body)
        nodos = []
        edges = []
        for a in range(0, len(data)):
            nodos.append(data[a]['nodo'])
            for b in range(0, len(data[a]['lista'])):
                edges.append([data[a]['nodo'], data[a]['lista'][b]])
        # print(nodos, edges)
        m = matrix()
        context['adya'] = m.adyacencia(nodos, edges)
        context['inci'] = m.incidencia(nodos, edges)
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
