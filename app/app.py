from flask import Flask
from redis import Redis

import pymongo
from pymongo import MongoClient

app 	= Flask(__name__)
redis 	= Redis(host='redis-srv', port=6379)
client = MongoClient('mongodb://mongo-srv:27017/')

first_insert = {"count": 0}
db_docker = client.docker_database
post_id = db_docker.post.insert_one(first_insert).inserted_id

@app.route('/')
def hello():
    redis.incr('hits')

    return 'Pagina acessada: %s vezes' % redis.get('hits')

@app.route('/mongo')
def mongo():
	db_docker.post.update_one({"_id": post_id}, {"$inc":{"count":+1}})
	result = db_docker.post.find_one({"_id": post_id})

	return 'Pagina acessada: %s vezes ' % str(result['count'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)