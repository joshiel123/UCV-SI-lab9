def get_local_culture_info(destination: str) -> dict:
    """Obtiene información estructurada sobre la cultura local del destino especificado.

    Retorna platos típicos (con ingredientes), costumbres locales (etiqueta social)
    y frases útiles/modismos comunes de destinos conocidos como Cusco, Buenos Aires,
    Arequipa y París, con un caso por defecto para otros destinos.

    Args:
        destination: Nombre del destino a consultar.

    Returns:
        Diccionario con claves:
            - status (str): "success" si la consulta fue exitosa.
            - destination (str): Destino consultado.
            - typical_dishes (list[str]): Platos e ingredientes tradicionales.
            - local_customs (list[str]): Costumbres, etiqueta social y normas de conducta.
            - useful_phrases (list[str]): Frases útiles o modismos comunes en el idioma local.
    """
    destination_normalized = destination.lower().strip()

    if "cusco" in destination_normalized or "cuzco" in destination_normalized:
        typical_dishes = [
            "Cuy chactado (cuy frito, sazonado con sal, ajo y pimienta)",
            "Chiri uchu (plato tradicional frío que incluye cuy, gallina, cecina, choclo y queso)",
            "Olluquito con charqui (olluco con carne seca de llama o alpaca)",
        ]
        local_customs = [
            "Respetar los templos y centros arqueológicos sagrados incas",
            "Agradecer a la Pachamama (Madre Tierra) y respetar las tradiciones locales",
            "Pedir permiso formal a los locales antes de tomarles fotos en trajes típicos",
        ]
        useful_phrases = [
            "Allianllachu (¿Cómo estás? en quechua)",
            "Asi no más (Expresión coloquial para indicar suficiencia)",
            "Choche / Pata (Amigo)",
        ]
    elif "buenos aires" in destination_normalized:
        typical_dishes = [
            "Asado argentino (cortes de carne vacuna cocidos a la parrilla)",
            "Milanesa a la napolitana (carne empanada con salsa de tomate, jamón y queso)",
            "Empanadas porteñas (rellenas de carne picada a cuchillo, cebolla y huevo)",
        ]
        local_customs = [
            "Saludar con un beso en la mejilla, incluso entre hombres que se conocen",
            (
                "Compartir el mate respetando no mover la bombilla ni agradecer "
                "hasta terminar de beber"
            ),
            "Cenar tarde, habitualmente después de las 9:00 PM o 10:00 PM",
        ]
        useful_phrases = [
            "Che (Tú o amigo/a)",
            "Boludo (Utilizado de manera amigable o despectiva según el tono)",
            "Pibe / Piba (Muchacho / Muchacha)",
        ]
    elif "arequipa" in destination_normalized:
        typical_dishes = [
            (
                "Rocoto relleno (rocoto relleno de carne molida, maní, pasas, "
                "cubierto de queso derretido)"
            ),
            "Chupe de camarones (sopa espesa de camarones de río con leche, queso y habas)",
            (
                "Adobo arequipeño (lomo de cerdo marinado en chicha de jora y "
                "especias, cocido en olla de barro)"
            ),
        ]
        local_customs = [
            "Visitar y comer en las picanterías tradicionales, especialmente los fines de semana",
            "Tener un gran orgullo regional y respeto por el volcán Misti",
            "Comer adobo arequipeño el domingo por la mañana",
        ]
        useful_phrases = [
            "¡Ay, qué diantres! (Expresión arequipeña de sorpresa)",
            "Choche (Amigo)",
            "Coro / Cora (Niño / Niña)",
        ]
    elif "parís" in destination_normalized or "paris" in destination_normalized:
        typical_dishes = [
            "Coq au vin (pollo estofado en vino tinto con champiñones y manteca)",
            (
                "Ratatouille (estofado de verduras con berenjena, calabacín, "
                "tomate y hierbas de Provenza)"
            ),
            "Croissants y baguettes elaborados con mantequilla francesa",
        ]
        local_customs = [
            (
                "Decir siempre 'Bonjour' (Buenos días) o 'Bonsoir' (Buenas tardes) "
                "al entrar a comercios"
            ),
            "Mantener el volumen de voz moderado en restaurantes y transporte público",
            "Dejar propina discrecional (el servicio ya está incluido en la cuenta)",
        ]
        useful_phrases = [
            "Bonjour (Buenos días / Hola)",
            "Merci beaucoup (Muchas gracias)",
            "S'il vous plaît (Por favor)",
        ]
    else:
        typical_dishes = [
            "Platos típicos del destino elaborados con ingredientes locales"
        ]
        local_customs = [
            "Investigar y respetar las normas de comportamiento locales antes de viajar",
            "Saludar de manera cortés respetando el espacio personal y la cultura del lugar"
        ]
        useful_phrases = [
            "Hola (en el idioma local)",
            "Por favor (en el idioma local)",
            "Gracias (en el idioma local)"
        ]

    return {
        "status": "success",
        "destination": destination,
        "typical_dishes": typical_dishes,
        "local_customs": local_customs,
        "useful_phrases": useful_phrases,
    }
