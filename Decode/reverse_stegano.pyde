#declare variables for window 
b_width = 500
b_height = 500
    
  
def setup():
    global img
    background(0)
    size(b_width,b_height)
    img = loadImage("stegano.tiff") #global path
    image(img,0,0)#set as wallpaper
    take_pixel()
    
def take_pixel():
    Square=0 #big pixel
    incrementer=50
    sentence="" #output
    while Square<img.width*img.height:  #while i'm working on a square that is inside my image
        r=red(img.pixels[Square])
        g=green(img.pixels[Square])
        b=blue(img.pixels[Square])
        #i take my rgb colours
        Rtranslated=chr(int(r))
        Gtranslated=chr(int(g))
        Btranslated=chr(int(b))
        #translate them into numbers and then into letters
        sentence=sentence+Rtranslated+Gtranslated+Btranslated
        #all together
        Square+=50
        #makes end of line
        if(Square % width == 0):
            Square=Square + width * ( incrementer - 1 )
        if r==0 and g==0 and b==0 or r==255 and g==255 and b==255:
            break
        #if square is black i'm finished
     
                   
    text("La tua frase e':",b_width/2-200,b_height/2-50)
    print(sentence)
    text(sentence,b_width/2-200,b_height/2)
    
    
