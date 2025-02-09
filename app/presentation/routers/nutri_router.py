from fastapi import APIRouter, Depends
from app.presentation.controllers.nutri_controller import NutricionistaController
from app.domain.models.nutricionista import Nutricionista

router = APIRouter(prefix="/nutricionistas", tags=["Nutricionistas"])

nutri_controller = NutricionistaController()

@router.post("/registrar")
async def registrar_nutricionista(nutricionista: Nutricionista, nutri_controller: NutricionistaController = Depends()):
    return await nutri_controller.registrar_nutricionista(nutricionista)

@router.get("/get")
async def get_nutricionistas(nutri_controller: NutricionistaController = Depends()):
    return await nutri_controller.get_nutricionistas()

@router.get("/get/{id_nutricionista}")
async def get_nutricionista(id_nutricionista: int, nutri_controller: NutricionistaController = Depends()):
    return await nutri_controller.get_nutricionista(id_nutricionista)

@router.delete("/delete/{id_nutricionista}")
async def delete_nutricionista(id_nutricionista: int, nutri_controller: NutricionistaController = Depends()):
    return await nutri_controller.delete_nutricionista(id_nutricionista)

@router.put("/update/{id_nutricionista}")
async def update_nutricionista(nutricionista: Nutricionista, id_nutricionista: int, nutri_controller: NutricionistaController = Depends()):
    return await nutri_controller.update_nutricionista(nutricionista, id_nutricionista)
