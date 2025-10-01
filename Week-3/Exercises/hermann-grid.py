from expyriment import design, control, stimuli, misc

exp = design.Experiment(name="Launching")

control.initialize(exp)

width, height= exp.screen.size

def grid(size,space,rows,cols,color,background):
    totalWidth=(cols*size)+((cols-1)*space)
    totalHeigth=(rows*size)+((rows-1)*space)
    if totalHeigth>height or totalWidth>width:
        print("Requested grid is bigger than screen, cannot display")

    wMargin=(width-totalWidth)/2
    hMargin=(height-totalHeigth)/2
    
    exp.screen.colour=background
    exp.screen.clear()
    

    for row in range(rows):
        for col in range(cols):
            xpos=-width/2+wMargin+size/2+col*(size+space)
            ypos=height/2-hMargin-size/2-row*(size+space)
            square=stimuli.Rectangle((size,size), colour=color,line_width=0, position=(xpos,ypos))
            square.present(clear=False, update=False)
    
    exp.screen.update()
    exp.keyboard.wait() 
    
grid(200,30,7,10,misc.constants.C_BLACK,misc.constants.C_WHITE)
