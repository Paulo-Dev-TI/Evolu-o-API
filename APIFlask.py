# Importa da Biblioteca (Flask, Request e Jsonify)
from flask import Flask, jsonify
import requests
# Definindo um APP:
app = Flask(__name__)
# uma chave para acessar a API - YouTube:
api_key = "AIzaSyDvfc99RWFey0Ryo_kwkUp7-qBfJeyzUuw"
# Rota definida para /youtube/<busca>
@app.route("/youtube/<busca>")
def youtube(busca):
    # url da API youtube
    url = "https://www.googleapis.com/youtube/v3/search"
    # Os parametros da API:
    parametros = {
        "part": "snippet",
        "q": busca,
        "type": "video",
        "maxResults" : 5,
        "key": api_key    
    }
    # Organizando as Informações:
    resposta = requests.get(url, params=parametros)
    if resposta.status_code == 200:
        dados = resposta.json()
        # Lista com Videos e Titulos
        links = []
        # Laço for para cada 
        for item in dados["items"]:
            titulo = item["snippet"]["title"]
            video_id = item["id"]["videoId"]
            # link para buscar: 
            link = f"https://www.youtube.com/watch?v={video_id}"
            
            # Adiciona a Lista "Links"
            links.append({"titulo": titulo,
                          "url": link
                          })
        #retorna a lista Links:
        return jsonify(links)
    
    # Se caso for falso:
    else: 
        return {"erro":"Não foi possível acessar a API"}
app.run(debug=True)