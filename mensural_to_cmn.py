from fractions import *
import argparse

from pymei import *

# Simple figures
def sixteenth_note(attribute_dur, noterest):
    print("sixteenth note")
    attribute_dur.setValue('16')
    cmn_voice.addChild(noterest)

def eighth_note(attribute_dur, noterest):
    print("eighth note")
    attribute_dur.setValue('8')
    cmn_voice.addChild(noterest)

def dotted_eighth_note(attribute_dur, noterest):
    print("dotted eighth note")
    attribute_dur.setValue('8')
    noterest.addAttribute('dots', '1')
    cmn_voice.addChild(noterest)

def quarter_note(attribute_dur, noterest):
    print("quarter note")
    attribute_dur.setValue('4')
    cmn_voice.addChild(noterest)

def dotted_quarter_note(attribute_dur, noterest):
    print("dotted quarter note")
    attribute_dur.setValue('4')
    noterest.addAttribute('dots', '1')
    cmn_voice.addChild(noterest)

def half_note(attribute_dur, noterest):
    print("half note")
    attribute_dur.setValue('2')
    cmn_voice.addChild(noterest)

def dotted_half_note(attribute_dur, noterest):
    print("dotted half note")
    attribute_dur.setValue('2')
    noterest.addAttribute('dots', '1')
    cmn_voice.addChild(noterest)

def whole_note(attribute_dur, noterest):
    print("whole note")
    attribute_dur.setValue('1')
    cmn_voice.addChild(noterest)

def dotted_whole_note(attribute_dur, noterest):
    print("dotted whole note")
    attribute_dur.setValue('1')
    noterest.addAttribute('dots', '1')
    cmn_voice.addChild(noterest)

def square_note(attribute_dur, noterest):
    print("square note")
    attribute_dur.setValue('breve')
    cmn_voice.addChild(noterest)

def dotted_square_note(attribute_dur, noterest):
    print("dotted square note")
    attribute_dur.setValue('breve')
    noterest.addAttribute('dots', '1')
    cmn_voice.addChild(noterest)

# Simple / Compound figures (depending on the 'times' parameter)

def long_note(times, attribute_dur, noterest, tie_list):
    print("long note * " + str(times))
    if times == 1:
        attribute_dur.setValue('long')
        cmn_voice.addChild(noterest)
    else:
        # Getting the xml:id and attributes from the mensural note
        xmlid = noterest.getId()
        noterest.removeAttribute('dur')
        old_attributes = noterest.getAttributes()
        for i in range(1, times+1):
            newnote = MeiElement(noterest.name)
            newnote.setId(xmlid + "_" + str(i))
            newnote.setAttributes(old_attributes)
            newnote.addAttribute('dur', 'long')
            cmn_voice.addChild(newnote)
            # Ties: between units
            if times > 1 and i < times:
                interunits_tie = MeiElement('tie')
                interunits_tie.addAttribute('startid', '#' + xmlid + "_" + str(i))
                interunits_tie.addAttribute('endid', '#' + xmlid + "_" + str(i + 1))
                tie_list.append(interunits_tie)

def dotted_long_note(times, attribute_dur, noterest, tie_list):
    print("dotted long note * " + str(times))
    if times == 1:
        attribute_dur.setValue('long')
        noterest.addAttribute('dots', '1')
        cmn_voice.addChild(noterest)
    else:
        # Getting the xml:id and attributes from the mensural note
        xmlid = noterest.getId()
        noterest.removeAttribute('dur')
        old_attributes = noterest.getAttributes()
        for i in range(1, times+1):
            newnote = MeiElement(noterest.name)
            newnote.setId(xmlid + "_" + str(i))
            newnote.setAttributes(old_attributes)
            newnote.addAttribute('dur', 'long')
            newnote.addAttribute('dots', '1')
            cmn_voice.addChild(newnote)
            # Ties: between units
            if times > 1 and i < times:
                interunits_tie = MeiElement('tie')
                interunits_tie.addAttribute('startid', '#' + xmlid + "_" + str(i))
                interunits_tie.addAttribute('endid', '#' + xmlid + "_" + str(i + 1))
                tie_list.append(interunits_tie)

