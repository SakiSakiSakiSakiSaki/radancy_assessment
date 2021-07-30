db=client.mydatabase
collection=db['mycollection']
cursor = collection.find({"houses"})
for document in cursor:
    print(document)
