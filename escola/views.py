from django.http import JsonResponse #pacote para redenrizar JSON

# Create your views here.
def alunos(request):
    if request.method == 'GET': #verificando se a requisição é do metodo GET    
        aluno ={'id': 1, 'nome': 'Lucas'}
        return JsonResponse(aluno)