import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
import time


class Entity(object):
    def __init__(self):
        self._pos = (0, 0)
        self._size = (50, 50)
        self._instruction = Rectangle(
            pos=self._pos, size=self._size)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value
        self._instruction.pos = self._pos

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
        self._instruction.size = self._size

class RectClass(Entity):
        
    def __init__(self, pos, size):
        super().__init__()
        self.pos   = pos
        #self.size  = size
        self.size  = (Window.width/3, Window.height/3)
        #print("__init__")


class MyRoot(BoxLayout, Widget):
    def __init__(self):
        super(MyRoot, self).__init__()
        
    def generate_number(self):
        print("Button Pressed")
        
        input_pswd      = self.ids.text_box.text
        input_delay     = self.ids.delay_box.text
        if input_pswd == "Pswd":
            input_pswd = "012345678"
        if input_delay == "Delay":
            input_delay = "0.2"

        self.pswd       = [int(ele) for ele in list(input_pswd)]
        self.delay      = float(input_delay)
        
        self.index      = 0
        self.pswd_run   = 1
        self.register_event_type("on_frame")
       
        self._entities = set()

        #self.canvas.opacity = 1
        self.canvas.clear()
        
        self.mycanvas_width         = Window.width
        self.mycanvas_height        = Window.height         #Window.height *(1-0.05)
        self.button_offset_height   = 0                     #Window.height *(0.05)
        self.box_size               = (self.mycanvas_width/3, self.mycanvas_height/3)

        time.sleep(1)

        self.event1 = Clock.schedule_interval(self._on_frame, self.delay)
        self.event2 = Clock.schedule_interval(self.add_rect, self.delay)
       

    def add_rect(self, dt):
        legth_of_list = len(self.pswd)
        if self.pswd_run == 1:
            
            if self.index>=legth_of_list:
                self.index          = 0
                self.pswd_run       = 0
                self.canvas.clear()
                self.event1.cancel()
                self.event2.cancel()
                return

            x_loc        = 0
            y_loc        = 0
            curr_number  = self.pswd[self.index]
            self.index   = self.index+1
            
            if 0<=curr_number<=2:
                y_loc = self.button_offset_height
                x_loc = curr_number*(int(self.mycanvas_width/3))
            if 3<=curr_number<=5:
                y_loc = self.button_offset_height + int(self.mycanvas_height/3)
                x_loc = (curr_number%3)*(int(self.mycanvas_width/3))
            if 6<=curr_number<=8:
                y_loc = self.button_offset_height + (2*int(self.mycanvas_height/3))
                x_loc = (curr_number%3)*(int(self.mycanvas_width/3))
            
            self.add_entity(RectClass((x_loc, y_loc), self.box_size))
            
            print(self.index, curr_number, x_loc, y_loc, self.delay)
            self.bind(on_frame=self.move_step)


    def _on_frame(self, dt):
        self.dispatch("on_frame", dt)

    def on_frame(self, dt):
        pass

    def add_entity(self, entity):
        self.canvas.add(entity._instruction)

    def move_step(self, entity, dt):
        #self.canvas.remove(entity)
        self.canvas.clear()
        return
    
class Ajeeth(App):
    def build(self):
        return MyRoot()

Ajeeth_S = Ajeeth()
Ajeeth_S.run()
