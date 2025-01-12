from ninja import Router

##Tipo de requisição - CONVENÇÃO
## GET - Listar todos links cadastrados
## POST - Criar novo link
## PUT - Atualizar informações que ja existem
## DELETE - Excluir algo, como um link

shortener_router = Router()

@shortener_router.get('create/')
def create(request):
    return {'status': 1}
