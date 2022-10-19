from rdflib import Graph, URIRef, RDF, Namespace, BNode, Literal, FOAF, XSD
import os

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

# 3
taskThreeGraph = Graph()

# Namespace binding
taskThreeGraph.bind('ex', EX)
taskThreeGraph.bind('dbr', DBR)
taskThreeGraph.bind('foaf', FOAF)

# cade
cade = EX['cade']
cadeHomeAddress = BNode('cade_home_address')
cadeEducation = BNode('cade_education')
cadeFieldOfInterest = BNode('cade_field_of_interest')
cadeFieldOfInterestBag = BNode('cade_field_of_interest_bag')
cadeTravelHistory = BNode('cade_travel_history')
cadeTravelHistorySeq = BNode('cade_travel_history_seq')

# emma
emma = EX['emma']
emmaHomeAddress = BNode('emma_home_address')
emmaEducation = BNode('emma_education')
emmaFieldOfStudy = BNode('emma_field_of_study')
emmaFieldOfStudyBag = BNode('emma_field_of_study_bag')
emmaFieldOfInterest = BNode('emma_field_of_interest')
emmaFieldOfInterestBag = BNode('emma_field_of_interest_bag')
emmaTravelHistory = BNode('emma_travel_history')
emmaTravelHistorySeq = BNode('emma_travel_history_seq')

# emma-cade relationship
emmaCadeRelationship = BNode('emma_cade_relationship')

# countries
france = DBR['France']

# cities
paris = DBR['Paris']

# cade
taskThreeGraph.add((cade, RDF.type, FOAF.Person))
taskThreeGraph.add((cade, FOAF.name, Literal('Cade', lang='en')))

# cade home address
taskThreeGraph.add((cade, EX['home_address'], cadeHomeAddress))
taskThreeGraph.add((cadeHomeAddress, EX['home_address_line'], Literal('1516 Henry Street, 94709', lang='en')))
taskThreeGraph.add((cadeHomeAddress, EX['home_city'], DBR['Berkley,_Michigan']))
taskThreeGraph.add((cadeHomeAddress, EX['home_country'], DBR['United_States']))

# cade education
taskThreeGraph.add((cadeEducation, EX['education_title'], DBR['Bachelor_of_Science']))
taskThreeGraph.add((cadeEducation, EX['education_specialty'], DBR['Biology']))
taskThreeGraph.add((cadeEducation, EX['education_place_of_study'], DBR['University_of_California,_Berkeley']))
taskThreeGraph.add((cadeEducation, EX['education_graduate_year'], Literal('2011', datatype=XSD.gYear)))
taskThreeGraph.add((cade, EX['education'], cadeEducation))

# cade fieldOfInterest
taskThreeGraph.add((cadeFieldOfInterestBag, RDF.type, RDF.Bag))
taskThreeGraph.add((cadeFieldOfInterestBag, RDF['_1'], DBR['Bird']))
taskThreeGraph.add((cadeFieldOfInterestBag, RDF['_2'], DBR['Ecology']))
taskThreeGraph.add((cadeFieldOfInterestBag, RDF['_3'], DBR['Natural_environment']))
taskThreeGraph.add((cadeFieldOfInterestBag, RDF['_4'], DBR['Photography']))
taskThreeGraph.add((cadeFieldOfInterestBag, RDF['_5'], DBR['Travel']))
taskThreeGraph.add((cade, FOAF.interest, cadeFieldOfInterestBag))

# cade travelHistory
taskThreeGraph.add((cadeTravelHistorySeq, RDF.type, RDF.Seq))
taskThreeGraph.add((cadeTravelHistorySeq, RDF['_1'], DBR['Canada']))
taskThreeGraph.add((cadeTravelHistorySeq, RDF['_2'], DBR['France']))
taskThreeGraph.add((cade, EX['travel_history'], cadeTravelHistorySeq))

# emma
taskThreeGraph.add((emma, RDF.type, FOAF.Person))
taskThreeGraph.add((emma, FOAF.name, Literal('Emma', lang='en')))

# emma home address
taskThreeGraph.add((emma, EX['home_address'], emmaHomeAddress))
taskThreeGraph.add((emmaHomeAddress, EX['home_address_line'], Literal('Carrer de la Guardia Civil 20, 46020', lang='en')))
taskThreeGraph.add((emmaHomeAddress, EX['home_city'], DBR['Valencia']))
taskThreeGraph.add((emmaHomeAddress, EX['home_country'], DBR['Spain']))

