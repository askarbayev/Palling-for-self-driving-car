import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
import argparse
from POP import POP

nlp = en_core_web_sm.load()

parser = argparse.ArgumentParser(description='Person command')
parser.add_argument('--command', type=str, help='A required person command argument')
args = parser.parse_args()
command = args.command

doc = nlp(command) 

locations = []
entity_types = ['FAC', 'ORG', 'LOC', 'GPE']
for entity in doc.ents:
	label = entity.label_
	if label in entity_types:
		print(label)
		entity_name = entity.text
		locations.append(entity_name)

print(locations)

location = locations[0]

if location == 'the Huntington Avenue Theatre':
	from home_theatre import operators, init, goal, total_order
	algo = POP(init, goal, operators)
	plan = algo.pop()

	result = [init]

	total_order(plan[1], init, result)

	num = 1
	for x in result:
		print(str(num) + '.', x)
		num += 1
		print('\n')

elif location == 'the Atlantic Fish Co':
	from work_restaurant import operators, init, goal, total_order
	algo = POP(init, goal, operators)
	plan = algo.pop()

	result = [init]

	total_order(plan[1], init, result)

	num = 1
	for x in result:
		print(str(num) + '.', x)
		num += 1
		print('\n')

#python3 destination_extract.py --command 'Hey Lauren, drive me to the Atlantic Fish Co at 9pm.'

