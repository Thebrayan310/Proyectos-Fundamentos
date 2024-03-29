from flask import Flask, render_template, request, session
import random
import string

app = Flask(__name__)
app.secret_key = 'clave_secreta'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generador_contraseñas', methods=['GET', 'POST'])
def generador_contraseñas():
    if request.method == 'POST':
        longitud = int(request.form['longitud'])
        incluye_simbolos = 'incluye_simbolos' in request.form
        caracteres = string.ascii_letters + string.digits

        if incluye_simbolos:
            caracteres += string.punctuation

        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        return render_template('generador_contraseñas_resultado.html', contraseña=contraseña)

    return render_template('generador_contraseñas.html')

@app.route('/piedra_papel_tijeras')
def piedra_papel_tijeras():
    return render_template('piedra_papel_tijeras.html')

@app.route('/piedra_papel_tijeras_resultado', methods=['POST'])
def piedra_papel_tijeras_resultado():
    if 'eleccion' not in request.form:
        return render_template('piedra_papel_tijeras.html', error="Debes seleccionar una opción antes de jugar.")
    
    opciones = ['piedra', 'papel', 'tijeras']
    eleccion_usuario = request.form['eleccion']
    eleccion_computadora = random.choice(opciones)

    if eleccion_usuario == eleccion_computadora:
        resultado = "¡Empate!"
    elif (eleccion_usuario == 'piedra' and eleccion_computadora == 'tijeras') or \
         (eleccion_usuario == 'papel' and eleccion_computadora == 'piedra') or \
         (eleccion_usuario == 'tijeras' and eleccion_computadora == 'papel'):
        resultado = "¡Ganaste!"
    else:
        resultado = "¡Perdiste!"

    return render_template('piedra_papel_tijeras_resultado.html', resultado=resultado, eleccion_usuario=eleccion_usuario, eleccion_computadora=eleccion_computadora)

if __name__ == '__main__':
    app.run(debug=True)

