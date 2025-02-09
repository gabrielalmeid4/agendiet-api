from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.presentation.routers.user_router import router as user_router
from app.presentation.routers.plano_router import router as plano_router
from app.presentation.routers.peso_router import router as peso_router
from app.presentation.routers.nutri_router import router as nutri_router
from app.presentation.routers.meta_peso_router import router as meta_peso_router
from app.presentation.routers.med_router import router as med_router

app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

app.include_router(user_router)
app.include_router(plano_router)
app.include_router(peso_router)
app.include_router(nutri_router)
app.include_router(meta_peso_router)
app.include_router(med_router)