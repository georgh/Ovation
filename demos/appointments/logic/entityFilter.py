from enum import Enum

class Entity_Type(Enum):
	DAY = 1
	TIMESPAN = 2

days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday","tomorrow","yesterday"]
timespans = ["morning","afternoon","evening","night"]

class EntityFilter:

	def valid_entity(entity_type,entity_value):
		valid = False
		testList = []
		if entity_type == Entity_Type.DAY:
			testList = days
		if entity_type == Entity_Type.TIMESPAN:
			testList = timespans
		for word in testList:
			if entity_value == word:
				valid = True
		return valid

	def filterList(entity_list):
		filteredList = []
		for entity in entity_list:
			if entity.entity.lower() == "day" and EntityFilter.valid_entity(Entity_Type.DAY,entity.value.lower()):

				filteredList.append(entity)
			if entity.entity.lower() == "timespans" and EntityFilter.valid_entity(Entity_Type.TIMESPAN,entity.value.lower()):
				filteredList.append(entity)
		return filteredList
