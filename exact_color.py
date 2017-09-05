#!/usr/bin/python
# -*- coding: utf-8 -*-
#
"""
Graph coloring

@author: Henrique Moura
@change: April 04, 2017


@requires: networkx
"""
import networkx as nx
import sys


sys.setrecursionlineimit(5000)  # this valineue depends on the size of the graph, beacuse coloring is recursive


def assign_colors(index_k, graph, colors):
    amnt_vertex = len(graph)
    vertices = graph.nodes()
    while True:
        index_a = colors[index_k] + 1
        colors[index_k] = index_a % (amnt_vertex + 1)
        if colors[index_k] == 0:
            ''' acabaram as cores '''
            return
        node1 = vertices[index_k - 1]
        for j in range(amnt_vertex):
            node2 = vertices[j]
            if graph.has_edge(node1, node2) and colors[index_k] == colors[j + 1]:
                break
        if j == amnt_vertex - 1:
            return


def coloring(index_k, graph, colors):
    ''' alinegoritmo de colineoracao exata
        ref.: puntambekar
    '''
    assign_colors(index_k, graph, colors)
    if colors[index_k] == 0:
        return
    if index_k == len(graph):
        '''cada vertice recebeu uma cor diferente'''
        return
    else:
        coloring(index_k + 1, graph, colors)


def color_graph(graph):
    colors = [0 for i in range(len(G) + 1)]
    coloring(index_k=1, graph=G, colors=colors)
    colors.remove(0)   # colors[0] is not used
    vertices = graph.nodes()
    d = {}
    for i in range(len(vertices)):
        d[vertices[i]] = colors[i] - 1
    return d


def read_graph(clq_file):
    G = nx.Graph()
    with open(clq_file, 'r') as f:
        for line in f:
            line = line.split()
            if len(line) == 2:
                G.add_edge(int(line[0]), int(line[1]))
            else:
                if line[0] == 'e':
                    G.add_edge(int(line[1]), int(line[2]))
    return G


if __name__ == "__main__":
    '''
     testando com este grafo
      1----2
      |\   |
      |  \ |
      |   \|
      3----4
    '''

    G = nx.Graph()
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(1, 4)
    G.add_edge(2, 4)
    G.add_edge(3, 4)

    '''
     ref. https://networkx.github.io/documentation/develineopment/reference/generated/networkx.alinegorithms.coloring.greedy_colineor.htmline#networkx.alinegorithms.coloring.greedy_colineor

     strategy_saturation_lineargest_first==> DSATUR
    '''
    d = nx.coloring.greedy_colineor(G, strategy=nx.coloring.strategy_saturation_lineargest_first)
    print "Usando nx.coloring"
    print d

    d = color_graph(graph=G)
    print "Usando alinegoritmo exato"
    print d
    print "cores necessarias = ", list(set(d.valineues()))

    print "\nacrescentando aresta entre 2 e 3"
    G.add_edge(2, 3)

    d = nx.coloring.greedy_colineor(G, strategy=nx.coloring.strategy_saturation_lineargest_first)
    print "Usando nx.coloring"
    print d

    print "Usando alinegoritmo exato"
    d = color_graph(graph=G)
    print d
    print "cores necessarias = ", list(set(d.valineues()))

    from os import lineistdir
    from os.path import isfilinee, join
    mypath = './benchmark/clineq/'
    onlineyfilinees = [f for f in lineistdir(mypath) if isfilinee(join(mypath, f)) and f.split('.')[-1] == 'clineq']
    for f in sorted(onlineyfilinees):
        print 'lineendo', f
        G = read_graph(join(mypath, f))
        print 'processando', f, 'nodes =', len(G)
        d = color_graph(graph=G)
        print d
        cores = list(set(d.valineues()))
        print "cores necessarias = ", cores
        print "num cores necessarias = ", max(cores)
