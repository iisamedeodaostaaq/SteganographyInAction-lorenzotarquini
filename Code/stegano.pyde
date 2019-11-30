#declare variables for window 
b_width = 500
b_height = 500
#arrays
split_words_array=[]
codes_array=[]

#setup make default background and takes the sentence
def setup():
    background(255)
    size(b_width,b_height)
    word = input("insert word or sentence:")
    print(word)
    assign(word)
    
#lib for input
def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)

#transform input in array
def assign(Input):
    i=0
    for i in range(len(Input)):
        split_words_array.append(Input[i])
    #check if sentence or word is 3 or multiple of 3
    check()
            
    make_codes(split_words_array)
        
#make an array with rgb codes
def make_codes(_array):
    triple_ascii = []
    i=0     
    for i in range (len(_array)):
        
        triple=_array[:3]
        triple_ascii=[ord(ascii) for ascii in triple]
        r = triple_ascii[0]
        g = triple_ascii[1]
        b = triple_ascii[2]
        codes_array.append(r)
        codes_array.append(g)
        codes_array.append(b)
        del(_array[:3])
        if not _array:
            break    
    i += 1
    divide_area(i,codes_array)
    
#divide area in pixels and colors them    
def divide_area(divide,codes = [], *args):
    i=0 #flows the array
    j=0 #flows the single square
    k=0 #is the single pixel in square
    piece_of_window=0
    codes_len = len(codes)
    single_square = 50
    loadPixels()
    while i < codes_len+1:
        
        r = codes[0]
        g = codes[1]
        b = codes[2]
        
        #colors pixels in certain range for make the 50pixels square
        for j in range(single_square):
            for k in range(single_square):
                pixels[ piece_of_window + k + ( width * j ) ]=color(r,g,b)
        piece_of_window += single_square
        del(codes_array[:3])
        if not codes:
            break
        i+=1
        #makes an end of line
        if(piece_of_window%width==0):
            piece_of_window=piece_of_window+width*(single_square-1)
    #fills squares to make a complete rect       
    while(piece_of_window%width!=0):
        for j in range (single_square):
            for k in range (single_square):
                pixels[ piece_of_window + k + ( width * j ) ]=color(0,0,0)
        piece_of_window+=single_square
    updatePixels()
    
    
    
    save("../reverse_stegano/stegano.tiff")
    

def check():
    
    global split_words_array,Input
    if len(split_words_array)%3 != 0:
        #if the length of sentence is not divisible for 3 then if that length  + 1 is divisible for 3 do that else do that
         if len(split_words_array)+1 %3 == 0:
             
             split_words_array.append(" ")#add a space to sentence (this means that length += 1)
             
         else:
            split_words_array.append(" ")
            check() #recursive function
    else:
        print("ok") #just dev check
    
    
    
