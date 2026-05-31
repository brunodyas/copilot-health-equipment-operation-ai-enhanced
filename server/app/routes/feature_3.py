from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/3', tags=['feature'])

@router.get('/status')
def feature_3_status():
    return {'ok': True, 'feature': 'Refatorar o código para melhorar a legibilidade e manutenção', 'task': '3'}
