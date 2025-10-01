from expyriment import design, control, stimuli, misc

exp = design.Experiment(name="Launching")

control.initialize(exp)

width, height= exp.screen.size
posXIzq=(-width/2)+(width*0.025)
posXDer=(width/2)-(width*0.025)
posYArr=(height/2)-(width*0.025)
posYAba=(-height/2)+(width*0.025)
square1=stimuli.Rectangle((width*0.05,width*0.05), colour=misc.constants.C_RED,line_width=1, position=(posXIzq,posYArr))
square2=stimuli.Rectangle((width*0.05,width*0.05), colour=misc.constants.C_RED,line_width=1, position=(posXIzq,posYAba))
square3=stimuli.Rectangle((width*0.05,width*0.05), colour=misc.constants.C_RED,line_width=1, position=(posXDer,posYArr))
square4=stimuli.Rectangle((width*0.05,width*0.05), colour=misc.constants.C_RED,line_width=1, position=(posXDer,posYAba))

square1.present(clear=True, update=False)
square2.present(clear=False, update=False)
square3.present(clear=False, update=False)
square4.present(clear=False, update=True)

exp.keyboard.wait()
control.end()