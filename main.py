from barebone_fastapi_template import app
import uvicorn


if __name__ == '__main__':
    uvicorn.run(app=app)