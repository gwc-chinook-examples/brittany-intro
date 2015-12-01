import csv
import json

# HELPER FUNCTIONS
def init_media():
	media = {}

	default_value = ''
	media = dict.fromkeys([
		'caption',
		'credit',
		'url',
		'thumb'], default_value)

	return media

def init_text():
	text = {}

	default_value = ''
	text = dict.fromkeys([
		'headline',
		'text'], default_value)

	return text

def init_event():
	# initializing the event object
	event = {}
	# initializing event sub-objects
	start_date = {}
	end_date = {}
	group = ''

	default_value = ''
	start_date = dict.fromkeys([
		'year',
		'month',
		'day',
		'hour',
		'minute',
		'second'
		'millisecond',
		'format'], default_value)
	end_date = dict.fromkeys([
		'year',
		'month',
		'day',
		'hour',
		'minute',
		'second'
		'millisecond',
		'format'], default_value)

	# set year
	start_date['year'] = '2015'
	end_date['year'] = '2015'

	# add sub-objects to event object
	event['start_date'] = start_date
	event['end_date'] = end_date
	event['group'] = group
	event['media'] = init_media()
	event['text'] = init_text()

	return event

def time_converter(time_label):
	hour = ''
	if time_label == 'Morning':
		hour = '9'
	elif time_label == 'Afternoon':
		hour = '2'
	return hour

def create_events(filepath):
	reader = csv.DictReader(open(filepath))

	events = []
	for row in reader:
		event = init_event()
		event['start_date']['month'] = row['start_month']
		event['start_date']['day'] = row['start_day']
		event['start_date']['hour'] = time_converter(row['start_time'])
		event['end_date']['month'] = row['end_month']
		event['end_date']['day'] = row['end_day']
		event['end_date']['hour'] = time_converter(row['end_time'])
		event['text']['headline'] = row['headline']
		event['text']['text'] = row['text']

		events.append(event)

	return events

# create JSON
output = {}

output['scale'] = 'human'
output['title'] = {
	'media': init_media(),
	'text': init_text()
}
output['events'] = create_events('static/data/test.csv')

with open('static/data/test.json', 'w') as outfile:
	json.dump(output, outfile, indent=4, separators=(',', ': '))
