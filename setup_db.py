# from cassandra.cluster import Cluster
#
# cluster = Cluster(['172.19.0.3'],port=9042)
# session = cluster.connect()
#
# query = "create keyspace Currency with replication = {'class' : 'SimpleStrategy', 'replication_factor':2}"
# session.execute(query)
#
# session.execute('USE Currency')
#
# query = "CREATE TABLE cities (id int, name text, country text, PRIMARY KEY(id);"
# session.execute(query)
#
# query = "INSERT INTO cities(id,name,country) VALUES (1,'Warsaw','Poland');"
# session.execute(query)
