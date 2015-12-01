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

def init_background():
	background = {}

	default_value = ''
	background = dict.fromkeys([
		'url',
		'color'], default_value)

	return background

def init_date():
	date = {}

	default_value = ''
	date = dict.fromkeys([
		'year',
		'month',
		'day',
		'hour',
		'minute',
		'second',
		'millisecond',
		'format'], default_value)

	return date

def init_event():
	# initializing the event object
	event = {}
	# initializing event sub-objects
	group = ''

	# add sub-objects to event object
	event['start_date'] = init_date()
	event['group'] = group
	event['media'] = init_media()
	event['text'] = init_text()

	return event

def time_converter(time_label):
	hour = ''
	if time_label == 'Morning':
		hour = '9'
	elif time_label == 'Afternoon':
		hour = '14'
	elif time_label == "Evening":
		hour = '19'
	else:
		hour = time_label
	return hour

def create_events(filepath):
	reader = csv.DictReader(open(filepath))

	events = []
	for row in reader:
		event = init_event()
		event['start_date']['year'] = row['start_year']
		event['start_date']['month'] = row['start_month']
		event['start_date']['day'] = row['start_day']
		event['start_date']['hour'] = time_converter(row['start_time'])
		event['text']['headline'] = row['headline']
		event['text']['text'] = row['text']
		event['media']['caption'] = row['media_caption']
		event['media']['credit'] = row['media_credit']
		event['media']['url'] = row['media_url']
		event['media']['thumb'] = row['media_thumb']

		if row['end_month'] != '':
			event['end_date'] = init_date()
			event['end_date']['year'] = row['end_year']
			event['end_date']['month'] = row['end_month']
			event['end_date']['day'] = row['end_day']
			event['end_date']['hour'] = time_converter(row['end_time'])

		events.append(event)

	return events

def create_json(filepath, endpath, headline, text, background_url):
	output = {}

	output['scale'] = 'human'
	output['title'] = {
		'media': init_media(),
		'text': init_text(),
		'background': init_background()
	}
	output['title']['text']['headline'] = headline
	output['title']['text']['text'] = text
	output['title']['background']['url'] = background_url
	output['events'] = create_events(filepath)

	with open(endpath, 'w') as outfile:
		json.dump(output, outfile, indent=4, separators=(',', ': '))