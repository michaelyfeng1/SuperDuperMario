import pygame
import pathlib

from macroDefines import *

class tile_cache_mgr(object):
    def __init__(self):
        super(Object, self).__init__()
        self.switcher = None
        self.element_list = {}

        self.set_switcher()
    
    def __add_element(self, element_name, element):
        self.elemenmt_list[element_name] = element

    def add_element(self, element_name, element):
        function = self.switcher.get(element_name)
        
        function(element_name, element)
    
    def set_switcher(self):
        self.switcher = {
            ELEMENT_MARIO: __add_element,
            ELEMENT_FIRE_BALL: __add_element,
            ELEMENT_GOOMBA: __add_element,
            ELEMENT_SHYGUY: __add_element,
            ELEMENT_MUSHROOM: __add_element,
            ELEMENT_FLOWER: __add_element,
            ELEMENT_QUESTION: __add_element,
            ELEMENT_CLOUD: __add_element,
            ELEMENT_TURTLE: __add_element,
            ELEMENT_TODD: __add_element
        }


class base_element(object):
    def __init__(self):
        super(Object, self).__init__()
        self.element_name = None
        self.frames = {}
        self.images = {}
        self.frames_path = {}
        self.num_of_frames = {}

    def set_element_name(self, element_name):
        self.element_name = element_name
    
    def get_element_name(self):
        return self.element_name
    