# Compound figures

def dotted_square_note_AND_dotted_whole_note(times, noterest, tie_list):
    print("( dotted square note + dotted whole note ) * " + str(times))
    # dotted square note + dotted whole note
    # Getting the xml:id and attributes from the mensural note
    xmlid = noterest.getId()
    noterest.removeAttribute('dur')
    old_attributes = noterest.getAttributes()
    for i in range (1, times + 1):
        # First Note: dotted square note
        newnote = MeiElement(noterest.name)
        newnote.setId(xmlid + "_" + str(2*i - 1))
        newnote.setAttributes(old_attributes)
        newnote.addAttribute('dur', 'breve')
        newnote.addAttribute('dots', '1')
        cmn_voice.addChild(newnote)
        # Second Note: dotted whole note
        newnote = MeiElement(noterest.name)
        newnote.setId(xmlid + "_" + str(2*i))
        newnote.setAttributes(old_attributes)
        newnote.addAttribute('dur', '1')
        newnote.addAttribute('dots', '1')
        cmn_voice.addChild(newnote)
        # Ties
        # For the compound unit (i.e., for the 'dotted square note + dotted whole note')
        intraunit_tie = MeiElement('tie')
        intraunit_tie.addAttribute('startid', '#' + xmlid + "_" + str(2*i - 1))
        intraunit_tie.addAttribute('endid', '#' + xmlid + "_" + str(2*i))
        tie_list.append(intraunit_tie)
        # Between the compound units
        if times > 1 and i < times:
            interunits_tie = MeiElement('tie')
            interunits_tie.addAttribute('startid', '#' + xmlid + "_" + str(2*i))
            interunits_tie.addAttribute('endid', '#' + xmlid + "_" + str(2*i + 1))
            tie_list.append(interunits_tie)

def dotted_long_note_AND_dotted_square_note (times, noterest, tie_list):
    print("( dotted long note + dotted square note ) * " + str(times))
    # dotted long note + dotted square note
    # Getting the xml:id and attributes from the mensural note
    xmlid = noterest.getId()
    noterest.removeAttribute('dur')
    old_attributes = noterest.getAttributes()
    for i in range(1, times + 1):
        # First Note: dotted long note
        newnote = MeiElement(noterest.name)
        newnote.setId(xmlid + "_" + str(2*i - 1))
        newnote.setAttributes(old_attributes)
        newnote.addAttribute('dur','long')
        newnote.addAttribute('dots','1')
        cmn_voice.addChild(newnote)
        # Second Note: dotted square note
        newnote = MeiElement(noterest.name)
        newnote.setId(xmlid + "_" + str(2*i))
        newnote.setAttributes(old_attributes)
        newnote.addAttribute('dur','breve')
        newnote.addAttribute('dots','1')
        cmn_voice.addChild(newnote)
        # Ties
        # For the compound unit (i.e., for the 'dotted square note + dotted whole note')
        intraunit_tie = MeiElement('tie')
        intraunit_tie.addAttribute('startid', '#' + xmlid + "_" + str(2*i - 1))
        intraunit_tie.addAttribute('endid', '#' + xmlid + "_" + str(2*i))
        tie_list.append(intraunit_tie)
        # Between the compound units
        if times > 1 and i < times:
            interunits_tie = MeiElement('tie')
            interunits_tie.addAttribute('startid', '#' + xmlid + "_" + str(2*i))
            interunits_tie.addAttribute('endid', '#' + xmlid + "_" + str(2*i + 1))
            tie_list.append(interunits_tie)

# Complex cases of compound figures (more than one option to choose from)

def eighteenth_minims_case(breve_default_value, noterest, tie_list):
    print(18)
    # Two cases based on the default value of the breve (either of 9 or 6 minims -the case of 4 is not pertinent-)
    if breve_default_value == 6:
        # dotted long note + dotted square note
        dotted_long_note_AND_dotted_square_note(1, noterest, tie_list)
    elif breve_default_value == 9:
        # 2 x (dotted square note + dotted whole note)
        dotted_square_note_AND_dotted_whole_note(2, noterest, tie_list)
    else:
        # should not happen
        print("MISTAKE! 18 minims and the default number of minims in the breve isn't 6 nor 9 (i.e., mensuration isn't any of [3,2], [2,3], or [3,3])")

