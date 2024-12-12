from flask import Flask, render_template, request, redirect, url_for, flash
from models import *
from sqlalchemy import select
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
#---------------------------------------------------------------------------------------
# @app.route("/index")
# def index():
#     return redirect('index')

#----------------------------------------------------------------------------------------

@app.route('/lista_animal')
def lista_animal():
    sql_animais= select(Animal)
    lista_animais = db_session.execute(sql_animais).scalars().all()
    animais = []
    for pessoa in lista_animais:
        animais.append(pessoa.serialize_user())
    print(lista_animais)
    return render_template('lista_animais.html',
                           lista_de_animais=animais)

@app.route('/novo_animal', methods=['POST', 'GET'])
def novo_animal():
    if request.method == 'POST':

        if not request.form['form_nome_animal'] or not request.form['form_raca1'] or not request.form['form_anoNasci'] or not request.form['idCliente3']:
            flash('Obritório preencher todos os campos')

        else:

            form_Animal = Animal(nome_animal=request.form.get("form_nome_animal"),
                                    raca1 = request.form.get("form_raca1"),
                                    anoNasci= request.form.get("form_anoNasci"),
                                    idCliente3 = request.form.get("form_idCliente3"),
                                    )
            print(form_Animal)
            form_Animal.save()
            db_session.close()
            flash('Animal cadastrado com sucesso')
            return redirect(url_for('lista_animal'))

    return render_template('novo_animal.html')

#-----------------------------------------------------------------------------------------

@app.route('/lista_cliente')
def lista_cliente():
    sql_clientes= select(Animal)
    lista_clientes = db_session.execute(sql_clientes).scalars().all()
    clientes= []
    for pessoa in lista_clientes:
        clientes.append(pessoa.serialize_user())
    print(lista_clientes)
    return render_template('lista_clientes.html',
                           lista_de_clientes=clientes)

@app.route('/novo_cliente', methods=['POST', 'GET'])
def novo_cliente():
    if request.method == 'POST':

        if not request.form['form_CPF'] or not request.form['form_Nome1'] or not request.form['form_telefone'] or not request.form['form_Profissao2'] or not request.form['form_Area2']:
            flash('Obritório preencher todos os campos')

        else:
            form_Cliente = Cliente(CPF=request.form.get("form_CPF"),
                                    Nome1 = request.form.get("form_Nome1"),
                                    telefone= request.form.get("form_telefone"),
                                    Profissao2 = request.form.get("form_Profissao2"),
                                    Area2 = request.form.get("form_Area2"),
                                    )
            print(form_Cliente)
            form_Cliente.save()
            db_session.close()
            flash('Animal cadastrado com sucesso')
            return redirect(url_for('lista_cliente'))

    return render_template('novo_cliente.html')

#------------------------------------------------------------------------------------------

@app.route('/lista_consulta')
def lista_consulta():
    sql_consultas= select(Animal)
    lista_consultas = db_session.execute(sql_consultas).scalars().all()
    consultas = []
    for pessoa in lista_consultas:
        consultas.append(pessoa.serialize_user())
    print(lista_consultas)
    return render_template('lista_animais.html',
                           lista_de_consultas=consultas)

@app.route('/nova_consulta', methods=['POST', 'GET'])
def nova_consulta():
    if request.method == 'POST':

        if (not request.form['form_motivo_id2'] or not request.form['for_hora'] or not request.form['form_minuto']
                or not request.form['form_data1'] or not request.form['form_idAnimal2'] or not request.form['form_idVeterinario']):
            flash('Obritório preencher todos os campos')

        else:
            form_Consulta = Animal(motivo_id2=request.form.get("form_motivo_id2"),
                                    hora = request.form.get("form_hora"),
                                    minuto= request.form.get("form_minuto"),
                                    data1 = request.form.get("form_data1"),
                                    idAnimal2 = request.form.get("form_idAnimal2"),
                                    idVeterinario = request.form.get("form_idVeterinario"),
                                    )
            print(form_Consulta)
            form_Consulta.save()
            db_session.close()
            flash('Consulta cadastrado com sucesso')
            return redirect(url_for('lista_consulta'))

    return render_template('nova_consulta.html')

#------------------------------------------------------------------------------------------

#@app.route('/lista_categoria', methods=['POST', 'GET'])
#def lista_categoria():
#    sql_categorias= select(Categoria)
#    lista_categorias = db_session.execute(sql_categorias).scalars().all()
#    categorias = []
#    for pessoa in lista_categorias:
#        categorias.append(pessoa.serialize_user())
#    print(lista_categorias)
#    return render_template('lista_categoria.html',
#                           lista_de_categorias=categorias)

#@app.route('/nova_categoria', methods=['POST', 'GET'])
#def novo_cadastro():
#    if request.method == 'POST':
#
#        if (not request.form['form_nome_categoria']):
#            flash('Obritório preencher todos os campos')
#
#        else:
#           form_Cadastro = Categoria(nome_categoria=request.form.get("form_nome_animal"),
#                                   )
#            print(form_Cadastro)
#            form_Cadastro.save()
#            db_session.close()
#            flash('Animal cadastrado com sucesso')
#            return redirect(url_for('lista_cadastro'))
#
#   return render_template('novo_cadastro.html')

#---------------------------------------------------------------------------------------------

@app.route('/lista_vaterinario', methods=['POST', 'GET'])
def lista_veterinario():
    sql_veterinarios= select(Veterinario)
    lista_veterinarios = db_session.execute(sql_veterinarios).scalars().all()
    veterinarios = []
    for pessoa in lista_veterinarios:
        veterinarios.append(pessoa.serialize_user())
    print(lista_veterinario)
    return render_template('lista_veterinario.html',
                           lista_de_veterinario=veterinarios)

@app.route('/novo_vaterinario', methods=['POST', 'GET'])
def novo_veterinario():
    if request.method == 'POST':

        if (not request.form['form_salario2'] or not request.form['for_nomeVet'] or not request.form['form_crmv']
                or not request.form['form_v_consulta1']):
            flash('Obritório preencher todos os campos')

        else:
            form_Veterinario = Veterinario(salario2=request.form.get("form_salario2"),
                                    nomeVet = request.form.get("form_nomeVet"),
                                    crmv= request.form.get("form_crmv"),
                                    v_consulta1 = request.form.get("form_v_consulta1"),
                                    )

            print(form_Veterinario)
            form_Veterinario.save()
            db_session.close()
            flash('Animal cadastrado com sucesso')
            return redirect(url_for('lista_veterinario'))

    return render_template('novo_veterinario.html')

#---------------------------------------------------------------------------------------------


if __name__ == '__main__':
    app.run(debug=True)