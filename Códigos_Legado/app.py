from flask import Flask, render_template
import csv

app = Flask(__name__)

def carregar_csv(nome_arquivo):
    dados = []
    with open(nome_arquivo, encoding='utf-8') as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            dados.append(linha)
    return dados

@app.route('/')
def index():
    # Carregando dados dos CSVs
    vias = carregar_csv('transito.csv')
    onibus = carregar_csv('transporte.csv')
    clima = carregar_csv('clima.csv')[0] # Pega a primeira linha do clima

    for via in vias:
        v = int(via['velocidade_media'])
        c = int(via['carros_10min'])
        
        indice = v + c 
        via['indice'] = indice
        
        if indice > 100:
            via['status'] = "Congestionado"
        elif indice > 50:
            via['status'] = "Moderado"
        else:
            via['status'] = "Leve"

    try:
        sensacao = clima['temperatura'] + 5 # Vai dar erro se não converter para int
    except TypeError:
        sensacao = "Erro de Calculo"

    return render_template('index.html', vias=vias, onibus=onibus, clima=clima, sensacao=sensacao)

if __name__ == '__main__':
    app.run(debug=True)