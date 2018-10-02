from django.shortcuts import render
from .models import cliente
import datetime

# Create your views here.
def home(request):
    if request.user.is_authenticated():
        clientes = cliente.objects.all().order_by('nome')
        if request.method == 'POST' and request.POST.get('cliente_id') != None:
            cli_id = request.POST.get('cliente_id')
            cli_obj = cliente.objects.filter(id=cli_id).get()
            return render(request, 'home/editar_cliente.html', {'title':'Editar Cliente', 'cli_obj':cli_obj})
        return render(request, 'home/home.html', {'title':'Home', 'clientes':clientes})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def novo(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('name') != None:
            nome = request.POST.get('name')
            data_nasc = request.POST.get('data_nasc')
            venc_hab = request.POST.get('venc_hab')
            rg = request.POST.get('rg')
            cpf = request.POST.get('cpf')
            end = request.POST.get('end')
            num = request.POST.get('num')
            bairro = request.POST.get('bairro')
            cep = request.POST.get('cep')
            cidade = request.POST.get('cidade')
            estado = request.POST.get('estado')
            tel = request.POST.get('tel')
            cel = request.POST.get('cel')
            mail = request.POST.get('mail')
            if request.POST.get('data_nasc') != '' and request.POST.get('venc_hab') != '':
                novo_cliente = cliente(nome=nome, data_nasc=data_nasc, venc_habilitacao=venc_hab, rg=rg, cpf=cpf, endereco=end, numero=num, bairro=bairro, cep=cep, cidade=cidade, estado=estado, telefone=tel, celular=cel, email=mail)
                novo_cliente.save()
            elif request.POST.get('data_nasc') == '' and request.POST.get('venc_hab') != '':
                novo_cliente = cliente(nome=nome, venc_habilitacao=venc_hab, rg=rg, cpf=cpf, endereco=end, numero=num, bairro=bairro, cep=cep, cidade=cidade, estado=estado, telefone=tel, celular=cel, email=mail)
                novo_cliente.save()
            elif request.POST.get('data_nasc') != '' and request.POST.get('venc_hab') == '':
                novo_cliente = cliente(nome=nome, data_nasc=data_nasc, rg=rg, cpf=cpf, endereco=end, numero=num, bairro=bairro, cep=cep, cidade=cidade, estado=estado, telefone=tel, celular=cel, email=mail)
                novo_cliente.save()
            elif request.POST.get('data_nasc') == '' and request.POST.get('venc_hab') == '':
                novo_cliente = cliente(nome=nome, rg=rg, cpf=cpf, endereco=end, numero=num, bairro=bairro, cep=cep, cidade=cidade, estado=estado, telefone=tel, celular=cel, email=mail)
                novo_cliente.save()
            return render(request, 'home/novo_cliente.html', {'title':'Novo Cliente'})
        return render(request, 'home/novo_cliente.html', {'title':'Novo Cliente'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def hab_vencidas(request):
    if request.user.is_authenticated():
        now = datetime.datetime.now()
        contador = 0
        for c in cliente.objects.filter(venc_habilitacao__lt=now).all():
            contador = contador + 1
        clientes = cliente.objects.all().order_by('venc_habilitacao')
        return render(request, 'home/hab_vencida.html', {'title':'Habilitações Vencidas', 'contador':contador, 'clientes':clientes})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def editar_cliente(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('cliente_id') != None:
            cli_id = request.POST.get('cliente_id')
            cli_obj = cliente.objects.filter(id=cli_id).get()
            return render(request, 'home/editar_cliente1.html', {'title':'Editar Cliente', 'cli_obj':cli_obj})
        return render(request, 'home/editar_cliente1.html', {'title':'Editar Cliente'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def salvar(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('cliente_id') != None:
            cli_id = request.POST.get('cliente_id')
            cli_obj = cliente.objects.filter(id=cli_id).get()
            nome = request.POST.get('name')
            data_nasc = request.POST.get('data_nasc')
            venc_hab = request.POST.get('venc_hab')
            rg = request.POST.get('rg')
            cpf = request.POST.get('cpf')
            end = request.POST.get('end')
            num = request.POST.get('num')
            bairro = request.POST.get('bairro')
            cep = request.POST.get('cep')
            cidade = request.POST.get('cidade')
            estado = request.POST.get('estado')
            tel = request.POST.get('tel')
            cel = request.POST.get('cel')
            mail = request.POST.get('mail')
            
            if request.POST.get('data_nasc') != '' and request.POST.get('venc_hab') != '':
                cli_obj.nome = nome
                cli_obj.data_nasc = data_nasc
                cli_obj.venc_habilitacao = venc_hab
                cli_obj.rg = rg
                cli_obj.cpf = cpf
                cli_obj.endereco = end
                cli_obj.numero = num
                cli_obj.bairro = bairro
                cli_obj.cep = cep
                cli_obj.cidade = cidade
                cli_obj.noestadome = estado
                cli_obj.telefone = tel
                cli_obj.celular = cel
                cli_obj.email = mail
                cli_obj.save();
                return render(request, 'home/editar_cliente.html', {'title':'Editar Cliente', 'cli_obj':cli_obj})
            elif request.POST.get('data_nasc') == '' and request.POST.get('venc_hab') != '':
                cli_obj.nome = nome
                cli_obj.venc_habilitacao = venc_hab
                cli_obj.data_nasc = cli_obj.data_nasc
                cli_obj.rg = rg
                cli_obj.cpf = cpf
                cli_obj.endereco = end
                cli_obj.numero = num
                cli_obj.bairro = bairro
                cli_obj.cep = cep
                cli_obj.cidade = cidade
                cli_obj.noestadome = estado
                cli_obj.telefone = tel
                cli_obj.celular = cel
                cli_obj.email = mail
                cli_obj.save();
                return render(request, 'home/editar_cliente.html', {'title':'Editar Cliente', 'cli_obj':cli_obj})
            elif request.POST.get('data_nasc') != '' and request.POST.get('venc_hab') == '':
                cli_obj.nome = nome
                cli_obj.data_nasc = data_nasc
                cli_obj.venc_habilitacao = cli_obj.venc_habilitacao
                cli_obj.rg = rg
                cli_obj.cpf = cpf
                cli_obj.endereco = end
                cli_obj.numero = num
                cli_obj.bairro = bairro
                cli_obj.cep = cep
                cli_obj.cidade = cidade
                cli_obj.noestadome = estado
                cli_obj.telefone = tel
                cli_obj.celular = cel
                cli_obj.email = mail
                cli_obj.save();
                return render(request, 'home/editar_cliente.html', {'title':'Editar Cliente', 'cli_obj':cli_obj})
            elif request.POST.get('data_nasc') == '' and request.POST.get('venc_hab') == '':
                cli_obj.nome = nome
                cli_obj.venc_habilitacao = cli_obj.venc_habilitacao
                cli_obj.data_nasc = cli_obj.data_nasc
                cli_obj.rg = rg
                cli_obj.cpf = cpf
                cli_obj.endereco = end
                cli_obj.numero = num
                cli_obj.bairro = bairro
                cli_obj.cep = cep
                cli_obj.cidade = cidade
                cli_obj.noestadome = estado
                cli_obj.telefone = tel
                cli_obj.celular = cel
                cli_obj.email = mail
                cli_obj.save();
                return render(request, 'home/editar_cliente.html', {'title':'Editar Cliente', 'cli_obj':cli_obj})
            return render(request, 'home/editar_cliente.html', {'title':'Editar Cliente', 'cli_obj':cli_obj})
        return render(request, 'home/editar_cliente1.html', {'title':'Editar Cliente'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def visualizar(request):
    if request.user.is_authenticated():
        clientes = cliente.objects.all().order_by('nome')
        if request.method == 'POST' and request.POST.get('cliente_id') != None:
            cli_id = request.POST.get('cliente_id')
            cli_obj = cliente.objects.filter(id=cli_id).get()
            return render(request, 'home/editar_cliente.html', {'title':'Editar Cliente', 'cli_obj':cli_obj})
        return render(request, 'home/home.html', {'title':'Home', 'clientes':clientes})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})