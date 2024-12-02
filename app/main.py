from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from . import models, schemas, auth, database
from app.dependencies import get_db, get_current_user, get_current_admin
from fastapi_health import health

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(data={"sub": user.username, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/user", response_model=schemas.User)
def read_users_me(current_user: schemas.User = Depends(get_current_user)):
    return current_user

@app.get("/admin", response_model=schemas.User)
def read_admins_me(current_user: schemas.User = Depends(get_current_admin)):
    return current_user

def healthy_condition():
    return {
            "readiness": "OK",
            "liveness": "OK"
        }

def sick_condition():
    return False

app.add_api_route("/health", health([healthy_condition, sick_condition]))
