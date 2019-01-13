# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 15:04:37 2018

@author: Zhou
"""

import numpy as np
from heapq import *
from time import clock

def dijkstra(graph, start):
    dist = graph[start,:].copy()
    visited = np.zeros(graph.shape[1]) #初始化已访问顶点集合
    visited[start] = 1
    previous = np.empty(graph.shape[1],int) #初始化路径
    previous[dist != np.inf] = start
    previous[dist == np.inf] = -1
    for i in range(graph.shape[1] - 1):
        unvisited = np.nonzero(visited == 0)[0] #找出未访问顶点中最近的
        closest = unvisited[dist[unvisited].argmin()]
        visited[closest] = 1 #加入已访问集合
        for j, dist_cj in enumerate(graph[closest]): #修改到集合外各点的距离
            if visited[j] == 0 and dist_cj != np.inf and dist[closest] + dist_cj < dist[j]:
                dist[j] = dist[closest] + dist_cj
                previous[j] = closest
    return dist, previous

class vertex():
    def __init__(self, i, dist):
        self.i = i
        self.dist = dist
    
    def __lt__(self, x):
        return self.dist < x.dist

def dijkstra_heap(graph, start):
    dist = np.empty(graph.shape[1])
    dist[:] = np.inf; dist[start] = 0
    visited = np.zeros(graph.shape[1])
    previous = np.empty(graph.shape[1],int)
    previous[graph[start,:] != np.inf] = start
    previous[graph[start,:] == np.inf] = -1
    heap = [vertex(start, np.inf)]
    while heap:
        closest = heappop(heap)
        if visited[closest.i]: continue
        visited[closest.i] = 1
        for j, dist_cj in enumerate(graph[closest.i]):
            if visited[j] == 0 and dist_cj != np.inf and dist[closest.i] + dist_cj < dist[j]:
                dist[j] = dist[closest.i] + dist_cj
                previous[j] = closest.i
                heappush(heap, vertex(j, dist[j]))
    return dist, previous
        

def showPath(dist, previous, start, end): #输出路径
    if previous[end] == -1:
        print('无路径！')
        return
    print('从顶点{:2}到顶点{:2}的路径长度为：{:2.2f}'.format(start, end, dist[end]))
    path = []
    vertex = end
    while vertex != -1:
        path.append(vertex)
        vertex = previous[vertex]
    path.reverse()
    print('路径为{}'.format(path))
    
def createGraph(numVertex):
    graph = np.random.rand(numVertex,numVertex) * 10
    graph = np.triu(graph)
    graph += graph.T
    i=np.arange(graph.shape[1])
    graph[i,i] = np.inf
    graph[graph > 8] = np.inf
    return graph


graph = np.array([[np.inf,4,6,6,np.inf,np.inf,np.inf],
                 [4,np.inf,1,7,np.inf,np.inf,np.inf],
                 [np.inf,np.inf,np.inf,np.inf,6,4,np.inf],
                 [np.inf,np.inf,2,np.inf,np.inf,5,np.inf],
                 [np.inf,np.inf,np.inf,np.inf,np.inf,np.inf,6],
                 [np.inf,np.inf,np.inf,np.inf,1,np.inf,8],
                 [np.inf,np.inf,np.inf,np.inf,np.inf,np.inf,np.inf]])
dist,previous = dijkstra_heap(graph,0)
showPath(dist, previous, 0, 6)
    
a=createGraph(1000)
tib = clock()
dijkstra(a,0)
tie = clock()
print('未优化用时: {}ms'.format(1000*(tie-tib)))
tib = clock()
dijkstra_heap(a,0)
tie = clock()
print('优化后用时: {}ms'.format(1000*(tie-tib)))