from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/test-voice", methods=["POST"])
def voice_response():
    xml_response = """<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<Response>
  <Say voice=\"woman\" language=\"fr-FR\">Bonjour, ceci est un test de voix via Render. Le webhook fonctionne.</Say>
</Response>"""
    return Response(xml_response, status=200, mimetype="application/xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
