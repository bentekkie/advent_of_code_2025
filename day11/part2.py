#!/usr/bin/env python3
from collections import defaultdict, deque

inp = "input.txt"

adj = defaultdict(list)

with open(inp, "r") as f:
    for line in f:
        frm, tos = line.strip().split(": ")
        tos = tos.split(" ")
        adj[frm] = tos


def countPaths(graph, source, destination):
    indegree = defaultdict(int)
    for u, vs in graph.items():
        for v in vs:
            indegree[v] += 1
    q = deque(i for i in graph if indegree[i] == 0)
    topoOrder = []
    while q:
        node = q.popleft()
        topoOrder.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    ways = defaultdict(int, {source: 1})
    for node in topoOrder:
        for neighbor in graph[node]:
            ways[neighbor] += ways[node]
    return ways[destination]


def removenodes(adj, nodes):
    return defaultdict(
        list,
        {
            u: [v for v in vs if v not in nodes]
            for u, vs in adj.items()
            if u not in nodes
        },
    )


nodac = removenodes(adj, {"dac"})
nofft = removenodes(adj, {"fft"})
noboth = removenodes(adj, {"fft", "dac"})
waysall = countPaths(adj, "svr", "out")
waysnofft = countPaths(nofft, "svr", "out")
waysnodac = countPaths(nodac, "svr", "out")
waysnoboth = countPaths(noboth, "svr", "out")
multi = waysall + waysnoboth - waysnofft - waysnodac
print("part2", multi)
