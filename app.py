from flask import Flask
from summarize import main as summarize_main
from transcript import main as transcript_main

app = Flask(__name__)

@app.route('/')
def index():
    try:
        transcript_main()
        summarize_main()
        return "Transcription et résumé terminés avec succès ✅"
    except Exception as e:
        return f"Erreur pendant l'exécution : {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)