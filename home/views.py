from django.shortcuts import render
from .models import cliente
import datetime
from django.http import HttpResponse
#from .utils import render_to_pdf
from django.views.generic import View
from django.template.loader import get_template

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
            insc = request.POST.get('insc')
            venc_hab = request.POST.get('venc_hab')
            rg = request.POST.get('rg')
            rg_data = request.POST.get('rg_data')
            rg_uf = request.POST.get('rg_uf')
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
            tel1 = request.POST.get('tel1')
            cel1 = request.POST.get('cel1')
            mail1 = request.POST.get('mail1')
            tel2 = request.POST.get('tel2')
            cel2 = request.POST.get('cel2')
            mail2 = request.POST.get('mail2')
            if request.POST.get('data_nasc') != '' and request.POST.get('venc_hab') != '':
                novo_cliente = cliente(nome=nome, data_nasc=data_nasc, venc_habilitacao=venc_hab, inscricao=insc, rg=rg, rg_data=rg_data, rg_uf=rg_uf, cpf=cpf, endereco=end, numero=num, bairro=bairro, cep=cep, cidade=cidade, estado=estado, telefone=tel, celular=cel, email=mail, telefone1=tel1, celular1=cel1, email1=mail1, telefone2=tel2, celular2=cel2, email2=mail2)
                novo_cliente.save()
            elif request.POST.get('data_nasc') == '' and request.POST.get('venc_hab') != '':
                novo_cliente = cliente(nome=nome, venc_habilitacao=venc_hab, inscricao=insc, rg=rg, rg_data=rg_data, rg_uf=rg_uf, cpf=cpf, endereco=end, numero=num, bairro=bairro, cep=cep, cidade=cidade, estado=estado, telefone=tel, celular=cel, email=mail, telefone1=tel1, celular1=cel1, email1=mail1, telefone2=tel2, celular2=cel2, email2=mail2)
                novo_cliente.save()
            elif request.POST.get('data_nasc') != '' and request.POST.get('venc_hab') == '':
                novo_cliente = cliente(nome=nome, data_nasc=data_nasc, inscricao=insc, rg=rg, cpf=cpf, rg_data=rg_data, rg_uf=rg_uf, endereco=end, numero=num, bairro=bairro, cep=cep, cidade=cidade, estado=estado, telefone=tel, celular=cel, email=mail, telefone1=tel1, celular1=cel1, email1=mail1, telefone2=tel2, celular2=cel2, email2=mail2)
                novo_cliente.save()
            elif request.POST.get('data_nasc') == '' and request.POST.get('venc_hab') == '':
                novo_cliente = cliente(nome=nome, rg=rg, rg_data=rg_data, inscricao=insc, rg_uf=rg_uf, cpf=cpf, endereco=end, numero=num, bairro=bairro, cep=cep, cidade=cidade, estado=estado, telefone=tel, celular=cel, email=mail, telefone1=tel1, celular1=cel1, email1=mail1, telefone2=tel2, celular2=cel2, email2=mail2)
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
            insc = request.POST.get('insc')
            venc_hab = request.POST.get('venc_hab')
            rg = request.POST.get('rg')
            rg_data = request.POST.get('rg_data')
            rg_uf = request.POST.get('rg_uf')
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
            tel1 = request.POST.get('tel1')
            cel1 = request.POST.get('cel1')
            mail1 = request.POST.get('mail1')
            tel2 = request.POST.get('tel2')
            cel2 = request.POST.get('cel2')
            mail2 = request.POST.get('mail2')
            
            if request.POST.get('data_nasc') != '' and request.POST.get('venc_hab') != '':
                cli_obj.nome = nome
                cli_obj.data_nasc = data_nasc
                cli_obj.inscricao = insc
                cli_obj.venc_habilitacao = venc_hab
                cli_obj.rg = rg
                cli_obj.rg_data = rg_data
                cli_obj.rg_uf = rg_uf
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
                cli_obj.telefone1 = tel1
                cli_obj.celular1 = cel1
                cli_obj.email1 = mail1
                cli_obj.telefone2 = tel2
                cli_obj.celular2 = cel2
                cli_obj.email2 = mail2
                cli_obj.save();
                return render(request, 'home/editar_cliente.html', {'title':'Editar Cliente', 'cli_obj':cli_obj})
            elif request.POST.get('data_nasc') == '' and request.POST.get('venc_hab') != '':
                cli_obj.nome = nome
                cli_obj.inscricao = insc
                cli_obj.venc_habilitacao = venc_hab
                cli_obj.data_nasc = cli_obj.data_nasc
                cli_obj.rg = rg
                cli_obj.rg_data = rg_data
                cli_obj.rg_uf = rg_uf
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
                cli_obj.telefone1 = tel1
                cli_obj.celular1 = cel1
                cli_obj.email1 = mail1
                cli_obj.telefone2 = tel2
                cli_obj.celular2 = cel2
                cli_obj.email2 = mail2
                cli_obj.save();
                return render(request, 'home/editar_cliente.html', {'title':'Editar Cliente', 'cli_obj':cli_obj})
            elif request.POST.get('data_nasc') != '' and request.POST.get('venc_hab') == '':
                cli_obj.nome = nome
                cli_obj.data_nasc = data_nasc
                cli_obj.inscricao = insc
                cli_obj.venc_habilitacao = cli_obj.venc_habilitacao
                cli_obj.rg = rg
                cli_obj.rg_data = rg_data
                cli_obj.rg_uf = rg_uf
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
                cli_obj.telefone1 = tel1
                cli_obj.celular1 = cel1
                cli_obj.email1 = mail1
                cli_obj.telefone2 = tel2
                cli_obj.celular2 = cel2
                cli_obj.email2 = mail2
                cli_obj.save();
                return render(request, 'home/editar_cliente.html', {'title':'Editar Cliente', 'cli_obj':cli_obj})
            elif request.POST.get('data_nasc') == '' and request.POST.get('venc_hab') == '':
                cli_obj.nome = nome
                cli_obj.inscricao = insc
                cli_obj.venc_habilitacao = cli_obj.venc_habilitacao
                cli_obj.data_nasc = cli_obj.data_nasc
                cli_obj.rg = rg
                cli_obj.rg_data = rg_data
                cli_obj.rg_uf = rg_uf
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
                cli_obj.telefone1 = tel1
                cli_obj.celular1 = cel1
                cli_obj.email1 = mail1
                cli_obj.telefone2 = tel2
                cli_obj.celular2 = cel2
                cli_obj.email2 = mail2
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

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf.html')
        cliente_id = request.GET.get('cliente_id')
        cli_obj = cliente.objects.filter(id=cliente_id).get()
        hoje = datetime.datetime.now().strftime('%d/%m/%Y')

        context = {
                "cli_nome": cli_obj.nome,
                "cli_nasc": cli_obj.data_nasc.strftime('%d/%m/%Y'),
                "cli_hab": cli_obj.venc_habilitacao.strftime('%d/%m/%Y'),
                "cli_rg": cli_obj.rg,
                "cli_cpf": cli_obj.cpf,
                "cli_end": cli_obj.endereco,
                "cli_num": cli_obj.numero,
                "cli_bairro": cli_obj.bairro,
                "cli_cep": cli_obj.cep,
                "cli_cidade": cli_obj.cidade,
                "cli_estado": cli_obj.estado,
                "cli_tel": cli_obj.telefone,
                "cli_cel": cli_obj.celular,
                "cli_mail": cli_obj.email,
                "hoje": hoje,
            }
        html = template.render(context)
        pdf = render_to_pdf('pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "%s.pdf" %(cli_obj.nome)
            content = "inline-block; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
        return HttpResponse(pdf, content_type='application/pdf')

def excluir(request):
    if request.user.is_authenticated():
        clientes = cliente.objects.all().order_by('nome')
        if request.method == 'POST' and request.POST.get('cliente_id') != None:
            cli_id = request.POST.get('cliente_id')
            cli_obj = cliente.objects.filter(id=cli_id).get()
            cli_obj.delete()
            return render(request, 'home/home.html', {'title':'Home', 'clientes':clientes})
        return render(request, 'home/home.html', {'title':'Home', 'clientes':clientes})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})
