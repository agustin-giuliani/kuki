import requests


def consultar_internet(url):

    try:

        respuesta = requests.get(
            url,
            timeout=10
        )

        respuesta.raise_for_status()

        return respuesta.text

    except requests.RequestException as error:

        raise RuntimeError(
            "No se pudo consultar Internet: "
            + str(error)
        )


def buscar_internet(consulta):

    if not consulta or not consulta.strip():

        raise ValueError(
            "La consulta no puede estar vacia."
        )

    url = "https://es.wikipedia.org/w/rest.php/v1/search/page"

    parametros = {
        "q": consulta,
        "limit": 3
    }

    headers = {
        "User-Agent": "KUKI/1.0"
    }

    try:

        respuesta = requests.get(
            url,
            params=parametros,
            headers=headers,
            timeout=10
        )

        respuesta.raise_for_status()

        datos = respuesta.json()

        resultados = []

        for pagina in datos.get("pages", []):

            resultados.append({
                "titulo": pagina.get("title"),
                "descripcion": pagina.get("description"),
                "extracto": pagina.get("excerpt"),
                "url": (
                    "https://es.wikipedia.org/wiki/"
                    + pagina.get("key", "")
                )
            })

        return {
            "consulta": consulta,
            "resultados": resultados
        }

    except requests.RequestException as error:

        raise RuntimeError(
            "No se pudo buscar en Internet: "
            + str(error)
        )