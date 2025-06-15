import pandas as pd
import matplotlib.pyplot as plt
Peliculas = {
    '1':{
        'Nombre':'El Padrino',
        'Año':1972,
        'rating':9.2,
        'Duracion':175,
    },
    '   2': {
        'Nombre': 'El Caballero de la Noche',
        'Año': 2008,
        'rating': 9.0,
        'Duracion': 152,
    },
    '3': {
        'Nombre': 'Pulp Fiction',
        'Año': 1994,
        'rating': 8.9,
        'Duracion': 154,
    },
    '4': {
        'Nombre': 'Forrest Gump',
        'Año': 1994,
        'rating': 8.8,
        'Duracion': 142,
    },
    '5': {
        'Nombre': 'Inception',
        'Año': 2010,
        'rating': 8.8,
        'Duracion': 148,
    },
    '6': {
        'Nombre': 'Matrix',
        'Año': 1999,
        'rating': 8.7,
        'Duracion': 136,
    },
    '7': {
        'Nombre': 'Parasite',
        'Año': 2019,
        'rating': 8.6,
        'Duracion': 132,
    },
    '8': {
        'Nombre': 'Interstellar',
        'Año': 2014,
        'rating': 8.6,
        'Duracion': 169,
    },
    '9': {
        'Nombre': 'El Señor de los Anillos: La Comunidad del Anillo',
        'Año': 2001,
        'rating': 8.8,
        'Duracion': 178,
    },
    '10': {
        'Nombre': 'Titanic',
        'Año': 1997,
        'rating': 7.9,
        'Duracion': 195,
    },
    '11': {
        'Nombre': 'Gladiator',
        'Año': 2000,
        'rating': 8.5,
        'Duracion': 155,
    },
    '12': {
        'Nombre': 'El Silencio de los Inocentes',
        'Año': 1991,
        'rating': 8.6,
        'Duracion': 118,
    },
    '13': {
        'Nombre': 'Fight Club',
        'Año': 1999,
        'rating': 8.8,
        'Duracion': 139,
    },
    '14': {
        'Nombre': 'La La Land',
        'Año': 2016,
        'rating': 8.0,
        'Duracion': 128,
    },
    '15': {
        'Nombre': 'Avengers: Endgame',
        'Año': 2019,
        'rating': 8.4,
        'Duracion': 181,
    },
    '16': {
        'Nombre': 'El Laberinto del Fauno',
        'Año': 2006,
        'rating': 8.2,
        'Duracion': 118,
    },
    '17': {
        'Nombre': 'Whiplash',
        'Año': 2014,
        'rating': 8.5,
        'Duracion': 106,
    },
    '18': {
        'Nombre': 'Toy Story',
        'Año': 1995,
        'rating': 8.3,
        'Duracion': 81,
    },
    '19': {
        'Nombre': 'Coco',
        'Año': 2017,
        'rating': 8.4,
        'Duracion': 105,
    },
    '20': {
        'Nombre': 'El Gran Hotel Budapest',
        'Año': 2014,
        'rating': 8.1,
        'Duracion': 99,
    },
}

def CrearDataFrame(peliculas):
    df = pd.DataFrame.from_dict(peliculas, orient='index')
    print("El Dataframe se ha creado correctamente.")
    return df

def MostrarDataFrame(df):
    print(df)
def MostarPeliculasMejorValoradas(df):
   df.sort_values(  by='rating', ascending=False, inplace=True)
   print("Las peliculas mejor valoradas son:")
   print(df[['Nombre', 'rating']].head(10))
   df.reset_index(drop=True, inplace=True) 
def CrearGrafico(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['rating'], bins=10, color='red', alpha=0.7, edgecolor='black')
    plt.title('Distribución de Ratings de Peliculas')
    plt.xlabel('Rating')
    plt.ylabel('Cantidad de Peliculas')
    plt.show()
PeliculasDataframe = CrearDataFrame(Peliculas)
MostrarDataFrame(PeliculasDataframe);
MostarPeliculasMejorValoradas(PeliculasDataframe)    
CrearGrafico(PeliculasDataframe)