from expyriment import design, control, stimuli, misc

exp = design.Experiment(name="Launching",background_colour=misc.constants.C_GREY)

control.initialize(exp)

width, height= exp.screen.size

square=stimuli.Rectangle((width*0.25,width*0.25), colour=misc.constants.C_GREY,line_width=0, position=(0,0))
circle1=stimuli.Circle(int(width*0.05), colour=misc.constants.C_BLACK,line_width=0, position=(width*0.125,width*0.125))
circle2=stimuli.Circle(int(width*0.05), colour=misc.constants.C_BLACK,line_width=0, position=(width*-0.125,width*0.125))
circle3=stimuli.Circle(int(width*0.05), colour=misc.constants.C_WHITE,line_width=0, position=(width*0.125,width*-0.125))
circle4=stimuli.Circle(int(width*0.05), colour=misc.constants.C_WHITE,line_width=0, position=(width*-0.125,width*-0.125))


circle1.present(clear=True, update=False)
circle2.present(clear=False, update=False)
circle3.present(clear=False, update=False)
circle4.present(clear=False, update=False)
square.present(clear=False, update=True)

exp.keyboard.wait()
control.end()