from fastapi import FastAPI, Header, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import jwt
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET_KEY = 'tt_group_super_secret_key'

def get_current_user(authorization: str = Header(None)):
    if not authorization: raise HTTPException(status_code=401)
    try:
        token = authorization.split(" ")[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid Token")

@app.post("/check")
async def handle_check(action: dict, user: dict = Depends(get_current_user)):
    # In a real app, save to SQL here
    return {
        "user": user['sub'],
        "time": datetime.now().strftime("%H:%M:%S"),
        "action": action.get("type"),
        "msg": f"T&T Group: {action.get('type')} successful"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=5002)