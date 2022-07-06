from mini_media.model import users, posts


# authencate



session={}
def authentiate(**kwargs):
    username = kwargs.get("username")
    email = kwargs.get("email")
    user_data = [user for user in users if user["username"] == username and user["email"] == email]
    print(user_data)
    return user_data


def LoginRequierd(fn):
    def wrapper(*args, **kwargs):
        if "user" in session:
            return fn(*args, **kwargs)
        else:
            print("You must Login")

    return wrapper
@LoginRequierd
def logged_user():
    username = session.get("user")
    userid = [user["id"] for user in users if user["username"] == username][0]
    return userid


class signInView:

    def post(self,*args, **kwargs):
        username=kwargs.get("username")
        email=kwargs.get("email")
        user=authentiate(username=username,email=email)
        if user:
            print("Login success")
            session["user"]=username
        else:
            print("Invalid credentials")
@LoginRequierd
def logout(*args,**kwargs):
    session.pop("user")


class PostListView:
    @LoginRequierd
    def get(self,*args,**kwargs):
        return posts




#print(session)

pl=PostListView()
try:
    all_post = pl.get()


except Exception as e:

    print(e)



class Mypostview:
    @LoginRequierd
    def get(self ,*args,**kwargs):
        username=session.get("user")
        userid=[user["id"] for user in users if user["username"]==username][0]
        q=[post for post in posts if post["userId"]==userid]
        return q
        print(userid)


sign = signInView()
sign.post(username="Bret", email="Sincere@april.biz")

pos=Mypostview()
print(pos.get())


class postcreate_View():
    @LoginRequierd
    def posts(self,*args,**kwargs):
        userid=logged_user()
        title=kwargs.get("title")
        body=kwargs.get("body")
        data={
            "userId":userid,
            "title":title,
             "body":body
        }
        posts.append(data)
        print(" ```__Post created sucessfully__```")
class postdetailsView():
    @LoginRequierd
    def get(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        q=[p for p in posts if p.get("id")==post_id]
        return q
    def put(self,id=None,*args,**kwargs):

        post=[p for p in posts if p.get("id")==id][0]
        title=kwargs.get("title")
        body=kwargs.get("body")
        post["title"]=title
        post["body"]=body
        print(post)





pst=postcreate_View()
pst.posts(title="mypost",body="this is my new post")
mp=Mypostview()
print(mp.get())

details=postdetailsView()
print(details.get(post_id=5))
details.put(id=10,title="My new post",body="This is my post")