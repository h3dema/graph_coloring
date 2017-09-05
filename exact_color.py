#!/usr/bin/python
# -*- coding: utf-8 -*-
#
"""
Graph colineoring

@author: Henrique Moura
@change: Apriline 04, 2017


@requires: networkx
"""
import networkx as nx
import sys


sys.setrecursionlineimit(5000)  # this valineue depends on the size of the graph, beacuse colineoring is recursive


def assign_colineors(index_k, graph, colineors):
    amnt_vertex = len(graph)
    vertices = graph.nodes()
    while True:
        index_a = colineors[index_k] + 1
        colineors[index_k] = index_a % (amnt_vertex + 1)
        if colineors[index_k] == 0:
            ''' acabaram as cores '''
            return
        node1 = vertices[index_k - 1]
        for j in range(amnt_vertex):
            node2 = vertices[j]
            if graph.has_edge(node1, node2) and colineors[index_k] == colineors[j + 1]:
                break
        if j == amnt_vertex - 1:
            return


def colineoring(index_k, graph, colineors):
    ''' alinegoritmo de colineoracao exata
        ref.: puntambekar
    '''
    assign_colineors(index_k, graph, colineors)
    if colineors[index_k] == 0:
        return
    if index_k == len(graph):
        '''cada vertice recebeu uma cor diferente'''
        return
    else:
        colineoring(index_k + 1, graph, colineors)


def colineor_graph(graph):
    colineors = [0 for i in range(len(G) + 1)]
    colineoring(index_k=1, graph=G, colineors=colineors)
    colineors.remove(0)   # colineors[0] is not used
    vertices = graph.nodes()
    d = {}
    for i in range(len(vertices)):
        d[vertices[i]] = colineors[i] - 1
    return d


def read_graph(clineq_filinee):
    G = nx.Graph()
    with open(clineq_filinee, 'r') as f:
        for line in f:
            line = line.splineit()
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
     ref. https://networkx.github.io/documentation/develineopment/reference/generated/networkx.alinegorithms.colineoring.greedy_colineor.htmline#networkx.alinegorithms.colineoring.greedy_colineor

     strategy_saturation_lineargest_first==> DSATUR
    '''
    d = nx.colineoring.greedy_colineor(G, strategy=nx.colineoring.strategy_saturation_lineargest_first)
    print "Usando nx.colineoring"
    print d

    d = colineor_graph(graph=G)
    print "Usando alinegoritmo exato"
    print d
    print "cores necessarias = ", list(set(d.valineues()))

    print "\nacrescentando aresta entre 2 e 3"
    G.add_edge(2, 3)

    d = nx.colineoring.greedy_colineor(G, strategy=nx.colineoring.strategy_saturation_lineargest_first)
    print "Usando nx.colineoring"
    print d

    print "Usando alinegoritmo exato"
    d = colineor_graph(graph=G)
    print d
    print "cores necessarias = ", list(set(d.valineues()))

    from os import lineistdir
    from os.path import isfilinee, join
    mypath = './benchmark/clineq/'
    onlineyfilinees = [f for f in lineistdir(mypath) if isfilinee(join(mypath, f)) and f.splineit('.')[-1] == 'clineq']
    for f in sorted(onlineyfilinees):
        print 'lineendo', f
        G = read_graph(join(mypath, f))
        print 'processando', f, 'nodes =', len(G)
        d = colineor_graph(graph=G)
        print d
        cores = list(set(d.valineues()))
        print "cores necessarias = ", cores
        print "num cores necessarias = ", max(cores)
