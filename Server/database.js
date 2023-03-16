var db = connect("127.0.0.1:27017/ubtcs")
db.createCollection("ActiveRecords")
db.createCollection("CompletedRecords")

db.createCollection("Paths")
db.Paths.insert([
	{
		"src":"C1",
		"des":"C2",
		"w":10
	},
	{
		"src":"C2",
		"des":"C1",
		"w":10
	},
	
	{
		"src":"C1",
		"des":"C3",
		"w":20
	},
	{
		"src":"C3",
		"des":"C1",
		"w":20
	},
	{
		"src":"C1",
		"des":"C4",
		"w":30
	},
	{
		"src":"C4",
		"des":"C1",
		"w":30
	},
	
	{
		"src":"C2",
		"des":"C3",
		"w":10
	},
	{
		"src":"C3",
		"des":"C2",
		"w":10
	},
	
	{
		"src":"C2",
		"des":"C4",
		"w":20
	},
	{
		"src":"C4",
		"des":"C2",
		"w":20
	},
	
	{
		"src":"C3",
		"des":"C4",
		"w":10
	},
	{
		"src":"C4",
		"des":"C3",
		"w":10
	},
])

