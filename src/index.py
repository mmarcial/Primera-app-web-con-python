# framework para creacion de paginas web. tambien podemos usar django
# Para poder acceder al sitio debemos ejecutar el proyecto desde la consola.
# Con render_template hacemos uso de las plantillas html. Para que tome los archivos html sin pasar path se debe colocarlos
# en carpeta llamado templates. Si el nombre de la carpeta es diferente no encontrara los archivos.
from flask import Flask, render_template
# generamos variable general del proyecto
app = Flask(__name__)

# Generamos la ruta general de pagina o pagina de inicio
@app.route('/')
def home():
    return render_template('home.html')
# enrutamos otra seccion del sitio.
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)