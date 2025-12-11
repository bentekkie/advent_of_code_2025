#!/usr/bin/env python3
import networkx as nx

g = nx.DiGraph()

inp = "input.txt"

with open(inp, "r") as f:
    for line in f:
        frm, tos = line.strip().split(": ")
        tos = tos.split(" ")
        for to in tos:
            g.add_edge(frm, to)

paths = nx.all_simple_paths(g, "you", "out")


print("part1", len(list(paths)))
