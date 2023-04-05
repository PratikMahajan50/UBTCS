var db = connect("127.0.0.1:27017/ubtcs")
db.createCollection("VehicleDetails")
db.createCollection("CompleteRecords")
db.createUser({'user':'u1','pwd':'u1','roles':[{role:'readWrite',db:'ubtcs'}]})
db.VehicleDetails.insert([
        {
                "ID":"MH 12 AT 1001",
                "OwnerName":"1001",
                "OwnerID":"1234567890123456",
                "Mapper Vehicle Class": "1"
        }
])
db.VehicleDetails.insert([
        {
                "ID":"MH 12 AT 1002",
                "OwnerName":"1002",
                "OwnerID":"1234567890123456",
                "Mapper Vehicle Class": "2"
        }
])
db.VehicleDetails.insert([
        {
                "ID":"MH 12 AT 1003",
                "OwnerName":"1003",
                "OwnerID":"1234567890123456",
                "Mapper Vehicle Class": "3"
        }
])
db.VehicleDetails.insert([
        {
                "ID":"MH 12 AT 1004",
                "OwnerName":"1004",
                "OwnerID":"1234567890123456",
                "Mapper Vehicle Class": "4"
        }
])
db.VehicleDetails.insert([
        {
                "ID":"MH 12 AT 1005",
                "OwnerName":"1005",
                "OwnerID":"1234567890123456",
                "Mapper Vehicle Class": "5"
        }
])
db.VehicleDetails.insert([
        {
                "ID":"MH 12 AT 1006",
                "OwnerName":"1006",
                "OwnerID":"1234567890123456",
                "Mapper Vehicle Class": "6"
        }
])
db.VehicleDetails.insert([
        {
                "ID":"MH 12 AT 1007",
                "OwnerName":"1007",
                "OwnerID":"1234567890123456",
                "Mapper Vehicle Class": "7"
        }
])
db.VehicleDetails.insert([
        {
                "ID":"MH 12 AT 1008",
                "OwnerName":"1008",
                "OwnerID":"1234567890123456",
                "Mapper Vehicle Class": "8"
        }
])
db.VehicleDetails.insert([
        {
                "ID":"MH 12 AT 1009",
                "OwnerName":"1009",
                "OwnerID":"1234567890123456",
                "Mapper Vehicle Class": "9"
        }
])
db.VehicleDetails.insert([
        {
                "ID":"MH 12 AT 1010",
                "OwnerName":"1010",
                "OwnerID":"1234567890123456",
                "Mapper Vehicle Class": "10"
        }
])


