from rdflib import Graph, URIRef, RDF, Namespace, BNode
# task 1

# 1.1

brassGraph = Graph()

EX = Namespace('https://example.org/')

brassGraph.bind('ex', EX)

brass = URIRef('https://dbpedia.org/resource/Brass')
copper = URIRef('https://dbpedia.org/resource/Copper')
zinc = URIRef('https://dbpedia.org/resource/Zinc')
alloy = URIRef('https://dbpedia.org/page/Alloy')
brass_consists_of = BNode('consists_of')

brassGraph.add((brass, RDF.type, alloy))
brassGraph.add((brass, EX['consists_of'], brass_consists_of))

brassGraph.add((brass_consists_of, RDF.type, RDF.Seq))
brassGraph.add((brass_consists_of, RDF['_1'], zinc))
brassGraph.add((brass_consists_of, RDF['_2'], copper))

# print(brassGraph.serialize(format='ttl'))

# 1.2




