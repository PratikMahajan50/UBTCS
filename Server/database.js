var db = connect("127.0.0.1:27017/ubtcs")
db.createCollection("ActiveRecords")
db.createCollection("CompletedRecords")

