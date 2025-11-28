from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
app = FastAPI()



my_posts=[{"title":"title of content 1","content":"content of content 1","id":1}, {"title":"title of content 2","content":"content of content 2","id":2}]

def find_post(id):
 for p in my_posts:
    if p['id']==id:
       return p
    
def delete_a_post(id):
   for i, posts in enumerate(my_posts):
    if id==posts['id']:
        return i
        
class Post(BaseModel):
    title:str
    content:str
    published:bool=True
    rating:Optional[int]=None

@app.get("/")
async def root():
    return{"message":"Hello Worldsiiiss"}

@app.get("/posts")
def get_posts():
    return{"data":my_posts}

@app.post("/createposts",status_code=status.HTTP_201_CREATED)
def create_posts(new_post:Post):
    post_dict=new_post.dict()
    post_dict['id']=randrange(0,1000000)
    my_posts.append(post_dict)
    return{"data":post_dict}  

@app.get("/posts/latest")
def get_latestpost():
    post=my_posts[int(len(my_posts)-1)] 
    return{"latest_post":post} 

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    index=delete_a_post(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    else: 
     my_posts.pop(index)
     return Response(status_code=status.HTTP_204_NO_CONTENT)
@app.get("/posts/{id}")
def get_onepost(id:int):
 post= find_post(id)
 raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
 return{"post_detail":post}
    
                                                  # if(id>len(my_posts)):
                                                  #     return{"Error":"Post not found"}                  
                                                  # else: 
                                                  #  post=find_post(id)
                                                  #  return{"post_detail":post}
@app.put("/posts/{id}")
def update_post(id:int, post:Post):
   index=delete_a_post(id)
   if index==None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
   else:
      post_dict=post.dict()
      post_dict['id']=id
      my_posts[index]=post_dict
      return{"data":post_dict}
