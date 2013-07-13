import sqlite3 #where is this being imported from?

DB = None #Earlier there was an error on line 5 because global DB is declared later. Here, we set it equal to None, so it knows that it is declared later
CONN = None

def get_all_posts():
    query = "SELECT posts.id, posts.title, posts.body, posts.user_id, posts.created_at, users.email FROM posts JOIN users ON posts.user_id=users.id ORDER BY created_at" #sorts posts by time created 
    query_result = DB.execute(query) # here, result is a pointer to the query
    rows = query_result.fetchall() # so then, you need to fetch the data, which returns as a list of tuples
    p_list = []
    for row in rows:
        id = row[0]
        title = row[1]
        body= row[2]
        user_id = row[3]
        created_at=row[4]
        email = row[5]

        p = Post(id, title, body, user_id, created_at, email)
        p_list.append(p)
    return p_list

class Post(object):
    def __init__(self, id, title, body, user_id, created_at, email):
        self.id = id #one attribute of this object is id, and that is equal to the argument id
        self.title = title
        self.body = body
        self.user_id = user_id
        self.created_at = created_at
        self.email = email

# # Post functions

# class Post(object):
#     def __init__(self, title, body, user_id, created_at):
#         self.title = title
#         self.body = body
#         self.user_id = user_id
#         self.created_at = created_at

#     def get_all_posts(self):
#         query = "SELECT * FROM posts"
#         DB.execute(query)
#         post_list = DB.fetchall()
#         return post_list

# def add_post(title, body, user_id, created_at):
#     query = "INSERT INTO posts (title, body, user_id, created_at) VALUES (?, ?, ?, ?)"
#     DB.execute(query, (title, body, user_id, created_at))
#     return True

# def get_post(post_id):
#     query = "SELECT * FROM posts WHERE post_id=?"
#     post = DB.execute(query, (post_id))
#     p = Post(post[1], post[2], post[3], post[4])
#     return p



# # User functions

# class User(object):
#     def __init__(self, email, password):
#         self.email = email
#         self.password = password

# def add_user(email, password):
#     query = "INSERT INTO users (email, password) VALUES (?, ?)"
#     DB.execute(query, (email, password))
#     return True


# # Vote functions

# class Vote(object):
#     def __init__(self, user_id, post_id, value):
#         self.user_id = user_id
#         self.post_id = post_id
#         self.value = value

# def add_vote(user_id, post_id, value):
#     query = "INSERT INTO votes VALUES (user_id, post_id, value)"
#     DB.execute(query, (github, project_title, grade))
#     CONN.commit()
#     return True

# # Database functions

## function that asks sqlite3 to connect to app.db
def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("app.db")
    DB = CONN.cursor()