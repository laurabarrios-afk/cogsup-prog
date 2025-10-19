from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_r, K_g, K_o, K_b, C_RED, C_BLUE, C_GREEN, C_EXPYRIMENT_ORANGE
import random
import itertools

""" Constants """
KEYS = [K_r, K_b, K_g, K_o]
TRIAL_TYPES = ["Match","Mismatch"]
COLORS = ["red","blue","green","orange"]
N_BLOCKS = 8
N_TRIALS_IN_BLOCK = 16
COLOR_TO_KEY = {"red": K_r, "blue": K_b, "green": K_g,"orange": K_o}

INSTR_START = """
In this task, you have to indicate the color in which the word is written.
Press the initial of the color (r for red, g for green, o for orange and b for blue).\n
Press SPACE to continue.
"""
INSTR_MID = """You have finished one block of the experiment, well done! Your task will be the same.\nTake a break then press SPACE to move on to the second half."""
INSTR_END = """Well done!\nPress SPACE to quit the experiment."""

FEEDBACK_CORRECT = """The response was correct"""
FEEDBACK_INCORRECT = """The response was incorrect"""

""" Helper functions """
def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(*stims):
    t0 = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    t1 = exp.clock.time
    return t1 - t0

def present_for(*stims, t=1000):
    dt = timed_draw(*stims)
    exp.clock.wait(t - dt)

def present_instructions(text):
    instructions = stimuli.TextScreen(text=text, text_justification=0, heading="Instructions")
    instructions.present()
    exp.keyboard.wait()

def derangements(lst): #Function to create all the permutations in which no element appears in the orginal position
    ders = [] 
    for perm in itertools.permutations(lst): #Iterates over every possible combianation
        if all(original != perm[idx] for idx, original in enumerate(lst)): #Selects the permutations in which 
            #each element is not in its original position
            ders.append(perm) #Adds it to the list of derangements 
    return ders


""" Global settings """
exp = design.Experiment(name="Stroop", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(['block_cnt', 'trial_cnt', 'trial_type', 'word', 'color', 'RT', 'correct'])

control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
fixation = stimuli.FixCross()
fixation.preload()

N_BLOCKS=16
N_TRIALS_IN_BLOCK
PERMS=derangements(COLORS) 



feedback_correct = stimuli.TextLine(FEEDBACK_CORRECT)
feedback_incorrect = stimuli.TextLine(FEEDBACK_INCORRECT)
load([feedback_correct, feedback_incorrect])

""" Experiment """
def run_trial(block_id, trial_id, trial_type, word, color):
    stim = stimuli.TextLine(text=word, text_colour=color)
    present_for(fixation, t=500)
    stim.present()
    key, rt = exp.keyboard.wait(KEYS)
    if key == COLOR_TO_KEY[color]:
        correct = True
    else:
        correct = False
    exp.data.add([block_id, trial_id, trial_type, word, color, rt, correct])
    feedback = feedback_correct if correct else feedback_incorrect
    present_for(feedback, t=1000)

control.start(subject_id=1)

order=(exp.subject-1)%len(PERMS) #Ensures each participant gets a different derangement based on their ids
perm=PERMS[order] #Selects said derangement 
#Ordered list of all trials (8 elements)
baseTrials = ([{"trial_type":"match","word":c,"color":c} for c in COLORS]+[{"trial_type":"mismatch","word":w,"color":c} for w,c in zip(COLORS, perm)])
block_repetitions=N_TRIALS_IN_BLOCK//len(baseTrials) #Obtains the number of times trials must be repeated 
#to achieve the desire number of trials

blocks = []
for b in range(1, N_BLOCKS + 1):
    b_trials=baseTrials*block_repetitions #Generates a list with that amount of trials
    random.shuffle(b_trials)
    trials=[{"block_id": b, "trial_id": i, **t} for i, t in enumerate(b_trials, 1)]
    blocks.append(trials)

present_instructions(INSTR_START)
for block_id in range(1, N_BLOCKS + 1):
    for trial_id in range(1, N_TRIALS_IN_BLOCK + 1):
        trial_type = random.choice(TRIAL_TYPES)
        word = random.choice(COLORS)
        if trial_type=="match":
            color = word 
        else:
            color = random.choice([c for c in COLORS if c != word])
        run_trial(block_id, trial_id, trial_type, word, color)
    if block_id != N_BLOCKS:
        present_instructions(INSTR_MID)
present_instructions(INSTR_END)

control.end()