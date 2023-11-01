from pgl import GWindow, GRect, GTimer, GPoint, GOval, GCompound, GPolygon, GLabel, GLine#, GImage
import random

#global variables:
BTN_SIZE = 40                         #how big the buttons are (width/height they are squares)
GAP = 15                              #how big the gap between buttons is
BTNS_HEIGHT = BTN_SIZE + GAP * 2      #how big the button area is on screen
GW_WIDTH = 1000                       #how big should the canvas be, how wide should the screen be
GW_HEIGHT = GW_WIDTH + BTNS_HEIGHT    #the canvas size + the buttons area

#COLORS: 
BLACK = '#222222'
DARK_GRAY = '#343434'
LIGHT_GRAY = '#A9A9A9'
WHITE = '#DCDCDC'
RED = '#CD3A3A'
YELLOW = '#ECD149'
BLUE = '#4652CF'

COLOR_BUTTONS = [ ] #list of the color selection buttons

COLOR = [ BLACK ] #variable for the currently selected color
CAN_DRAG = [ True, True, False, False ] #variables to tell what you are able to do to the canvas

gw = GWindow(GW_WIDTH, GW_HEIGHT)

def boxgame():#make boxes in my box game!
   gw.add_event_listener('mousedown', mousedown_action)
   gw.add_event_listener('drag', drag_action)
   gw.add_event_listener('click', click_action)
   make_buttons()

