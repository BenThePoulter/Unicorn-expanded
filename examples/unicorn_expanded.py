from time import sleep
import unicornhat as uh
import colorsys as col
def fill(R, G, B):
    for x in range(8):
        for y in range(8):
            uh.set_pixel(x, y, R, G, B)
def fadein():
    uh.brightness(0)
    for b in range(0, 91, 1):
        uh.brightness(b/100)
        uh.show()
        sleep(0.1)   
def fadeout():
    uh.brightness(0.9)
    for b in range(90, 0, -1):
        uh.brightness(b/100)
        uh.show()
        sleep(0.1)
def pulse(times):
    for i in range(times):
        uh.brightness(0.9)
        for b in range(90, 59, -1):
            uh.brightness(b/100)
            uh.show()
            sleep(0.04)
        for b in range(60, 91, 1):
            uh.brightness(b/100)
            uh.show()
            sleep(0.04)
def clear():
    uh.clear()
    uh.show()
def rainbow():
    def set_pixel_hsv(x,y,h,s,v):
        r, g, b = [int(c*255) for c in col.hsv_to_rgb(h,s,v)]
        uh.set_pixel(x,y,r,g,b)
    for y in range(8):
        for x in range(8):
            set_pixel_hsv(x,y,(1.0/8)*x,(1.0/8)*y,1.0)
            uh.show()
uh.brightness(0)
    