def twentyfour_minims_case(longa_default_value, attribute_dur, noterest, tie_list):
    print(24)
    # Two cases based on the default value of the breve (either of 8 or 12 minims)
    if longa_default_value == 8:
        # 3 x (long note)
        long_note(3, attribute_dur, noterest, tie_list)
    elif longa_default_value == 12:
        # 2 x (dotted long note)
        dotted_long_note(2, attribute_dur, noterest, tie_list)
    else:
        # should not happen
        print("MISTAKE! 24 minims and the default number of minims in the long isn't 8 nor 12.")

def thirtysix_minims_case(longa_default_value, breve_default_value, attribute_dur, noterest, tie_list):
    print(36)
    # Two cases
    if longa_default_value == 12:
        # 3 x (dotted long note)
        dotted_long_note(3, attribute_dur, noterest, tie_list)
    elif longa_default_value == 18:
        # Another two cases
        if breve_default_value == 6:
            # 2 x (dotted long note + dotted square note)
            dotted_long_note_AND_dotted_square_note(2, noterest, tie_list)
        elif breve_default_value == 9:
            # 2 x (2 x (dotted square note + dotted whole note)) = 4 x (dotted square note + dotted whole note)
            dotted_square_note_AND_dotted_whole_note(4, noterest, tie_list)
        else:
            # should not happen
            print("MISTAKE! In the 36 minims, the breve default value isn't neither 6 nor 9")
    else:
        # should not happen
        print("MISTAKE! In the 36 minims, the long default value isn't neither 12 nor 18")

def fiftyfour_minims_case(longa_default_value, breve_default_value, noterest, tie_list):
    print(54)
    # Two cases
    if longa_default_value == 18:
        # Another two cases
        if breve_default_value == 6:
            # 3 x (dotted long note + dotted square note)
            dotted_long_note_AND_dotted_square_note(3, noterest, tie_list)
        elif breve_default_value == 9:
            # 3 x (2 x (dotted square note + dotted whole note)) = 6 x (dotted square note + dotted whole note)
            dotted_long_note_AND_dotted_square_note(6, noterest, tie_list)
        else:
            # should not happen
            print("MISTAKE! In the 54 minims, the breve default value isn't neither 6 nor 9.")
    elif longa_default_value == 27:
        # 2 x (3 x (dotted square note + dotted whole note)) = 6 x (dotted square note + dotted whole note)
        dotted_square_note_AND_dotted_whole_note(6, noterest, tie_list)
    else:
        # should not happen
        print("MISTAKE! In the 54 minims, the long default value isn't neither 18 nor 27.")

# Changes the value of a mensural note into a cmn note

def change_noterest_to_cmn(noterest, tie_list):
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

    # Semibreves, breves, longs, and maximas
    if value_in_minims == 2:
        whole_note(attribute_dur, noterest)
    elif value_in_minims == 3:
        dotted_whole_note(attribute_dur, noterest)
    elif value_in_minims == 4:
        square_note(attribute_dur, noterest)
    elif value_in_minims == 6:
        dotted_square_note(attribute_dur, noterest)
    elif value_in_minims == 9:
        dotted_square_note_AND_dotted_whole_note(1, noterest, tie_list)
    elif value_in_minims == 8:
        long_note(1, attribute_dur, noterest, tie_list)
    elif value_in_minims == 12:
        dotted_long_note(1, attribute_dur, noterest, tie_list)
    elif value_in_minims == 18:
        eighteenth_minims_case(prolatio * tempus, noterest, tie_list)
    elif value_in_minims == 27:
        dotted_square_note_AND_dotted_whole_note(3, noterest, tie_list)
    elif value_in_minims == 16:
        long_note(2, attribute_dur, noterest, tie_list)
    elif value_in_minims == 24:
        twentyfour_minims_case(prolatio * tempus * modusminor, attribute_dur, noterest, tie_list)
    elif value_in_minims == 36:
        thirtysix_minims_case(prolatio * tempus * modusminor, prolatio * tempus, attribute_dur, noterest, tie_list)
    elif value_in_minims == 54:
        fiftyfour_minims_case(prolatio * tempus * modusminor, prolatio * tempus, noterest, tie_list)
    elif value_in_minims == 81:
        dotted_square_note_AND_dotted_whole_note(9, noterest, tie_list)
    # Minims or below
    elif value_in_minims == 1:
        half_note(attribute_dur, noterest)
    elif value_in_minims == Fraction(1,2):
        quarter_note(attribute_dur, noterest)
    elif value_in_minims == Fraction(1,4):
        eighth_note(attribute_dur, noterest)
    elif value_in_minims == Fraction(1,8):
        sixteenth_note(attribute_dur, noterest)
    # Dotted (minims or below)
    elif value_in_minims == Fraction(3,2):
        dotted_half_note(attribute_dur, noterest)
    elif value_in_minims == Fraction(3,4):
        dotted_quarter_note(attribute_dur, noterest)
    elif value_in_minims == Fraction(3,8):
        dotted_eighth_note(attribute_dur, noterest)
    # Else?
    else:
        print("mistake?")

