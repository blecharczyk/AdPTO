from dimacs import *
import myApproxFunctions
import datetime



#Divided in order to run parallel
graphs = [
("e5"),
("e10"),
("e20"),
("e40"),
("e150"),
("s25"),
("s50"),
("s500"),
("b20"),
("b30"),
("b100"),
("k330_a"),
("k330_b"),
("k330_c"),
("k330_d"),
("k330_e"),
("k330_f"),
("f30"),
("f35"),
("f40"),
("f56"),
("m20"),
("m30"),
("m40"),
("m50"),
("m100"),
("p20"),
("p35"),
("p60"),
("p150"),
("p200"),
("r30_01"),
("r30_05"),
("r50_001"),
("r50_01"),
("r50_05"),
("r100_005"),
("r100_01"),
("r200_001"),
("r200_005")
]

for graph in graphs:
  s = "graph/" + graph
  G = loadGraph(s)
  Edg = edgeList(G)
  filename = s + ".sol"
  S3 = myApproxFunctions.approx_with_2_factor(G)
  print(len(S3), " ", s, isVC(Edg, S3), datetime.datetime.now())
  saveSolution(filename, S3)