class mario(base_element):
    '''

    '''
    def __init__(self):
        super(object, self).__init__()
        self.frame_img_file_name_pattern = {}
        self.position = {}
        self.eat_mushroom = False
        self.eat_flower = False
        self.direction  = None
        self.frame_counter = 0

        self.mario_state = {}

        self.mario_local_frame = {}
        self.mario_local_images = {}
        self.mario_local_frames_path = {}
        self.mario_local_num_frames = {}

        self.mario_state_init()
    
    def mario_state_init(self):
        current_pattern  = None
        mario_frame_data_set = []

        self.element_name = 'mario_block'

        #Small Mario

        self.mario_local_frames_path[SMALL_MARIO_LEFT_S] = pathlib.Path('./resource/small_mario_frames')
        current_pattern = "M*S*g.png"
        self.load_frames(current_pattern, SMALL_MARIO_LEFT_S)

        assert (DEBUG_ENABLE), "Set Small Mario Static Left"

        self.mario_local_frames_path[SMALL_MARIO_LEFT_M] = pathlib.Path('./resource/small_mario_frames')
        current_pattern = "f*s.gif"
        self.load_frames(current_pattern, SMALL_MARIO_LEFT_M)

        assert (DEBUG_ENABLE), "Set Small Mario Dynamic Left"

        self.mario_local_frames_path[SMALL_MARIO_LEFT_J] = pathlib.Path('./resource/small_mario_frames')
        current_pattern = "M*J*g.png"
        self.load_frames(current_pattern, SMALL_MARIO_LEFT_J)

        assert (DEBUG_ENABLE), "Set Small Mario Jump Left"

        self.mario_local_frames_path[SMALL_MARIO_RIGHT_S] = pathlib.Path('./resource/small_mario_frames')
        current_pattern = "M*S*g*p.png"
        self.load_frames(current_pattern, SMALL_MARIO_RIGHT_S)

        assert (DEBUG_ENABLE), "Set Small Mario Static Right"

        self.mario_local_frames_path[SMALL_MARIO_RIGHT_M] = pathlib.Path('./resource/small_mario_frames')
        current_pattern = "f*s*p.gif"
        self.load_frames(current_pattern, SMALL_MARIO_RIGHT_M)

        assert (DEBUG_ENABLE), "Set Small Mario Dynamic Right"

        self.mario_local_frames_path[SMALL_MARIO_RIGHT_J] = pathlib.Path('./resource/small_mario_frames')
        current_pattern = "M*J*g*p.png"
        self.load_frames(current_pattern, SMALL_MARIO_RIGHT_J)

        assert (DEBUG_ENABLE), "Set Small Mario Jump Right"

        #Big Mario

        self.mario_local_frames_path[BIG_MARIO_LEFT_S] = pathlib.Path('./resource/big_mario_frames')
        current_pattern = "S*M*S*g.png"
        self.load_frames(current_pattern, BIG_MARIO_LEFT_S)

        assert (DEBUG_ENABLE), "Set Big Mario Static Left"

        self.mario_local_frames_path[BIG_MARIO_LEFT_M] = pathlib.Path('./resource/big_mario_frames')
        current_pattern = "f*s.gif"
        self.load_frames(current_pattern, BIG_MARIO_LEFT_M)

        assert (DEBUG_ENABLE), "Set Big Mario Dynamic Left"

        self.mario_local_frames_path[BIG_MARIO_LEFT_J] = pathlib.Path('./resource/big_mario_frames')
        current_pattern = "S*M*J*g.png"
        self.load_frames(current_pattern, BIG_MARIO_LEFT_J)

        assert (DEBUG_ENABLE), "Set Big Mario Jump Left"

        self.mario_local_frames_path[BIG_MARIO_RIGHT_S] = pathlib.Path('./resource/big_mario_frames')
        current_pattern = "S*M*S*g*p.png"
        self.load_frames(current_pattern, BIG_MARIO_RIGHT_S)

        assert (DEBUG_ENABLE), "Set Big Mario Static Right"

        self.mario_local_frames_path[BIG_MARIO_RIGHT_M] = pathlib.Path('./resource/big_mario_frames')
        current_pattern = "f*s*p.gif"
        self.load_frames(current_pattern, BIG_MARIO_RIGHT_M)

        assert (DEBUG_ENABLE), "Set Big Mario Dynamic Right"

        self.mario_local_frames_path[BIG_MARIO_RIGHT_J] = pathlib.Path('./resource/big_mario_frames')
        current_pattern = "S*M*J*g*p.png"
        self.load_frames(current_pattern, BIG_MARIO_RIGHT_J)

        assert (DEBUG_ENABLE), "Set Big Mario Jump Right"

        #Fire Mario
        self.mario_local_frames_path[FIRE_MARIO_LEFT_S] = pathlib.Path('./resource/fire_mario_frames')
        current_pattern = "F*M*S*g.png"
        self.load_frames(current_pattern, FIRE_MARIO_LEFT_S)

        assert (DEBUG_ENABLE), "Set Fire Mario Static Left"

        self.mario_local_frames_path[FIRE_MARIO_LEFT_M] = pathlib.Path('./resource/fire_mario_frames')
        current_pattern = "f*s.gif"
        self.load_frames(current_pattern, FIRE_MARIO_LEFT_M)

        assert (DEBUG_ENABLE), "Set Fire Mario Dynamic Left"

        self.mario_local_frames_path[FIRE_MARIO_LEFT_J] = pathlib.Path('./resource/fire_mario_frames')
        current_pattern = "F*M*J*g.png"
        self.load_frames(current_pattern, FIRE_MARIO_LEFT_J)

        assert (DEBUG_ENABLE), "Set Fire Mario Jump Left"

        self.mario_local_frames_path[FIRE_MARIO_RIGHT_S] = pathlib.Path('./resource/fire_mario_frames')
        current_pattern = "F*M*S*g*p.png"
        self.load_frames(current_pattern, FIRE_MARIO_RIGHT_S)

        assert (DEBUG_ENABLE), "Set Fire Mario Static Right"

        self.mario_local_frames_path[FIRE_MARIO_RIGHT_M] = pathlib.Path('./resource/fire_mario_frames')
        current_pattern = "f*s*p.gif"
        self.load_frames(current_pattern, FIRE_MARIO_RIGHT_M)

        assert (DEBUG_ENABLE), "Set Fire Mario Dynamic Right"

        self.mario_local_frames_path[FIRE_MARIO_RIGHT_J] = pathlib.Path('./resource/fire_mario_frames')
        current_pattern = "F*M*J*g*p.png"
        self.load_frames(current_pattern, FIRE_MARIO_RIGHT_J)

        assert (DEBUG_ENABLE), "Set Fire Mario Jump Right"

        self.frames[ELEMENT_MARIO] = self.mario_local_frame

    def set_mario_frames_img(self):
        self.load_frames(self.frame_img_file_name_pattern)

    def update_mario_frames(self, update_type):
        if update_type == STATE_UPDATE_TYPE_MOVE:
            pass
        elif update_type == STATE_UPDATE_TYPE_EAT:
            pass
    def update_mario_state(self):
        if self.eat_mushrrom is True:  
            self.update_mario_frames(STATE_UPDATE_TYPE_EAT)
        elif self.eat_flower is True:
            self.update_element_frames(STATE_UPDATE_TYPE_EAT)
        else:
            self.update_element_frames(STATE_UPDATE_TYPE_MOVE)
    
    def load_frames(self, file_name_pattern, index):
        mario_frames = []
        mario_images = []
        num_of_frame = 0

        for frame in self.mario_local_frames_path[index].glob(file_name_pattern):
            mario_frames.append(frame)

        for index, frame in enumerate(mario_frames):
            frame = ".\\" + str(frame)
            img = pygame.image.load(frame)
            mario_images.append(img)

            num_of_frame = num_of_frame + 1

            #Debug
            print(frame)
            print(img)
        
        print(num_of_frame)

        self.mario_local_frame[index] = mario_frames
        self.mario_local_images[index] = mario_images
        self.mario_local_num_frames[index] = num_of_frame

    def draw(self, screen, frame_counter):
        image = None

        if frame_counter % 100 == 0:
            self.frame_counter = self.frame_counter + 1
        
        if self.mario_state == MARIO_STATE_STAND:
            if self.direction == DIRECTION_LEFT:
                if self.eat_flower is True:
                    image = self.images[BIG_MARIO_LEFT_S]
                elif self.eat_mushroom is True:
                    image = self.images[FIRE_MARIO_LEFT_S]
                else:
                    image = self.images[SMALL_MARIO_LEFT_S]
            elif self.direction == DIRECTION_RIGHT:
                if self.eat_flower is True:
                elif self.eat_mushroom is True:
                    
                else:

        elif self.mario_state == MARIO_STATE_MOVE:
        
        elif self.mario_state == MARIO_STATE_JUMP:
        
        elif self.mario_state == MARIO_STATE_INVALID:
            assert (DEBUG_ENABLE), "Mario State Is Invalid"

        if self.frame_counter == self.num_of_frames:
            self.frame_counter = 0
        
        self.screen.blit(self.)