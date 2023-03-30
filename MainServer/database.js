var db = connect("127.0.0.1:27017/ubtcs")
db.createCollection("VehicleDetails")
db.createCollection("Records")
db.VehicleDetails.insert([
	{
		"ID":"MH 12 AT 6666",
		"OwnerName":"XYZ",
		"OwnerID":"1234567890123456",
		"Mapper Vehicle Class": "5"
	}
])