from fastapi import APIRouter


router = APIRouter()


@router.post(path='/add')
def add(
    a: float,
    b: float,
) -> float:
    return a + b


@router.post(path='/minus')
def minus(
    a: float,
    b: float,
) -> float:
    return a - b