# Main part of the program, it takes the input and output file paths given by the user, 
# and transform each of the notes and rests in the input file to the corresponding cmn values and saves them in the output file
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This program takes a Mensural MEI file as input and converts it into a CMN MEI file.")
    parser.add_argument('input_file', help="Path of the Mensural MEI file to be converted into CMN. This Mensural MEI should encode the precise duration of each note of the mensural piece (i.e., it encodes both the note shape in @dur and the 'perfect'/'imperfect'/'altered' quality of the note in @num and @numbase).")
    parser.add_argument('output_file', help="Path of the output (CMN MEI) file")
    args = parser.parse_args()

    # Mensural MEI input file
    mensural_meidoc = documentFromFile(args.input_file).getMeiDocument()
    layers = mensural_meidoc.getElementsByName('layer')

    # The MEI document that will save the CMN MEI output file
    cmn_meidoc = documentFromFile(args.input_file).getMeiDocument()
    cmnlayers = cmn_meidoc.getElementsByName('layer')
    cmnStavesDef = cmn_meidoc.getElementsByName('staffDef')
    for layer in cmnlayers:
        layer.deleteAllChildren()

    tie_list_piece = []
    # Processing the elements on each staff
    for i in range(0, len(cmnStavesDef)):
        mensural_voice = layers[i]
        staffdef = cmnStavesDef[i]
        prolatio = int(staffdef.getAttribute('prolatio').value)
        tempus = int(staffdef.getAttribute('tempus').value)
        modusminor = int(staffdef.getAttribute('modusminor').value)
        modusmaior = int(staffdef.getAttribute('modusmaior').value)

        staffdef.removeAttribute('modusmaior')
        staffdef.removeAttribute('modusminor')
        staffdef.removeAttribute('tempus')
        staffdef.removeAttribute('prolatio')

        cmn_voice = cmnlayers[i]
        tie_list_per_voice = []

        # Processing each element in the staff
        for child in mensural_voice.getChildren():
            # Processing each note / rest in the staff
            if child.name == "note" or child.name == "rest":
                change_noterest_to_cmn(child, tie_list_per_voice)
            # Other elements are just copied as it
            else:
                cmn_voice.addChild(child)
        tie_list_piece.append(tie_list_per_voice)

    # Third MEI document: CMN MEI document with the <measure> element
    outcmn_meidoc = documentFromFile(args.input_file).getMeiDocument()
    outcmn_section = outcmn_meidoc.getElementsByName('section')[0]
    outcmn_section.deleteAllChildren()
    unique_measure = MeiElement('measure')
    unique_measure.addAttribute('n', '1')
    cmnStaves = cmn_meidoc.getElementsByName('staff')
    for i in range (0, len(cmnStaves)):
        cmnStaff = cmnStaves[i]
        unique_measure.addChild(cmnStaff)
        for tie in tie_list_piece[i]:
            unique_measure.addChild(tie)
    outcmn_section.addChild(unique_measure)


    documentToFile(outcmn_meidoc, args.output_file)