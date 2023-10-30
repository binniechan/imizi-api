from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.requests import Request

from app import models, schemas
from app.db.connection import db
from app.depends.validate_api_key import validate_api_key

image = APIRouter()


@image.post("/upload")
def upload_image(session: Session = Depends(db.session), valid_key: bool = Depends(validate_api_key)):
    if valid_key:
        return {"message": "success"}
    return {"message": "failed"}

# @image.post("/upload")
# def upload_image(request: Request,session: Session = Depends(db.session), valid_key: bool = Depends(validate_api_key)):
#     if valid_key:
#         return {"message": "success"}
#     return {"message": "failed"}
@image.get("/{image_id}")
def get_image(request: Request, image_id: int, session: Session = Depends(db.session)):
    if request.state.user:
        return {"message": "success"}
    return {"message": "failed"}

# middleware를 무조건 거치게 되는데 token이 없으면 request 객체가 생성이 안된다
# 그래서 request 객체를 쓰든 안쓰든 api실행시 permission error뜸