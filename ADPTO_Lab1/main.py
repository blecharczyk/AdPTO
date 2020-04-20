from dimacs import *
from itertools import *
import numpy as np
import myFunctions

#Divided in order to run parallel
graphs = [
("e5"),
("e10"),
("e20"),
("e40"),
("e150"),]
graphs2 = [
("s25"),
("s50"),
("s500"),]
graphs3 = [
("b20"),
("b30"),
("b100"),
("k330_a"),
("k330_b"),
("k330_c"),]
graphs4 = [
("m20"),
("m30"),
("m40"),
("m50"),
("m100"),]
graphs5 = [
("p20"),
("p35"),
("p60"),
("p150"),]
("r30_01"),
("r30_05"),
("r50_001"),
("r50_01"),
("r50_05"),
("r100_005"),


for graph in graphs2:
  s = "graph/" + graph
  G = loadGraph(s)
  Edg = edgeList(G)
  for i in range (len(G)):
    filename = s + ".sol"
    Dd = set()
    S3 = myFunctions.betterVC(G, i, Dd)
    if(S3!=None):
      print(S3, " ", s)
      saveSolution(filename, S3)
      break






