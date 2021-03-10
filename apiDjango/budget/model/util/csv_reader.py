import json
import csv

csvFilePath = r'resources/IMDb movies.csv'


def parse_films():
    
	data = {}

	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		
		for rows in csvReader:
			
			key = rows['country']
			if key in data:	
    				data[key].append(rows)
			else:
    				data[key] = [rows]
	return data;

		