# emma education
taskThreeGraph.add((emmaEducation, EX['education_title'], DBR['Master_of_Science']))
taskThreeGraph.add((emmaEducation, EX['education_specialty'], DBR['Chemistry']))
taskThreeGraph.add((emmaEducation, EX['education_place_of_study'], DBR['University_of_Valencia']))
taskThreeGraph.add((emmaEducation, EX['education_graduate_year'], Literal('2015', datatype=XSD.gYear)))
taskThreeGraph.add((emma, EX['education'], emmaEducation))

# emma fieldOfStudy
taskThreeGraph.add((emmaFieldOfStudyBag, RDF.type, RDF.Bag))
taskThreeGraph.add((emmaFieldOfStudyBag, RDF['_1'], DBR['Recycling']))
taskThreeGraph.add((emmaFieldOfStudyBag, RDF['_2'], DBR['Toxic_waste']))
taskThreeGraph.add((emmaFieldOfStudyBag, RDF['_3'], DBR['Air_pollution']))
taskThreeGraph.add((emma, EX['field_of_study'], emmaFieldOfStudyBag))

# emma fieldOfInterest
taskThreeGraph.add((emmaFieldOfInterestBag, RDF.type, RDF.Bag))
taskThreeGraph.add((emmaFieldOfInterestBag, RDF['_1'], DBR['Cycling']))
taskThreeGraph.add((emmaFieldOfInterestBag, RDF['_2'], EX['Music']))
taskThreeGraph.add((emmaFieldOfInterestBag, RDF['_3'], DBR['Travel']))
taskThreeGraph.add((emma, FOAF.interest, emmaFieldOfInterestBag))

# emma travelHistory
taskThreeGraph.add((emmaTravelHistorySeq, RDF.type, RDF.Seq))
taskThreeGraph.add((emmaTravelHistorySeq, RDF['_1'], DBR['Portugal']))
taskThreeGraph.add((emmaTravelHistorySeq, RDF['_2'], DBR['Italy']))
taskThreeGraph.add((emmaTravelHistorySeq, RDF['_3'], france))
taskThreeGraph.add((emmaTravelHistorySeq, RDF['_4'], DBR['Germany']))
taskThreeGraph.add((emmaTravelHistorySeq, RDF['_5'], DBR['Denmark']))
taskThreeGraph.add((emmaTravelHistorySeq, RDF['_6'], DBR['Sweden']))
taskThreeGraph.add((emma, EX['travel_history'], emmaTravelHistorySeq))

# countries
taskThreeGraph.add((france, EX['capital_in'], paris))

# cade - emma relationship
taskThreeGraph.add((cade, FOAF.knows, emma))
taskThreeGraph.add((emma, FOAF.knows, cade))

taskThreeGraph.add((cade, EX['in_relationship'], emmaCadeRelationship))
taskThreeGraph.add((emma, EX['in_relationship'], emmaCadeRelationship))

taskThreeGraph.add((emmaCadeRelationship, EX['met_in_place'], paris))
taskThreeGraph.add((emmaCadeRelationship, EX['met_on_date'], Literal('2014-08', datatype=XSD.gYearMonth)))

# additional changes

taskThreeGraph.add((emma, FOAF.birthday, Literal('1986-10', datatype=XSD.gYearMonth)))
taskThreeGraph.add((cadeTravelHistorySeq, RDF['_3'], DBR['Germany']))

# output

fileFormat = 'ttl'
taskThreeGraphSerialized = taskThreeGraph.serialize(format=fileFormat)
taskThreeFileName = f'task-three-graph.{fileFormat}'

# print(taskThreeGraph.serialize(format='json-ld'))
# print(taskThreeGraph.serialize(format='xml'))
# print(taskThreeGraph.serialize(format='n3'))
# print(taskThreeGraph.serialize(format='ttl'))

if os.path.exists(taskThreeFileName):
    os.remove(taskThreeFileName)

f = open(taskThreeFileName, 'a')
f.write(taskThreeGraphSerialized)
f.close()

# print all the triplets to the console
for s, p, o in taskThreeGraph:
    print(s, p, o)

# print all the triplets to the console concerning emma
# subject, predicate, object
for s, p, o in taskThreeGraph:
    if s == emma:
        print(s, p, o)

# print all the names in the graph
# subject, predicate, subject
for person in taskThreeGraph.subjects(RDF.type, FOAF.Person):
    for name in taskThreeGraph.objects(person, FOAF.name):
        print(name)

# alternative approach for the previous assignment
for name in taskThreeGraph.subject_objects(FOAF.name):
    print(name[1])
