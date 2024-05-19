import pygame

class Animator:
    def __init__(self):
        self.animations = []
        self.frameCount = 0
        
    def reach_rect(self, get_rect, set_rect, target, end_action, frames ):
        new_anim = { 
                "type": "rect",
                "loop": self.rect_anim,
                "original": get_rect(),
                "get": get_rect,
                "set": set_rect,
                "target": target,
                "end_action": end_action,
                "start_time": self.frameCount,
                "end_time": self.frameCount + frames,
                "progress": 0
        }
        self.animations.append(new_anim)
        
    def rect_anim(self, anim):
        anim["progress"] = (self.frameCount - anim["start_time"]) / ( anim["end_time"] - self.frameCount  )
        
        org_pos = pygame.Vector2( anim["get"]().topleft )
        target_pos = pygame.Vector2( anim["target"].topleft )
        new_pos = org_pos.lerp( target_pos, anim["progress"] )
        
        org_size = pygame.Vector2( anim["get"]().size )
        target_size = pygame.Vector2( anim["target"].size )
        new_size = org_size.lerp( target_size, anim["progress"] )
        
        anim["set"]( pygame.Rect(new_pos, new_size) )
    
        
    def loop(self):
        self.frameCount += 1
        
        for i, anim in enumerate(self.animations):
            anim["loop"](anim)
            if round(anim["progress"], 2) == 1:
                anim["end_action"]()
                del self.animations[i]