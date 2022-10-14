from rdflib import Graph, URIRef, RDF, Namespace, BNode, Literal, FOAF

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

# 1.5
# Олена каже, що її друг живе в Києві

messageGraph = Graph()
message = EX['message_1']
olena = EX['olena']
olena_friend = EX['olena\'s_friend']
information_chunk = BNode('information_chunk')

messageGraph.bind('ex', EX)

messageGraph.add((olena, EX['says'], message))
messageGraph.add((olena, FOAF.knows, olena_friend))
messageGraph.add((olena_friend, FOAF.knows, olena))
messageGraph.add((message, EX['author'], olena))
messageGraph.add((message, EX['contains'], information_chunk))
messageGraph.add((information_chunk, EX['about'], olena_friend))
messageGraph.add((information_chunk, EX['contents'], Literal('My friend lives in Kyiv', lang='en')))

print(messageGraph.serialize(format='ttl'))

# 1.6
# Стефан думає, що Анна знає, що він знає її батька.

stephanAnnaGraph = Graph()
stephan = EX['stephan']
anna = EX['anna']
anna_father = EX['anna_father']
assumption = EX['assumption']
assumption_contents = EX['assumption_contents']
possibility = EX['possibility']
assumption_about = BNode('assumption_about')
possibility_about = BNode('possibility_about')

stephanAnnaGraph.bind('ex', EX)

stephanAnnaGraph.add((assumption, EX['about'], assumption_about))
stephanAnnaGraph.add((assumption_about, RDF.type, RDF.Bag))
stephanAnnaGraph.add((assumption_about, RDF['_1'], stephan))
stephanAnnaGraph.add((assumption_about, RDF['_2'], anna_father))
stephanAnnaGraph.add((assumption, EX['contents'], Literal('Stephan knows my father', lang='en')))
stephanAnnaGraph.add((anna, EX['assumes'], assumption))
stephanAnnaGraph.add((possibility, EX['content'], Literal('Anna knows that I know', lang='en')))
stephanAnnaGraph.add((possibility_about, RDF.type, RDF.Bag))
stephanAnnaGraph.add((possibility_about, RDF['_1'], anna))
stephanAnnaGraph.add((possibility_about, RDF['_2'], assumption))
stephanAnnaGraph.add((possibility, EX['about'], possibility_about))
stephanAnnaGraph.add((stephan, EX['thinks_about'], possibility))

print(stephanAnnaGraph.serialize(format='ttl'))

# 1.7
# Іван знає, що Рим є столицею Італії.

romeGraph = Graph()

romeGraph.bind('ex', EX)

ivan = EX['ivan']
fact = EX['fact_1']
rome = URIRef(DBR['Rome'])
italy = URIRef(DBR['Italy'])

romeGraph.add((fact, EX['subject'], rome))
romeGraph.add((fact, EX['object'], italy))
romeGraph.add((fact, RDF.type, EX['capital']))
romeGraph.add((ivan, EX['knows_about'], fact))

print(romeGraph.serialize(format='ttl'))