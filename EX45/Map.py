import scenes

class Map(object):

    scenes = {
        'singapore' : scenes.Singapore(),
        'mumbai' : scenes.Mumbai(),
        'kairo' : scenes.Kairo(),
        'bucharest' : scenes.Bucharest(),
        'rome' : scenes.Rome(),
        'london' : scenes.London(),
        'trondheim' : scenes.Trondheim(),
        'death' : scenes.Death(),
        'finished' : scenes.Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
