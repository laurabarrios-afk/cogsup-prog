from expyriment import design, control, stimuli
from expyriment.misc.constants import K_SPACE, C_WHITE, C_BLUE, C_RED, C_YELLOW

exp = design.Experiment(name="ternus")
control.initialize(exp)
width,height=exp.screen.size
canvas=stimuli.Canvas(size=(width,height))

posX1=[(-width/4)*3,-width/4,width/4]
posX2=[-width/4,width/4,(width/4)*3]
colors=[C_YELLOW,C_BLUE,C_RED]

def make_circles(stims):
    canvas = stimuli.Canvas(size=(width,height))
    for stim in stims:
        stim.plot(canvas)
    canvas.present(clear=True, update=True)

def present_for(stims, frames):
    make_circles(stims)
    exp.clock.wait(frames * 16.67) 

def run_trials(rad, isi, use_tags):
    while True:
        circles1 = [stimuli.Circle(radius=rad, position=(pos,0), colour=C_WHITE) for pos in posX1]
        circles2 = [stimuli.Circle(radius=rad, position=(pos,0), colour=C_WHITE) for pos in posX2]
        tags1 = [stimuli.Circle(radius=20, position=(pos,0), colour=color) for pos,color in zip(posX1,colors)]
        tags2 = [stimuli.Circle(radius=20, position=(pos,0), colour=color) for pos,color in zip(posX2,colors)]

        if use_tags:  
            present_for(circles1 + tags1, 12)
        else:
            present_for(circles1, 12)         

        exp.clock.wait(isi*16.67)
                        
        if use_tags:
            present_for(circles2 + tags2, 12)
        else:
            present_for(circles2, 12)    

        if exp.keyboard.check(K_SPACE):
            break

        
run_trials(rad=200, isi=3, use_tags=False)
run_trials(rad=200, isi=30, use_tags=False)
run_trials(rad=200, isi=3, use_tags=True)

control.end()