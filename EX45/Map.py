class Map(object):

    scenes = {
        'singapore' : Singapore(),
        'mumbai' : Mumbai(),
        'kairo' : Kairo(),
        'bucharest' : Bucharest(),
        'rome' : Rome(),
        'london' : London(),
        'trondheim' : Trondheim(),
        'death' : Death(),
        'finished' : Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('singapore')
a_game = Engine(a_map)
a_game.play()
