#8
peliculas = [
    ["Inception", 2010, 8.8],
    ["Titanic", 1997, 7.8],
    ["The Matrix", 1999, 8.7],
    ["Avengers: Endgame", 2019, 8.4],
    ["The Room", 2003, 3.7],
    ["Interstellar", 2014, 8.6],
    ["Cats", 2019, 2.8]
]
filtro=list(filter(lambda x:x[2]>8.5,peliculas))
filtro.sort(key=lambda x:x[1],reverse=True)
acomodo=list(map(lambda x:f"{x[0]} ({x[1]}) - ⭐ {x[2]}",filtro))
print(acomodo)
"Título (Año) - ⭐ Calificación"