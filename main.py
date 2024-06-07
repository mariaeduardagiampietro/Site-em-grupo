from flask import Flask, render_template, request, redirect
app = Flask(__name__)

pacientess = []
agendamento = []

@app.route('/')
def index():
    return render_template('index.html', pacientes=pacientess, agendamento=agendamento)

@app.route('/pacientes')
def pacientes():
    return render_template('pacientes.html')

@app.route('/verificar_pacientes', methods=['GET', 'POST'])
def verificar_pacientes():
    if request.method == 'POST':
        nome = request.form['nome']
        especie = request.form['especie']
        raca = request.form['raca']
        peso = request.form['peso']
        nome_tutor = request.form['nome_tutor']
        telefone = request.form['telefone']
        codigo = len(pacientess)
        pacientess.append([codigo, nome, especie, raca, peso, nome_tutor, telefone])
        return render_template('lista_pacientes.html', pacientes=pacientess)

@app.route('/agendamento_consultas')
def agendamento_consultas():
    return render_template('agendamento_consultas.html')

@app.route('/verificar_agendamento_consultas', methods=['GET', 'POST'])
def verificar_agendamento_consultas():
    if request.method == 'POST':
        nome = request.form['nome']
        nome_tutor = request.form['nome_tutor']
        data = request.form['data']
        horario = request.form['horario']
        sintomas = request.form['sintomas']
        codigo = len(agendamento)
        agendamento.append([codigo, nome, nome_tutor, data, horario, sintomas])
        return render_template('lista_agendamento.html', agendamento=agendamento)

@app.route('/edicao_cadastro')
def edicao_cadastro():
    return render_template('edicao_cadastro.html')

@app.route('/verificar_edicao_cadastro/<int:codigo>', methods=['GET', 'POST'])
def verificar_edicao_cadastro(codigo):
    if request.method == 'POST':
        nome = request.form['nome']
        especie = request.form['especie']
        raca = request.form['raca']
        peso = request.form['peso']
        nome_tutor = request.form['nome_tutor']
        telefone = request.form['telefone']
        pacientess[codigo] = [codigo, nome, especie, raca, peso, nome_tutor, telefone]
        return render_template('lista_pacientes.html', pacientes=pacientess)

    else:
        paciente = pacientess[codigo]
        return render_template('edicao_cadastro.html', paciente=paciente)

@app.route('/lista_agendamento')
def lista_agendamento():
    return render_template('lista_agendamento.html', agendamento=agendamento)

@app.route('/cancelamento_consultas/<int:codigo>')
def cancelamento_consultas(codigo):
    del agendamento[codigo]
    return redirect('/lista_agendamento')

@app.route('/idade_humana')
def idade_humana():
    return render_template('idade_humana.html')

@app.route('/verificar_idade', methods=['POST'])
def verificar_idade():

    especie = (request.form['especie'])
    idade = int(request.form['idade'])

    if especie.lower() == 'cachorro':
        if idade == 1:
            idade_humana = 15
        elif idade == 2:
            idade_humana = 24
        elif idade == 3:
            idade_humana = 28
        elif idade == 4:
            idade_humana = 32
        elif idade == 5:
            idade_humana = 36
        elif idade == 6:
            idade_humana = 40
        elif idade == 7:
            idade_humana = 44
        else:
            idade_humana = 44 + (idade - 7) * 5

    elif especie.lower() == 'gato':
        if idade == 1:
            idade_humana = 15
        elif idade == 2:
            idade_humana = 24
        elif idade == 3:
            idade_humana = 28
        elif idade == 4:
            idade_humana = 32
        elif idade == 5:
            idade_humana = 36
        else:
            idade_humana = 36 + (idade - 5) * 4

    return render_template('idade_humana.html', idade_humana_python = f'A idade humana aproximada do {especie.lower()} é de aproximadamente {idade_humana} anos.', idade_humana=idade_humana)

@app.route('/medicamento')
def medicamento():
    return render_template('medicamento.html')

@app.route('/verificar_medicamento', methods=['POST'])
def verificar_medicamento():

    peso_animal = float(request.form['peso_animal'])
    dose_recomendada = float(request.form['dose_recomendada'])
    dose = peso_animal * dose_recomendada

    return render_template('medicamento.html', medicamento_python = f'A dose a ser administrada ao animal é de {dose} mg.',  medicamento=medicamento)

@app.route('/quantidade_mililitros_soro')
def quantidade_mililitros_soro():
    return render_template('quantidade_mililitros_soro.html')

@app.route('/verificar_quantidade_mililitros_soro', methods=['POST'])
def verificar_quantidade_mililitros_soro():

    peso_animal = float(request.form['peso_animal'])
    grau_desidratacao = request.form['grau_desidratacao']

    if grau_desidratacao.lower() == 'leve':
        volume_fluidoterapia = 50 * peso_animal
    elif grau_desidratacao.lower() == 'moderada':
        volume_fluidoterapia = 75 * peso_animal
    elif grau_desidratacao.lower() == 'grave':
        volume_fluidoterapia = 100 * peso_animal

    return render_template('quantidade_mililitros_soro.html', quantidade_mililitros_soro_python = f'Volume de fluidoterapia a ser administrado: {volume_fluidoterapia} mL.')

if __name__ == '__main__':
    app.run(debug=True)