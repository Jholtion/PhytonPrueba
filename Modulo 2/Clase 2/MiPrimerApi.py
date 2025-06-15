from flask import Flask, request, render_template
import pandas as pd

MiprimeraApi = Flask(__name__) 

@MiprimeraApi.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename.endswith('.csv'):
            df = pd.read_csv(file)
            resumen = {
                'Filas' : df.shape[0],
                'Columnas' : df.shape[1],
                'NombresColumnas' : list(df.columns),
            }
            return render_template('Upload.html', resumen=resumen)
        else:
            return "El archivo no es un CSV",400
    return render_template('Upload.html')

if  __name__ == '__main__':
    MiprimeraApi.run(debug=True)