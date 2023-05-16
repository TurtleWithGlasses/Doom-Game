import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = "C:\\Users\\mhmts\\PycharmProjects\\Doom\\Resources\\sound\\"
        self.shotgun = pg.mixer.Sound(self.path + "resources_sound_shotgun.wav")
        self.npc_pain = pg.mixer.Sound(self.path + "resources_sound_npc_pain.wav")
        self.npc_death = pg.mixer.Sound(self.path + 'resources_sound_npc_death.wav')
        self.npc_shot = pg.mixer.Sound(self.path + 'resources_sound_npc_attack.wav')
        self.player_pain = pg.mixer.Sound(self.path + 'resources_sound_player_pain.wav')
        # self.theme = pg.mixer.music.load(self.path + 'resources_sound_theme.mp3')