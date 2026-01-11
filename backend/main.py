import model
# from model import user
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
from database import engine, Sessionlocal
from sqlalchemy.orm import Session
from database import Base
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# create tables
Base.metadata.create_all(bind=engine)
# pydantic schemas
class PostBase(BaseModel):
    title: str
    content: str
    user_id: int

class PostUpdate(BaseModel):
    title: str
    content: str

class PostResponse(PostBase):
    id: int
    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# dependency

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

# db_dependency = Annotated(Session, Depends(get_db))
@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    ...

@app.post("/posts/", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
async def create_post(post: PostBase, db: Session = Depends(get_db)):
    db_post = model.Post(**post.model_dump())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@app.get("/posts/{post_id}", status_code=status.HTTP_200_OK, response_model=PostResponse)
async def read_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(model.Post).filter(model.Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail='Post not found')
    return post


@app.get("/posts/", status_code=status.HTTP_200_OK, response_model=list[PostResponse])
async def read_posts(db: Session = Depends(get_db)):
    posts = db.query(model.Post).all()
    return posts

@app.put("/posts/{post_id}", status_code=status.HTTP_200_OK, response_model=PostResponse)
async def update_post(post_id: int, post: PostUpdate, db: Session = Depends(get_db)):
    db_post = db.query(model.Post).filter(model.Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail='Post not found')
    db_post.title = post.title
    db_post.content = post.content
    db.commit()
    db.refresh(db_post)
    return db_post

@app.delete("/posts/{post_id}", status_code=status.HTTP_200_OK)
async def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(model.Post).filter(model.Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail='Post was not found')
    db.delete(db_post)
    db.commit()

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = model.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail='user not found')
    return user
