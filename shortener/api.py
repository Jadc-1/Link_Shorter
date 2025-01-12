from ninja import Router
from .schemas import LinkSchema
from .models import Links
from django.shortcuts import get_object_or_404
##Tipo de requisição - CONVENÇÃO
## GET - Listar todos links cadastrados
## POST - Criar novo link
## PUT - Atualizar informações que ja existem
## DELETE - Excluir algo, como um link

shortener_router = Router()

@shortener_router.post('create/', response={200: LinkSchema, 409: dict})
def create(request, link_schema: LinkSchema):
    data = link_schema.to_model_data()
    token = data['token']
    redirect_link = data['redirect_link']
    expiration_time = data['expiration_time']
    max_uniques_cliques = data['max_uniques_cliques']

    if token and Links.objects.filter(token=token).exists():
        return 409, {'error': 'Token já existe, use outro'}
    

    link = Links(redirect_link = redirect_link, expiration_time = expiration_time, max_uniques_cliques = max_uniques_cliques, token = token)
    link.save()

    return 200, LinkSchema.from_model(link)

@shortener_router.get('/{token}')
def redirect_link(request, token):
    link = get_object_or_404(Links, token=token, active= True)