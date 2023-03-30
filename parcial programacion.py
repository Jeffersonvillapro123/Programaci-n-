import pandas
df = pandas.read_csv("resultados.csv")

def estadisticas(df: pandas.DataFrame):
    matematicas = (df["PUNT_MATEMATICAS"]).mean()
    tablalocal = df[(df["ESTU_MCPIO_RESIDE"]=="BARRANQUILLA")]
    promediolocal = (tablalocal["PUNT_MATEMATICAS"]).mean()
    nacional = (df["PUNT_MATEMATICAS"]).mean()
    if (nacional>promediolocal):
        mejor = "Nacional"
        promreg = nacional
    elif (promediolocal>nacional):
        mejor = "Local"
        promreg = promediolocal
    else:
        mejor = "Es igual"
        promreg = nacional

    noof = df[(df["COLE_NATURALEZA"]=="NO OFICIAL")]
    of = df[(df["COLE_NATURALEZA"]=="OFICIAL")]
    proof = (of["PUNT_MATEMATICAS"]).mean()
    pronof = (noof["PUNT_MATEMATICAS"]).mean()
    if (proof>pronof):
        mayor = "Oficial"
        prom = proof
    elif (pronof>proof):
        mayor = "No Oficial"
        prom = pronof
    else:
        mayor = "Es igual"
        prom = proof
    diccionario = {
        "nacional_math": matematicas,
        "performance_math": (mejor, promreg),
        "Mejor_resultado": (mayor, prom)
    }
    return diccionario
print(estadisticas(df))
