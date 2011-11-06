'''This modules contains the gameplay cocos layer that provides the
all the necessary things for controlling the player in GameScene.
'''

import cocos

import debug

class GameplayLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        debug.msg('Initializing gameplay layer')

        super(GameplayLayer, self).__init__()

    def on_enter(self):
        super(GameplayLayer, self).on_enter()

        self.parent.push_handlers(self)

    def on_exit(self):
        super(GameplayLayer, self).on_exit()

        self.parent.remove_handlers(self)

    def on_key_press(self, key, modifiers):
        player_input = self.parent.player.get_component('input')
        player_input.on_key_press(key, modifiers)

