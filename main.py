from rdflib import Graph, URIRef, RDF, Namespace, BNode, Literal

# assignment 1

# Setup

DBR = Namespace('https://dbpedia.org/resource/')

# 1.1
# Латунь – це сплав міді та цинку

brassGraph = Graph()

EX = Namespace('https://example.org/')

brassGraph.bind('ex', EX)

brass = URIRef('https://dbpedia.org/resource/Brass')
copper = URIRef('https://dbpedia.org/resource/Copper')
zinc = URIRef('https://dbpedia.org/resource/Zinc')
alloy = URIRef('https://dbpedia.org/resource/Alloy')
brass_consists_of = BNode('consists_of')

brassGraph.add((brass, RDF.type, alloy))
brassGraph.add((brass, EX['consists_of'], brass_consists_of))

brassGraph.add((brass_consists_of, RDF.type, RDF.Seq))
brassGraph.add((brass_consists_of, RDF['_1'], zinc))
brassGraph.add((brass_consists_of, RDF['_2'], copper))

# print(brassGraph.serialize(format='ttl'))

# 1.2
# SPIEGEL — німецький інформаційний журнал зі штаб-квартирою в Гамбурзі.

spiegelGraph = Graph()

spiegelGraph.bind('ex', EX)

spiegel = URIRef('https://dbpedia.org/resource/Der_Spiegel_(online)')
magazine = URIRef('https://dbpedia.org/resource/Magazine')
news = URIRef('https://dbpedia.org/resource/News')
hamburg = URIRef('https://dbpedia.org/resource/Hamburg')

spiegelGraph.add((spiegel, RDF.type, magazine))
spiegelGraph.add((spiegel, EX['genre'], news))
spiegelGraph.add((spiegel, EX['headquarters_in'], hamburg))

print(spiegelGraph.serialize(format='ttl'))

# 1.3
# Есе складається зі вступу, основної частини та висновку.

essay = URIRef(DBR['Essay'])
essay_consists_of = BNode('consists_of');
essayGraph = Graph()

essayGraph.bind('ex', EX)

essayGraph.add((essay, EX['consists_of'], essay_consists_of))
essayGraph.add((essay_consists_of, RDF.type, RDF.Seq))
essayGraph.add((essay_consists_of, RDF['_1'], EX['introduction']))
essayGraph.add((essay_consists_of, RDF['_2'], EX['main_part']))
essayGraph.add((essay_consists_of, RDF['_3'], EX['conclusion']))

print(essayGraph.serialize(format='ttl'))

# 1.4
# Павло знає, що Олена живе в Полтаві.

knowledgeGraph = Graph()
fact = EX['fact_1']
fact_translations = BNode('fact_translations')

knowledgeGraph.bind('ex', EX)

knowledgeGraph.add((fact, EX['translations'], fact_translations))
knowledgeGraph.add((fact_translations, RDF.type, RDF.Bag))
knowledgeGraph.add((fact_translations, RDF['_1'], Literal('Olena lives in Poltava', lang='en')))
knowledgeGraph.add((fact_translations, RDF['_2'], Literal('Олена проживає у Полтаві', lang='uk')))
knowledgeGraph.add((EX['paul'], EX['knows'], fact))

print(knowledgeGraph.serialize(format='ttl'))

