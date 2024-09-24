from flask import Flask, render_template, request, jsonify
from tarefas import criar_sistema_tarefas, estado_ambiente

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/atualizar_estado', methods=['POST']) #Rota que  atualiza o estado do ambiente
def atualizar_estado():
    data = request.json
    # Quando o usuario inserir um valor, o estado sera atualizado.
    for key, value in data.items():
        if key in estado_ambiente:
            estado_ambiente[key] = int(value)  
    return jsonify({"message": "Valores atualizados!"})

@app.route('/executar_tarefas')
def executar_tarefas():
    sistema = criar_sistema_tarefas()
    tarefas_executadas = sistema.executar_tarefas()
    return jsonify(tarefas_executadas)

if __name__ == '__main__':
    app.run(debug=True)
