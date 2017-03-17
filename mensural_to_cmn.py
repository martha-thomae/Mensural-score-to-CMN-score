from fractions import *
import argparse

from pymei import *

# Simple figures

def whole_note():
    attribute_dur.setValue('1')
    cmn_voice.addChild(noterest)

def dotted_whole_note():
    attribute_dur.setValue('1')
    noterest.addAttribute('dots', '1')
    cmn_voice.addChild(noterest)

def square_note():
    attribute_dur.setValue('breve')
    cmn_voice.addChild(noterest)

def dotted_square_note():
    attribute_dur.setValue('breve')
    noterest.addAttribute('dots', '1')
    cmn_voice.addChild(noterest)

def long_note():
    attribute_dur.setValue('long')
    cmn_voice.addChild(noterest)

def dotted_long_note():
    attribute_dur.setValue('long')
    noterest.addAttribute('dots', '1')
    cmn_voice.addChild(noterest)

# Compound figures

def dotted_square_note_AND_dotted_whole_note(times):
    # dotted square note + dotted whole note
    # Getting the xml:id and attributes from the mensural note
    xmlid = noterest.getId()
    noterest.removeAttribute('dur')
    old_attributes = noterest.getAttributes()
    for i in range (1, times + 1):
        # First Note: dotted square note
        newnote = MeiElement('note')
        newnote.setId(xmlid + "_" + str(2*i - 1))
        newnote.setAttributes(old_attributes)
        newnote.addAttribute('dur', 'breve')
        newnote.addAttribute('dots', '1')
        cmn_voice.addChild(newnote)
        # Second Note: dotted whole note
        newnote = MeiElement('note')
        newnote.setId(xmlid + "_" + str(2*i))
        newnote.setAttributes(old_attributes)
        newnote.addAttribute('dur', '1')
        newnote.addAttribute('dots', '1')
        cmn_voice.addChild(newnote)

def dotted_long_note_AND_dotted_square_note (times):
    # dotted long note + dotted square note
    # Getting the xml:id and attributes from the mensural note
    xmlid = noterest.getId()
    noterest.removeAttribute('dur')
    old_attributes = noterest.getAttributes()
    for i in range(1, times + 1):
        # First Note: dotted long note
        newnote = MeiElement('note')
        newnote.setId(xmlid + "_" + str(2*i - 1))
        newnote.setAttributes(old_attributes)
        newnote.addAttribute('dur','long')
        newnote.addAttribute('dots','1')
        cmn_voice.addChild(newnote)
        # Second Note: dotted square note
        newnote = MeiElement('note')
        newnote.setId(xmlid + "_" + str(2*i))
        newnote.setAttributes(old_attributes)
        newnote.addAttribute('dur','breve')
        newnote.addAttribute('dots','1')
        cmn_voice.addChild(newnote)

def long_note(times):
    if times == 1:
        long_note()
    else:
        # Getting the xml:id and attributes from the mensural note
        xmlid = noterest.getId()
        noterest.removeAttribute('dur')
        old_attributes = noterest.getAttributes()
        for i in range(1, times+1):
            newnote = MeiElement('note')
            newnote.setId(xmlid + "_" + str(i))
            newnote.setAttributes(old_attributes)
            newnote.addAttribute('dur', 'long')
            cmn_voice.addChild(newnote)

def dotted_long_note(times):
    if times == 1:
        dotted_long_note()
    else:
        # Getting the xml:id and attributes from the mensural note
        xmlid = noterest.getId()
        noterest.removeAttribute('dur')
        old_attributes = noterest.getAttributes()
        for i in range(1, times+1):
            newnote = MeiElement('note')
            newnote.setId(xmlid + "_" + str(i))
            newnote.setAttributes(old_attributes)
            newnote.addAttribute('dur', 'long')
            newnote.addAttribute('dots', '1')
            cmn_voice.addChild(newnote)

