from maps.map import Map

buildings = [
    {
        "name": "IBC",
        "labels": {
            "long": "Isabel Brown Caces",
            "subtitle": "Escuela de Ing. Informática - Ing. Industrial "
        },
        "points": [ (360, 385), (448, 385), (448, 428), (360, 430) ]
    }, 
    {
        "name": "GEO",
        "labels": {
            "long": "Instituto de Geografía"
        },
        "points":      [ (358, 360), (400, 360), (448, 373), (448, 382), (358, 382) ]
    },
    {
        "name": "ING-AU",
        "labels": {
            "long": "Aulario de Ing. Química",
            "subtitle": "Ing. Quimica - Ing. en Minas - Ing. Metalúrgica"
        },
        "points":   [ (220, 520), (300, 520), (285, 580), (215, 580) ]
    },
    {
        "name": "ICT",
        "labels": {
            "long": "Ingeniría en Construción y Transporte"
        },
        "points": [ (265, 360), (320, 360), (320, 438), (265, 440) ]
    },
    {
        "name": "FIN",
        "labels": {
            "long": "Facultad Mayor de Ingeniería"
        },
        "points": [ (210, 370), (240, 370), (240, 440), (210, 440) ]
    },
    {
        "name": "RA",
        "labels": {
            "long": "Rafael Ariztía",
            "subtitle": "Ing. Eléctrica - Ing. Electrónica"
        },
        "points": [ (150, 360), (207, 360), (207, 440), (150, 440) ]
    }
]

streets = [
    {
        "name": "Errázuriz",
        "points": [ (  0, 220), ( 45, 225), (325, 300), (500, 350), 
                        (500, 385), (325, 335), ( 45, 270), (  0, 265) ]
    }, 
    {
        "name": "A",
        "points": [ (  0, 340), (360, 345), (395, 355), (  0, 355)]
    },
    {
        "name": "Brasil",
        "points": [ (  0, 443), (330, 443), (490, 430), (490, 450),
                        (345, 460), (  0, 460) ]
    },
    {
        "name": "BrasilB",
        "points": [ (  0, 485), (345, 485), (490, 480), (490, 495), (345, 500), (0, 500) ]
    }
]

land = [ (-20, 130), ( 95, 140), (160, 140), (230, 140), (275, 130), 
            (340, 125), (425, 110), (640,  50), (640, 1000), (-20, 1000) ]

MAIN_MAP = Map(
    size = (640, 1000),
    background = land,
    boxes = buildings,
    lines = streets,
    zoom_treshold = 1
)