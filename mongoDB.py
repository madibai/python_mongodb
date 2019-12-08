from pymongo import MongoClient


def start():
    #  client = MongoClient()
    #  client = MongoClient('localhost', 27017)
    client = MongoClient('mongodb://localhost:27017')
    db = client['test']
    #  result = insertPost(db)
    #  print('One post: {0}'.format(result))

    bills_post = db.posts.find_one({'author': 'Scott'})
    print(bills_post)

    all_posts = db.posts.find()
    for post in all_posts:
        print(post)


def insertPost(db):
    posts = db.posts
    result = posts.insert_one(getPostData())
    #  print('One post: {0}'.format(result.inserted_id))
    return result.inserted_id


def getPostData():
    post_data = {
        'title': 'Python and MongoDB',
        'content': 'PyMongo is fun, you guys',
        'author': 'Frank'
    }
    return post_data


if __name__ == "__main__":
    start()