def eighteenth_minims_case(breve_default_value):
    print(18)
    # Two cases based on the default value of the breve (either of 9 or 6 minims -the case of 4 is not pertinent-)
    if breve_default_value == 6:
        # dotted long note + dotted square note
        dotted_long_note_AND_dotted_square_note(1)
    elif breve_default_value == 9:
        # 2 x (dotted square note + dotted whole note)
        dotted_square_note_AND_dotted_whole_note(2)
    else:
        # should not happen
        print("MISTAKE! 18 minims and the default number of minims in the breve isn't 6 nor 9 (i.e., mensuration isn't any of [3,2], [2,3], or [3,3])")

def twentyfour_minims_case(longa_default_value):
    print(24)
    # Two cases based on the default value of the breve (either of 8 or 12 minims)
    if longa_default_value == 8:
        # 3 x (long note)
        long_note(3)
    elif longa_default_value == 12:
        # 2 x (dotted long note)
        dotted_long_note(2)
    else:
        # should not happen
        print("MISTAKE! 24 minims and the default number of minims in the long isn't 8 nor 12.")

def thirtysix_minims_case():
    print(36)
    # Two cases
    if longa_default_value == 12:
        # 3 x (dotted long note)
        dotted_long_note(3)
    elif longa_default_value == 18:
        # Another two cases
        if prolatio * tempus == 6:
            # 2 x (dotted long note + dotted square note)
            dotted_long_note_AND_dotted_square_note(2)
        elif prolatio * tempus == 9:
            # 2 x (2 x (dotted square note + dotted whole note)) = 4 x (dotted square note + dotted whole note)
            dotted_square_note_AND_dotted_whole_note(4)
        else:
            # should not happen
            print("MISTAKE! In the 36 minims, the breve default value isn't neither 6 nor 9")
    else:
        # should not happen
        print("MISTAKE! In the 36 minims, the long default value isn't neither 12 nor 18")

def fiftyfour_minims_case(longa_default_value):
    print(54)
    # Two cases
    if longa_default_value == 18:
        # Another two cases
        if prolatio * tempus == 6:
            # 3 x (dotted long note + dotted square note)
            dotted_long_note_AND_dotted_square_note(3)
        elif prolatio * tempus == 9:
            # 3 x (2 x (dotted square note + dotted whole note)) = 6 x (dotted square note + dotted whole note)
            dotted_long_note_AND_dotted_square_note(6)
        else:
            # should not happen
            print("MISTAKE! In the 54 minims, the breve default value isn't neither 6 nor 9.")
    elif longa_default_value == 27:
        # 2 x (3 x (dotted square note + dotted whole note)) = 6 x (dotted square note + dotted whole note)
        dotted_square_note_AND_dotted_whole_note(6)
    else:
        # should not happen
        print("MISTAKE! In the 54 minims, the long default value isn't neither 18 nor 27.")

# Changes the value of a mensural note into a cmn note

