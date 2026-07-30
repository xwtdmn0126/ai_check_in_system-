from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI 考勤系统成功部署啦！"}
fro
