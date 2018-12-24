from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
db=client.pymongo_sim
collection=db.pymongo_coll
db.pymongo_coll.insert_many([
	{"age_category": "child", "lower_bound": 0, "upper_bound":12},
	{"age_category": "teen", "lower_bound": 13, "upper_bound":17},
	{"age_category": "young_adult", "lower_bound": 18, "upper_bound":25},
	{"age_category": "adult", "lower_bound": 26, "upper_bound":49},
	{"age_category": "elderly", "lower_bound": 50, "upper_bound":110}
	])
collection=db.pymongo_ageRecords
db.pymongo_ageRecords.insert_many([
	{"age":2, "age_category":"child"}
	])