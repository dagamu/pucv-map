from maps.map import Map

buildings = [
    {
        "name": "IBC",
        "labels": {
            "long": "Edificio Isabel Brown Caces",
            "subtitle": "Escuela de Ing. Informática - Ing. Industrial "
        },
        "points": [ (360, 385), (448, 385), (448, 428), (360, 430) ],
        "collider": [ 360, 385, 88, 43 ],
        "info-img-offset": 250,
        "icons": [ "coffee", "computer-lab" ],
        "enter_node": 5
    }, 
    {
        "name": "GEO",
        "labels": {
            "long": "Instituto de Geografía"
        },
        "points":      [ (358, 360), (400, 360), (448, 373), (448, 382), (358, 382) ],
        "collider": [ 360, 360, 90, 20 ],
        "info-img-offset": 270,
        "icons": [ "computer-lab" ],
        "enter_node": 5
    },
    {
        "name": "ING-AU",
        "map-link": "ING-AU",
        "labels": {
            "long": "Aulario de Ing. Química",
            "subtitle": "Ing. Quimica - Ing. en Minas - Ing. Metalúrgica"
        },
        "points":   [ (220, 520), (300, 520), (285, 580), (215, 580) ],
        "collider": [ 220, 520, 80, 60 ],
        "info-img-offset": 200,
        "icons": [ "coffee", "computer-lab" ],
        "enter_node": 12
    },
    {
        "name": "ICT",
        "labels": {
            "long": "Ingeniría en Construción y Transporte"
        },
        "points": [ (265, 360), (320, 360), (320, 438), (265, 440) ],
        "collider": [265, 360, 55, 78 ],
        "info-img-offset": 200,
        "icons": [ "coffee", "computer-lab" ],
        "enter_node": 18
    },
    {
        "name": "FIN",
        "labels": {
            "long": "Facultad Mayor de Ingeniería"
        },
        "points": [ (210, 370), (240, 370), (240, 440), (210, 440) ],
        "collider": [ 210, 370, 30, 70 ],
        "info-img-offset": 200,
        "icons": [ "coffee", "library", "music" ],
        "enter_node": 8
        
    },
    {
        "name": "RA",
        "labels": {
            "long": "Edificio Rafael Ariztía",
            "subtitle": "Ing. Eléctrica - Ing. Electrónica"
        },
        "points": [ (150, 360), (207, 360), (207, 440), (150, 440) ],
        "collider": [ 150, 360, 57, 80 ],
        "info-img-offset": 205,
        "icons": [ "computer-lab" ],
        "enter_node": 8
    },
    {
        "name": "EIB",
        "labels": {
            "long": "Escuela de Ingeniería Bioquímica"
        },
        "points": [ (10, 380), (67, 380), (67, 440), (10, 440) ],
        "collider": [10, 380, 57, 60],
        "info-img-offset": 171,
        "icons": [ "computer-lab" ],
        "enter_node": 21
        
    }
]

streets = [
    {
        "name": "Errázuriz",
        "points": [ (  0, 220), ( 45, 225), (325, 300), (640, 390), 
                              (640, 425), (325, 335), ( 45, 270), (  0, 265) ]
    }, 
    {
        "name": "A",
        "points": [ (  0, 340), (360, 345), (395, 355), (  0, 355)]
    },
    {
        "name": "Brasil",
        "points": [ (  0, 443), (330, 443), (640, 420), (640, 440),
                              (345, 460), (  0, 460) ]
    },
    {
        "name": "BrasilB",
        "points": [ (  0, 485), (345, 485), (640, 475), (640, 490), (345, 500), (0, 500) ]
    },
    {
        "name": "Gral. Cruz",
        "points": [ (330, 350), (340, 350), (343,355), (345, 500), (310,720), (295, 720),
                           (330, 500), (330,465) ]
    },
    {
        "name": "B",
        "points": [(100,280), (110,280), (110,440), (80,720), (70,720), (100,430) ]
    },
    {
        "name": "C",
        "points": [ (460 , 375), (480, 375), (475,450), (410, 720), (388,720), (455,440)]
    }
]

land = [ (-20, 130), ( 95, 140), (160, 140), (230, 140), (275, 130), 
            (340, 125), (425, 110), (640,  50), (640, 1000), (-20, 1000) ]

green_areas = [ [ (-20,460), (340, 460), (640,440), (640,480), (340,485), (-20,485) ] ]

icons = [
    {
        "name": "subway",
        "pos": (385, 285)
    }
]

constraints = {
    "min_zoom": 0.75,
    "max_zoom": 2,
    "min_x": 0
}

nodes = [
    { "pos": (385, 285), "id": "1" , "link": ["14"] },
    { "pos": (485, 390), "id": "2" , "link": [ "3", "13"] },
    { "pos": (455, 375), "id": "3" , "link": [ "2", "4", "15"] },
    { "pos": (455, 425), "id": "4" , "link": [ "3", "5"] },
    { "pos": (400, 430), "id": "5" , "link": [ "6", "4"] },
    { "pos": (350, 435), "id": "6" , "link": [ "7", "5", "16"] },
    { "pos": (320, 435), "id": "7" , "link": [ "8", "9", "6", "18"] },
    { "pos": (220, 435), "id": "8" , "link": [ "7", "19"] },
    { "pos": (325, 465), "id": "9" , "link": [ "7", "10"] },
    { "pos": (325, 480), "id": "10", "link": ["11", "9"] },
    { "pos": (325, 505), "id": "11", "link": ["12", "10"] },
    { "pos": (255, 505), "id": "12", "link": ["11"] },
    { "pos": (495, 340), "id": "13", "link": ["14", "2"] },
    { "pos": (370, 305), "id": "14", "link": ["1", "13"] },
    { "pos": (395, 355), "id": "15", "link": ["16","3"] },
    { "pos": (345, 355), "id": "16", "link": ["15", "17", "6"] },
    { "pos": (325, 355), "id": "17", "link": ["18", "16"] },
    { "pos": (320, 410), "id": "18", "link": ["7", "17"] },
    { "pos": (115, 435), "id": "19", "link": ["8", "20"] },
    { "pos": (90, 435),  "id": "20", "link": ["19", "21"] },
    { "pos": (35, 435),  "id": "21", "link": ["20"] },
]

boundaries = [ 0, 0, 600, 700 ]

MAIN_MAP = Map(
    size = (640, 1000),
    background = land,
    boxes = buildings,
    lines = streets,
    green_areas = green_areas,
    icons = icons,
    nodes = nodes,
    boundaries = boundaries,
    opt = {
        "start-pos": (-185, 20),
        "return-action": ["scene", "App Menu"]
    }
)