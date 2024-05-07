from maps.main_map import MAIN_MAP
from maps.ING_AU_map import ING_AU_MAP

from math import hypot

class MapsManager:
    def __init__(self, scene):
        self.maps = {
            "Main": MAIN_MAP,
            "ING-AU": ING_AU_MAP
        }
        self.target_nodes = {}
        self.scene = scene
        self.finding_path = False
        
        self.path = []
        
        
    def load( self ):
        for map_name, m in self.maps.items():
            m.setup()
            m.set_scene( self.scene )
            m.load( self.scene.asset_manager )
            
            for box in m.boxes:
                if "name" in box.keys() and "enter_node" in box.keys():
                    new_target_node = { 
                                       "name": box["name"],
                                       "id": box["name"],
                                       "map": map_name,
                                       "pos": box["box_center"],
                                       "link": [ box["enter_node"] ]
                                    }
                    self.target_nodes[ box["name"] ] = new_target_node
                    
    def start_find( self, end_id ):
        self.finding_path = True
        self.path = []
        
        self.open_set = {}
        self.closed_set = {}
        self.nodes = { **self.target_nodes }
        for m in self.maps.values():
            for node in m.nodes:
                self.nodes[node["id"]] = { **node }
                
        self.start_node = self.nodes["1"]
        self.end_node = self.nodes[end_id]
        
        self.start_node["g"] = 0
        self.start_node["f"] = self.heuristic( self.start_node, self.end_node)
        self.start_node["previous"] = False
        self.open_set[self.start_node["id"]] = self.start_node
        
    def heuristic( self, n, end ):
        n = n["pos"]
        end = end["pos"]
        return abs(n[0]-end[0]) + abs(n[1]-end[1])
        
    def loop( self ):
        if len(self.open_set.values()) > 0:
            current = min(self.open_set.values(), key=lambda d: d['f'])
            if current["id"] == str(self.end_node["link"][0]):
                print("Done")
                temp = current
                while temp["previous"]:
                    self.path.append(temp["pos"])
                    temp = temp["previous"]
                self.path.append(current["pos"])
                self.scene.map.set_path( self.path )
                self.finding_path = False
                
            print([ (x["id"], round(x["f"]), x in self.closed_set.values()) for x in self.open_set.values()])
            print(current["id"], current["link"])
            print()
            del self.open_set[ current["id"] ]
            self.closed_set[current["id"]] = current
            
            for n in current["link"]:
                neighbor = self.nodes[n]
                
                if not neighbor in self.closed_set.values():
                    c_pos = current["pos"]
                    n_pos = neighbor["pos"]
                    dist = hypot(c_pos[0]-n_pos[0], c_pos[1] - n_pos[1])
                    temp_g = current["g"] + dist 
                    if neighbor in self.open_set.values():
                        neighbor["g"] = temp_g
                    else:
                        neighbor["g"] = temp_g
                    self.open_set[neighbor["id"]] = neighbor
                    neighbor["previous"] = current
                    neighbor["h"] = self.heuristic( neighbor, self.end_node )
                    neighbor["f"] = neighbor["g"] + neighbor["h"]
                    
                    
                
        else:
            print("No solution")
            self.finding_path = False
        
    def get(self, name):
        self.maps[name].setup()
        return self.maps[name]