def make_buttons():#makes all of the buttons that appear at the top of the window
   def center_buttons():#makes all of the color selection buttons centered on the screen
      num_btns = len(COLOR_BUTTONS)
      base_btn_x = (GW_WIDTH / 2) - (num_btns * BTN_SIZE) / 2 - (num_btns * GAP) / 2
      for button in range(len(COLOR_BUTTONS)):
         COLOR_BUTTONS[button].set_location(base_btn_x + button * (GAP + BTN_SIZE), GAP)   
   def make_colors():#makes all of the color selection buttons
      gw.black = GRect(0, 0, BTN_SIZE, BTN_SIZE)
      gw.black.set_color(BLACK)
      gw.black.set_filled(True)
      gw.add(gw.black)
      COLOR_BUTTONS.append(gw.black)
      gw.red = GRect(0, 0, BTN_SIZE, BTN_SIZE)
      gw.red.set_filled(True)
      gw.red.set_color(RED)
      gw.add(gw.red)
      COLOR_BUTTONS.append(gw.red)
      gw.yellow = GRect(0, 0, BTN_SIZE, BTN_SIZE)
      gw.yellow.set_color(YELLOW)
      gw.yellow.set_filled(True)
      gw.add(gw.yellow)
      COLOR_BUTTONS.append(gw.yellow)
      gw.blue = GRect(0, 0, BTN_SIZE, BTN_SIZE)
      gw.blue.set_color(BLUE)
      gw.blue.set_filled(True)
      gw.add(gw.blue)
      COLOR_BUTTONS.append(gw.blue)
      gw.white = GRect(0, 0, BTN_SIZE, BTN_SIZE)
      gw.white.set_color(WHITE)
      gw.white.set_filled(True)
      gw.add(gw.white)
      COLOR_BUTTONS.append(gw.white)
      gw.colorbox = GOval(0+GAP, 0+GAP, BTN_SIZE, BTN_SIZE)
      gw.colorbox.set_color(COLOR[0])
      gw.colorbox.set_filled(True)
      gw.add(gw.colorbox)
   def make_background():#makes the background
      gw.background = GRect(0,0,GW_WIDTH,GW_HEIGHT)
      gw.background.set_color(WHITE)
      gw.background.set_filled(True)
      gw.add(gw.background)
   def make_btn_bg():#makes the bar behind all the buttons
      gw.btn_bg = GRect(0, 0, GW_WIDTH, BTNS_HEIGHT)
      gw.btn_bg.set_filled(True)
      gw.btn_bg.set_color(DARK_GRAY)
      gw.add(gw.btn_bg)
   def make_bucket():#makes the fill bucket button
      gw.bucket_bg = GOval(GW_WIDTH-BTN_SIZE-GAP, GAP, BTN_SIZE, BTN_SIZE)
      gw.bucket_bg.set_filled(True)
      gw.bucket_bg.set_color(LIGHT_GRAY)
      gw.add(gw.bucket_bg)
      gw.bucket = GOval(GW_WIDTH-BTN_SIZE-GAP+(BTN_SIZE/10), GAP+(BTN_SIZE/10), BTN_SIZE-(BTN_SIZE/10)*2, BTN_SIZE-(BTN_SIZE/10)*2)
      gw.bucket.set_filled(True)
      gw.bucket.set_color(DARK_GRAY)
      gw.add(gw.bucket)
   def make_resize():#makes the resize tool button
      OVAL_SIZE = BTN_SIZE / 5
      XV = GW_WIDTH - (BTN_SIZE + GAP) * 2
      gw.resize_circle = GOval(XV+BTN_SIZE/4, GAP+BTN_SIZE/4, BTN_SIZE/2, BTN_SIZE/2)
      gw.resize_circle.set_color(DARK_GRAY)
      gw.resize_circle.set_filled(True)
      gw.add(gw.resize_circle)
      gw.resize = GCompound()
      rect = GRect(XV, GAP, BTN_SIZE, BTN_SIZE)
      rect.set_color(LIGHT_GRAY)
      gw.resize.add(rect)
      circle = GOval(XV-OVAL_SIZE/2,GAP-OVAL_SIZE/2,OVAL_SIZE,OVAL_SIZE)
      circle.set_color(LIGHT_GRAY)
      circle.set_filled(True)
      gw.resize.add(circle)
      circle = GOval(XV-OVAL_SIZE/2+BTN_SIZE,GAP-OVAL_SIZE/2,OVAL_SIZE,OVAL_SIZE)
      circle.set_color(LIGHT_GRAY)
      circle.set_filled(True)
      gw.resize.add(circle)
      circle = GOval(XV-OVAL_SIZE/2,GAP-OVAL_SIZE/2+BTN_SIZE,OVAL_SIZE,OVAL_SIZE)
      circle.set_color(LIGHT_GRAY)
      circle.set_filled(True)
      gw.resize.add(circle)
      circle = GOval(XV-OVAL_SIZE/2+BTN_SIZE,GAP-OVAL_SIZE/2+BTN_SIZE,OVAL_SIZE,OVAL_SIZE)
      circle.set_color(LIGHT_GRAY)
      circle.set_filled(True)
      gw.resize.add(circle)
      gw.add(gw.resize)
   def make_delete():#makes the erase/delete button
      gw.delete = GRect(GW_WIDTH-(GAP+BTN_SIZE)*3,GAP,BTN_SIZE,BTN_SIZE)
      gw.delete.set_color(RED)
      x = gw.delete.get_x()
      y = gw.delete.get_y()
      line = GLine(x,y,x+BTN_SIZE,y+BTN_SIZE)
      line.set_color(RED)
      gw.add(line)
      line = GLine(x+BTN_SIZE,y,x,y+BTN_SIZE)
      line.set_color(RED)
      gw.add(line)
      gw.add(gw.delete)

   make_background()
   make_btn_bg()
   make_colors()
   make_bucket()
   make_resize()
   make_delete()
   center_buttons()

