from fastapi import FastAPI
from barebone_fastapi_template.endpoints.calculation import router as router_calculation


app = FastAPI(
    title="Barebone FastAPI Template",
)
app.include_router(router=router_calculation)
