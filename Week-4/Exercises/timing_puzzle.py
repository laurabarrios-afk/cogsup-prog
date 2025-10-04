from expyriment import design, control, stimuli

exp = design.Experiment(name="timing puzzle")

control.initialize(exp)

fixation = stimuli.FixCross()
fixation.preload()
text = stimuli.TextLine("Fixation removed")
text.preload()

t0 = exp.clock.time
fixation.present()
t1=exp.clock.time
delay=t1-t0
exp.clock.wait(1000-delay)
t2=exp.clock.time

fix_duration = (t2 - t0)/1000

t0 = exp.clock.time
text.present()
t1 = exp.clock.time
delay=t0-t1
exp.clock.wait(1000-delay)

units = "second" if fix_duration == 1.0 else "seconds"
duration_text = f"Fixation was present on the screen for {fix_duration} {units}"

text2 = stimuli.TextLine(duration_text)
text2.present()
exp.clock.wait(2000)

control.end()