def change_noterest_to_cmn(noterest):
    print(noterest)
    # 1. Get the information of the figure related to its durational value (i.e., the information encoded in its attributes @dur, @num and @numbase):

    # Get the note shape (@dur)
    attribute_dur = noterest.getAttribute('dur')
    dur = attribute_dur.value
    # Get the ratio of its value (@num and @numbase)
    if noterest.hasAttribute('num') and noterest.hasAttribute('numbase'):
        ratio = Fraction(int(noterest.getAttribute('numbase').value), int(noterest.getAttribute('num').value))
        noterest.removeAttribute('num')
        noterest.removeAttribute('numbase')
        noterest.removeAttribute('quality')
    else:
        ratio = 1

    # 2. Get the value of the figure in terms of minims:

    # Figures which values are based on the mensuration
    if dur == 'semibrevis':
        value_in_minims = prolatio * ratio
    elif dur == 'brevis':
        value_in_minims = prolatio * tempus * ratio
    elif dur == 'longa':
        value_in_minims = prolatio * tempus * modusminor * ratio
    elif dur == 'maxima':
        value_in_minims = prolatio * tempus * modusminor * modusmaior * ratio
    # Figures of exclusively binary values
    elif dur == 'minima':
        value_in_minims = 1 * ratio
    elif dur == 'semiminima':
        value_in_minims = Fraction(1,2) * ratio
    elif dur == 'fusa':
        value_in_minims = Fraction(1,4) * ratio
    elif dur == 'semifusa':
        value_in_minims = Fraction(1,8) * ratio
    else:
        print("Mistake! Note " + str(noterest) + ". This figure is not allowed: " + str(dur) + "\n")

    # 3. Get the CMN figure(s) that represent that value of minims (considering a minim equal to a CMN half note):

    # At the moment, only semibreves, breves, longs, and maximas are considered (still missing everything smaller or equal than the minim)
    cmn_notes = {
        2: whole_note(),
        3: dotted_whole_note(),
        4: square_note(),
        6: dotted_square_note(),
        9: dotted_square_note_AND_dotted_whole_note(1),
        8: long_note(),
        12: dotted_long_note(),
        18: eighteenth_minims_case(prolatio * tempus),
        27: dotted_square_note_AND_dotted_whole_note(3)
        16: long_note(2)
        24: twentyfour_minims_case(prolatio * tempus * modusminor),
        36: thirtysix_minims_case(prolatio * tempus * modusminor),
        54: fiftyfour_minims_case(prolatio * tempus * modusminor),
        81: dotted_square_note_AND_dotted_whole_note(9)
    }

    cmn_notes[value_in_minims]

    # ... still missing notes smaller or equal to the minim...
    # undotted_soq_minim = [1, Fraction(1,2), Fraction(1,4), Fraction(1,8)]
    # dotted_soq_minim = 1.5 * soq_minim
    # soq_minim = undotted_soq_minim + dotted_soq_minim

    # soq_minim.index(value_in_minims)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This program takes a Mensural MEI file as input and converts it into a CMN MEI file.")
    parser.add_argument('input_file', help="Path of the Mensural MEI file to be converted into CMN. This Mensural MEI should encode the precise duration of each note of the mensural piece (i.e., it encodes both the note shape in @dur and the 'perfect'/'imperfect'/'altered' quality of the note in @num and @numbase).")
    parser.add_argument('output_file', help="Path of the output (CMN MEI) file")
    args = parser.parse_args()

    # Mensural MEI input file
    mensural_meidoc = documentFromFile(args.input_file).getMeiDocument()
    layers = mensural_meidoc.getElementsByName('layer')
    stavesDef = mensural_meidoc.getElementsByName('staffDef')

    # The MEI document that will save the CMN MEI output file
    cmn_meidoc = documentFromFile(args.input_file).getMeiDocument()
    cmnlayers = cmn_meidoc.getElementsByName('layer')
    for layer in cmnlayers:
        layer.deleteAllChildren()

    for i in range(0, len(stavesDef)):
        mensural_voice = layers[i]
        staffdef = stavesDef[i]
        prolatio = int(staffdef.getAttribute('prolatio').value)
        tempus = int(staffdef.getAttribute('tempus').value)
        modusminor = int(staffdef.getAttribute('modusminor').value)
        
        #modusmaior = int(staffdef.getAttribute('modusmaior').value)

        #staffdef.removeAttribute('modusmaior')
        staffdef.removeAttribute('modusminor')
        staffdef.removeAttribute('tempus')
        staffdef.removeAttribute('prolatio')

        cmn_voice = cmnlayers[i]

        for child in mensural_voice.getChildren():

            if child.name == "note" or child.name == "rest":
                change_noterest_to_cmn(child)
            else:
                cmn_voice.addChild(child)

    documentToFile(cmn_meidoc, args.output_file)