def click_action(event):#happens when you click
   obj = gw.get_element_at(event.get_x(), event.get_y())
   if event.get_y() < BTNS_HEIGHT:#only want to do things if you're clicking in the button area
      if obj == gw.colorbox:#if you click on the 'colorbox' or draw tool, you will be in drawing mode
         CAN_DRAG[2] = False
         CAN_DRAG[1] = True
         gw.bucket.set_color(DARK_GRAY)
         gw.bucket_bg.set_color(LIGHT_GRAY)
         gw.colorbox.set_color(COLOR[0])
         gw.resize_circle.set_color(DARK_GRAY)
         CAN_DRAG[3] = False
      elif obj == gw.delete:#if you click on the delete tool, you will be in deleteing things mode
         CAN_DRAG[3] = True
         gw.bucket.set_color(DARK_GRAY)
         gw.bucket_bg.set_color(LIGHT_GRAY)
         gw.colorbox.set_color(LIGHT_GRAY)
         gw.resize_circle.set_color(DARK_GRAY)
      elif obj == gw.bucket:#if you click on fill bucket tool, you are in fill mode
         CAN_DRAG[1] = False
         CAN_DRAG[2] = False
         CAN_DRAG[3] = False
         gw.bucket.set_color(COLOR[0])
         gw.bucket_bg.set_color(COLOR[0])
         gw.colorbox.set_color(LIGHT_GRAY)
         gw.resize_circle.set_color(DARK_GRAY)
      elif obj == gw.resize:# if you click on the resize tool, you are in resizing things mode
         gw.bucket.set_color(DARK_GRAY)
         gw.bucket_bg.set_color(LIGHT_GRAY)
         gw.resize_circle.set_color(LIGHT_GRAY)
         CAN_DRAG[2] = True
         CAN_DRAG[1] = False
         CAN_DRAG[3] = False
      elif obj in COLOR_BUTTONS:# if you click on a color, then switch your tool to that color(if you're able to use colors at the time)
         if CAN_DRAG[3] == False:
            COLOR[0] = obj.get_color()
            if CAN_DRAG[1] == True:
               gw.colorbox.set_color(COLOR[0])
            elif CAN_DRAG[2] == False:
               gw.bucket.set_color(COLOR[0])
               gw.bucket_bg.set_color(COLOR[0])

def mousedown_action(event):#happens on mousedown, i use this one specifically for if you are not clicking on a button
   x = event.get_x()
   y = event.get_y()
   gw.box = None
   if y > BTNS_HEIGHT:#only runs stuff if you click outside of the button area
      CAN_DRAG[0] = True#so you can start drawing a rectangle
      obj = gw.get_element_at(x,y)
      if CAN_DRAG[3] == True: #if you are in deleting mode, it will delete what you click on from the gwindow
         if obj == gw.background:#or set the background to white 
            gw.background.set_color(WHITE)
         elif obj != None:
            gw.remove(obj)
      elif CAN_DRAG[2] == True:#if you are in resizing mode, selects the box that is to be resized
         if obj != None and obj != gw.background:
            gw.box = obj
      elif CAN_DRAG[1] == True:#if you are in drawing mode, create a new box starting at the mousedown point
         gw.box = GRect(x, y, 0, 0)
         gw.box.set_color(COLOR[0])
         gw.box.set_filled(True)
         gw.add(gw.box)
      else:#if you are in fill mode, recolor the box you click on
         obj.set_color(COLOR[0])
   else: #if you click starting in the buttons area, make sure you are not able to draw a box
      CAN_DRAG[0] = False

def drag_action(event):#for when you drag the mouse
   if CAN_DRAG[2] == True and gw.box != None:#if you are in resizing mode, resize the box to the point you drag to
      x = event.get_x()
      y = event.get_y()
      boxx = gw.box.get_x()
      boxy = gw.box.get_y()
      if x > boxx and y > boxy:
         gw.box.set_size(x-boxx, y-boxy)
   elif CAN_DRAG[0] == True and CAN_DRAG[1] == True:# if you are in drawing mode, size the box to end at the point you drag to
      x = event.get_x()
      y = event.get_y()
      boxx = gw.box.get_x()
      boxy = gw.box.get_y()
      gw.box.set_size(x-boxx, y-boxy)
   #if you arent in either of those modes, drag should do nothing.
   


boxgame()