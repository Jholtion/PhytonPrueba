from flask  import Flask, jsonify, request

App = Flask(__name__)

@App.route('/')
def home():
    return "Bienvenido a la API de Flask"

@App.route('/mensaje', methods=['POST'])
def Enviar_mensaje():
    data = request.get_json()
    mensaje = data.get('mensaje','No hay mensaje')
    return jsonify({'mensaje': f'tu mensaje es: {mensaje}'}),201

if __name__ == '__main__':
    App.run(debug=True)