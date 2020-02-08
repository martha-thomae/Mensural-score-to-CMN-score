from fractions import *
from random import randint
import argparse

from pymei import *

# Simple figures
def sixteenth_note(attribute_dur, noterest):
    #print("sixteenth note")
    attribute_dur.setValue('16')
    return noterest

def eighth_note(attribute_dur, noterest):
    #print("eighth note")
    attribute_dur.setValue('8')
    return noterest

def dotted_eighth_note(attribute_dur, noterest):
    #print("dotted eighth note")
    attribute_dur.setValue('8')
    noterest.addAttribute('dots', '1')
    return noterest

def quarter_note(attribute_dur, noterest):
    #print("quarter note")
    attribute_dur.setValue('4')
    return noterest

def dotted_quarter_note(attribute_dur, noterest):
    #print("dotted quarter note")
    attribute_dur.setValue('4')
    noterest.addAttribute('dots', '1')
    return noterest

def half_note(attribute_dur, noterest):
    #print("half note")
    attribute_dur.setValue('2')
    return noterest

def dotted_half_note(attribute_dur, noterest):
    #print("dotted half note")
    attribute_dur.setValue('2')
    noterest.addAttribute('dots', '1')
    return noterest

def whole_note(attribute_dur, noterest):
    #print("whole note")
    attribute_dur.setValue('1')
    return noterest

def dotted_whole_note(attribute_dur, noterest):
    #print("dotted whole note")
    attribute_dur.setValue('1')
    noterest.addAttribute('dots', '1')
    return noterest

def square_note(attribute_dur, noterest):
    #print("square note")
    attribute_dur.setValue('breve')
    return noterest

def dotted_square_note(attribute_dur, noterest):
    #print("dotted square note")
    attribute_dur.setValue('breve')
    noterest.addAttribute('dots', '1')
    return noterest

# Simple / Compound figures (depending on the 'times' parameter)

def long_note(times, attribute_dur, noterest, tie_list):
    #print("long note * " + str(times))
    if times == 1:
        attribute_dur.setValue('long')
        return noterest
    else:
        # Getting the xml:id and attributes from the mensural note
        noterest_list = []
        xmlid = noterest.getId()
        noterest.removeAttribute('dur')
        old_attributes = noterest.getAttributes()
        for i in range(1, times+1):
            newnote = MeiElement(noterest.name)
            newnote.setId(xmlid + "_" + str(i))
            newnote.setAttributes(old_attributes)
            newnote.addAttribute('dur', 'long')
            noterest_list.append(newnote)
            # Ties: between units
            if times > 1 and i < times:
                interunits_tie = MeiElement('tie')
                interunits_tie.addAttribute('startid', '#' + xmlid + "_" + str(i))
                interunits_tie.addAttribute('endid', '#' + xmlid + "_" + str(i + 1))
                tie_list.append(interunits_tie)
        return noterest_list

def dotted_long_note(times, attribute_dur, noterest, tie_list):
    #print("dotted long note * " + str(times))
    if times == 1:
        attribute_dur.setValue('long')
        noterest.addAttribute('dots', '1')
        return noterest
    else:
        # Getting the xml:id and attributes from the mensural note
        noterest_list = []
        xmlid = noterest.getId()
        noterest.removeAttribute('dur')
        old_attributes = noterest.getAttributes()
        for i in range(1, times+1):
            newnote = MeiElement(noterest.name)
            newnote.setId(xmlid + "_" + str(i))
            newnote.setAttributes(old_attributes)
            newnote.addAttribute('dur', 'long')
            newnote.addAttribute('dots', '1')
            cnoterest_list.append(newnote)
            # Ties: between units
            if times > 1 and i < times:
                interunits_tie = MeiElement('tie')
                interunits_tie.addAttribute('startid', '#' + xmlid + "_" + str(i))
                interunits_tie.addAttribute('endid', '#' + xmlid + "_" + str(i + 1))
                tie_list.append(interunits_tie)
        return noterest_list

# Compound figures

def dotted_square_note_AND_dotted_whole_note(times, noterest, tie_list):
    #print("( dotted square note + dotted whole note ) * " + str(times))
    # dotted square note + dotted whole note
    # Getting the xml:id and attributes from the mensural note
    noterest_list = []
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
        noterest_list.append(newnote)
        # Second Note: dotted whole note
        newnote = MeiElement(noterest.name)
        newnote.setId(xmlid + "_" + str(2*i))
        newnote.setAttributes(old_attributes)
        newnote.addAttribute('dur', '1')
        newnote.addAttribute('dots', '1')
        noterest_list.append(newnote)
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
    return noterest_list

def dotted_long_note_AND_dotted_square_note (times, noterest, tie_list):
    #print("( dotted long note + dotted square note ) * " + str(times))
    # dotted long note + dotted square note
    # Getting the xml:id and attributes from the mensural note
    noterest_list = []
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
        noterest_list.append(newnote)
        # Second Note: dotted square note
        newnote = MeiElement(noterest.name)
        newnote.setId(xmlid + "_" + str(2*i))
        newnote.setAttributes(old_attributes)
        newnote.addAttribute('dur','breve')
        newnote.addAttribute('dots','1')
        noterest_list.append(newnote)
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
    return noterest_list

# Complex cases of compound figures (more than one option to choose from)

def eighteenth_minims_case(breve_default_value, noterest, tie_list):
    #print(18)
    # Two cases based on the default value of the breve (either of 9 or 6 minims -the case of 4 is not pertinent-)
    if breve_default_value == 6:
        # dotted long note + dotted square note
        return dotted_long_note_AND_dotted_square_note(1, noterest, tie_list)
    elif breve_default_value == 9:
        # 2 x (dotted square note + dotted whole note)
        return dotted_square_note_AND_dotted_whole_note(2, noterest, tie_list)
    else:
        # should not happen
        print("MISTAKE! 18 minims and the default number of minims in the breve isn't 6 nor 9 (i.e., mensuration isn't any of [3,2], [2,3], or [3,3])")

def twentyfour_minims_case(longa_default_value, attribute_dur, noterest, tie_list):
    #print(24)
    # Two cases based on the default value of the breve (either of 8 or 12 minims)
    if longa_default_value == 8:
        # 3 x (long note)
        return long_note(3, attribute_dur, noterest, tie_list)
    elif longa_default_value == 12:
        # 2 x (dotted long note)
        return dotted_long_note(2, attribute_dur, noterest, tie_list)
    else:
        # should not happen
        print("MISTAKE! 24 minims and the default number of minims in the long isn't 8 nor 12.")

def thirtysix_minims_case(longa_default_value, breve_default_value, attribute_dur, noterest, tie_list):
    #print(36)
    # Two cases
    if longa_default_value == 12:
        # 3 x (dotted long note)
        return dotted_long_note(3, attribute_dur, noterest, tie_list)
    elif longa_default_value == 18:
        # Another two cases
        if breve_default_value == 6:
            # 2 x (dotted long note + dotted square note)
            return dotted_long_note_AND_dotted_square_note(2, noterest, tie_list)
        elif breve_default_value == 9:
            # 2 x (2 x (dotted square note + dotted whole note)) = 4 x (dotted square note + dotted whole note)
            return dotted_square_note_AND_dotted_whole_note(4, noterest, tie_list)
        else:
            # should not happen
            print("MISTAKE! In the 36 minims, the breve default value isn't neither 6 nor 9")
    else:
        # should not happen
        print("MISTAKE! In the 36 minims, the long default value isn't neither 12 nor 18")

def fiftyfour_minims_case(longa_default_value, breve_default_value, noterest, tie_list):
    #print(54)
    # Two cases
    if longa_default_value == 18:
        # Another two cases
        if breve_default_value == 6:
            # 3 x (dotted long note + dotted square note)
            return dotted_long_note_AND_dotted_square_note(3, noterest, tie_list)
        elif breve_default_value == 9:
            # 3 x (2 x (dotted square note + dotted whole note)) = 6 x (dotted square note + dotted whole note)
            return dotted_long_note_AND_dotted_square_note(6, noterest, tie_list)
        else:
            # should not happen
            print("MISTAKE! In the 54 minims, the breve default value isn't neither 6 nor 9.")
    elif longa_default_value == 27:
        # 2 x (3 x (dotted square note + dotted whole note)) = 6 x (dotted square note + dotted whole note)
        return dotted_square_note_AND_dotted_whole_note(6, noterest, tie_list)
    else:
        # should not happen
        print("MISTAKE! In the 54 minims, the long default value isn't neither 18 nor 27.")

# Changes the value of a mensural note into a cmn note

def value_in_minims(noterest):
    #print(noterest)
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
    #print(dur, value_in_minims)
    return value_in_minims

def change_noterest_to_cmn(noterest, value_in_minims, tie_list):
    # Get the note shape (@dur)
    attribute_dur = noterest.getAttribute('dur')
    
    # Semibreves, breves, longs, and maximas
    if value_in_minims == 2:
        cmnnote = whole_note(attribute_dur, noterest)
    elif value_in_minims == 3:
        cmnnote = dotted_whole_note(attribute_dur, noterest)
    elif value_in_minims == 4:
        cmnnote = square_note(attribute_dur, noterest)
    elif value_in_minims == 6:
        cmnnote = dotted_square_note(attribute_dur, noterest)
    elif value_in_minims == 9:
        cmnnote_list = dotted_square_note_AND_dotted_whole_note(1, noterest, tie_list)
    elif value_in_minims == 8:
        cmnnote = long_note(1, attribute_dur, noterest, tie_list)
    elif value_in_minims == 12:
        cmnnote = dotted_long_note(1, attribute_dur, noterest, tie_list)
    elif value_in_minims == 18:
        cmnnote_list = eighteenth_minims_case(prolatio * tempus, noterest, tie_list)
    elif value_in_minims == 27:
        cmnnote_list = dotted_square_note_AND_dotted_whole_note(3, noterest, tie_list)
    elif value_in_minims == 16:
        cmnnote_list = long_note(2, attribute_dur, noterest, tie_list)
    elif value_in_minims == 24:
        cmnnote_list = twentyfour_minims_case(prolatio * tempus * modusminor, attribute_dur, noterest, tie_list)
    elif value_in_minims == 36:
        cmnnote_list= thirtysix_minims_case(prolatio * tempus * modusminor, prolatio * tempus, attribute_dur, noterest, tie_list)
    elif value_in_minims == 54:
        cmnnote_list = fiftyfour_minims_case(prolatio * tempus * modusminor, prolatio * tempus, noterest, tie_list)
    elif value_in_minims == 81:
        cmnnote_list = dotted_square_note_AND_dotted_whole_note(9, noterest, tie_list)
    # Minims or below
    elif value_in_minims == 1:
        cmnnote = half_note(attribute_dur, noterest)
    elif value_in_minims == Fraction(1,2):
        cmnnote = quarter_note(attribute_dur, noterest)
    elif value_in_minims == Fraction(1,4):
        cmnnote = eighth_note(attribute_dur, noterest)
    elif value_in_minims == Fraction(1,8):
        cmnnote = sixteenth_note(attribute_dur, noterest)
    # Dotted (minims or below)
    elif value_in_minims == Fraction(3,2):
        cmnnote = dotted_half_note(attribute_dur, noterest)
    elif value_in_minims == Fraction(3,4):
        cmnnote = dotted_quarter_note(attribute_dur, noterest)
    elif value_in_minims == Fraction(3,8):
        cmnnote = dotted_eighth_note(attribute_dur, noterest)
    # Else?
    else:
        print("mistake?")
    
    try:
        #print([cmnnote])
        return [cmnnote]
    except:
        #print(cmnnote_list)
        return cmnnote_list


# Main part of the program, it takes the input and output file paths given by the user, 
# and transform each of the notes and rests in the input file to the corresponding cmn values and saves them in the output file
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This program takes a Mensural MEI file as input and converts it into a CMN MEI file.")
    parser.add_argument('input_file', help="Path of the Mensural MEI file to be converted into CMN. This Mensural MEI should encode the precise duration of each note of the mensural piece (i.e., it encodes both the note shape in @dur and the 'perfect'/'imperfect'/'altered' quality of the note in @num and @numbase).")
    parser.add_argument('output_file', help="Path of the output (CMN MEI) file")
    parser.add_argument('count', help="Enter the number of beats per measure")
    parser.add_argument('unit', help="Enter the beat unit")
    args = parser.parse_args()

    # Mensural MEI input file
    mensural_meidoc = documentFromFile(args.input_file).getMeiDocument()
    layers = mensural_meidoc.getElementsByName('layer')
    stavesDef = mensural_meidoc.getElementsByName('staffDef')

    # The MEI document that will save the CMN MEI output file
    outcmn_meidoc = documentFromFile(args.input_file).getMeiDocument()
    cmnStavesDef = outcmn_meidoc.getElementsByName('staffDef')

    # Processing the elements on each staff
    voices_and_measures = {}
    for i, mensural_staffdef in enumerate(stavesDef):
        mensural_voice = layers[i]
        prolatio = int(mensural_staffdef.getAttribute('prolatio').value)
        tempus = int(mensural_staffdef.getAttribute('tempus').value)
        modusminor = int(mensural_staffdef.getAttribute('modusminor').value)
        modusmaior = int(mensural_staffdef.getAttribute('modusmaior').value)

        cmn_staffdef = cmnStavesDef[i]
        # Remove mensuration values in CMN
        cmn_staffdef.removeAttribute('modusmaior')
        cmn_staffdef.removeAttribute('modusminor')
        cmn_staffdef.removeAttribute('tempus')
        cmn_staffdef.removeAttribute('prolatio')
        # Change the notation type (to cmn)
        cmn_staffdef.getAttribute('notationtype').setValue('cmn')
        # And add the meter values in CMN
        cmn_staffdef.addAttribute('meter.count', str(args.count))
        cmn_staffdef.addAttribute('meter.unit', str(args.unit))
        barlength_whole = Fraction(int(args.count)/int(args.unit))
        barlenght_minims = barlength_whole * 2


        # Processing each element in the staff

        # First: retrieve only <note> and <rest> objects
        noterests_voice = []
        for child in mensural_voice.getChildren():
            # Processing each note / rest in the staff
            if child.name == "note" or child.name == "rest":
                noterests_voice.append(child)

        # First note of the voice (index set to 0)
        ind = 0
        note_or_rest = noterests_voice[ind]
        val = value_in_minims(note_or_rest)
        acum = val
        measure_num = 1
        notes_in_measure_per_voice = {}
        notes_in_measure_list = []

        print(len(noterests_voice))
        flag = True
        while flag:
            print("")
            print(note_or_rest)
            print("acumA: " + str(acum)) 
            # Evaluate how many notes go into a measure
            while acum < barlenght_minims:
                print(ind)
                # Add the current note
                notes_in_measure_list.append((note_or_rest, val, False))
                print(str(val), " < ", str(barlenght_minims))
                # Update index, find next note, and update acumulator with this next note
                ind = ind + 1
                try:
                    note_or_rest = noterests_voice[ind]
                except:
                    # No more notes (reached the end of the voice)
                    notes_in_measure_per_voice[measure_num] = notes_in_measure_list
                    flag = False
                    break
                print("next note: " + str(note_or_rest))
                val = value_in_minims(note_or_rest)
                acum = acum + val
                print("ACUM: " + str(acum))

            # If we have reached the barlength
            if acum == barlenght_minims:
                print(ind)
                # Add the note to the list and add the list to the dictionary
                notes_in_measure_list.append((note_or_rest, val, False))
                print(str(val), " = ", str(barlenght_minims))
                notes_in_measure_per_voice[measure_num] = notes_in_measure_list
                # Update (Restart acumulator and the list of notes in the measure, and update the measure_num to the next measure)
                acum = 0
                measure_num = measure_num + 1
                notes_in_measure_list = []
                # And continue with the next note
                ind = ind + 1
                try:
                    note_or_rest = noterests_voice[ind]
                except:
                    flag = False
                val = value_in_minims(note_or_rest)
                acum = acum + val
            
            # If we have gone over the barlength
            elif acum > barlenght_minims:
                print(str(acum), " > ", str(barlenght_minims))
                print(ind)
                # Then divide the note in two parts
                duration_prior_measure_end = acum - val
                val_note1 = barlenght_minims - duration_prior_measure_end
                val_note2 = val - val_note1
                print(val, val_note1, val_note2)
                # Define a new note with (almost) the same attributes as the original but with a different ID.
                # Regarding the Attributes:
                #  1. All attributes of the original note (except for @dur, which is previously removed) 
                #     are retrieved to define the two notes in which the original will be divided into.
                #  2. A new attribute @dur is then added to each individual note.
                #  This is done so that the @dur attribute of each of the note do not point to the same object;
                #  otherwise, it will be impossible to give a different duration value to each of the notes 
                #  in the future (if needed).
                # Regarding the ID:
                #  The new ID will be related to the original note, but will include a subindex
                #  to indicate that it is one of the many divisions of this note.
                xmlid = note_or_rest.getId()
                durval = note_or_rest.getAttribute('dur').value
                note_or_rest.removeAttribute('dur')
                old_attributes = note_or_rest.getAttributes()
                newnote = MeiElement(note_or_rest.name)
                newnote.setId(xmlid + "_" + str(randint(0,100)))
                newnote.setAttributes(old_attributes)
                newnote.addAttribute('dur', durval)
                note_or_rest.addAttribute('dur', durval)
                # Add the note to the list and add the list to the dictionary
                notes_in_measure_list.append((newnote, val_note1, True))
                print(newnote.id)
                notes_in_measure_per_voice[measure_num] = notes_in_measure_list
                # Update
                val = val_note2
                acum = val
                measure_num = measure_num + 1
                notes_in_measure_list = []

        voices_and_measures[i+1] = notes_in_measure_per_voice

    # Section
    outcmn_section = outcmn_meidoc.getElementsByName('section')[0]
    outcmn_section.deleteAllChildren()
    
    # Print the voice_and_measures dictionary that partitions the notes in each voice into measures.
    for item in voices_and_measures.items():
        print(item)

    # In a measure
    for nummeasure in range(1, len(voices_and_measures[1])+1):
        measure = MeiElement('measure')
        measure.addAttribute('n', str(nummeasure))
        outcmn_section.addChild(measure)
        # In a staff of that measure
        for numvoice in range(1, len(voices_and_measures)+1):
            # For each voice in the measure, 
            # Create a staff element (child of the measure)
            cmnStaff = MeiElement('staff')
            cmnStaff.addAttribute('n', str(numvoice))
            measure.addChild(cmnStaff)
            # And a layer element within the staff
            cmnLayer = MeiElement('layer')
            cmnLayer.addAttribute('n', '1')
            cmnStaff.addChild(cmnLayer)
            # Fill this staff with notes
            notes_info = voices_and_measures[numvoice][nummeasure]
            # Go through all the notes of that particular voice in that particular measure,
            # Change its values to modern values, and add the list of <tie> elements at the end of that <staff>
            tie_list_per_voice = []
            for i, triplet_noteinfo in enumerate(notes_info):
                element, val, tied_to_next = triplet_noteinfo[0], triplet_noteinfo[1], triplet_noteinfo[2]
                note_elements = change_noterest_to_cmn(element, val, tie_list_per_voice)
                for note in note_elements:
                    cmnLayer.addChild(note)
                # If the note is tied to the next, create a <tie> element and find the values for @startid (xmlid1) and @endid (xmlid2).
                if tied_to_next:
                    # Find @startid value: the last note of the note_elements list.
                    xmlid1 = note_elements[-1].getId()
                    # Find @endid value: the first (CMN) note in the next measure
                    # (doesn't necessarily coincide with the next mensural note of the next "measure", because this note
                    # could have been divided into other kinds of types--e.g., in the case of a very long note such as
                    # a longa that gets translated into dotted long + dotted square notes).
                    triplet_1stNoteInfo_nextMeasure = voices_and_measures[numvoice][nummeasure+1][0]
                    first_note, val_1stNote = triplet_1stNoteInfo_nextMeasure[0], triplet_1stNoteInfo_nextMeasure[1]
                    first_note_as_list_of_tied_notes = change_noterest_to_cmn(first_note, val_1stNote, [])
                    xmlid2 = first_note_as_list_of_tied_notes[0].getId()
                    # Create element and assign values to the @startid and @endid pair of attributes.
                    tie = MeiElement('tie')
                    tie.addAttribute('startid', '#' + xmlid1)
                    tie.addAttribute('endid', '#' + xmlid2)
                    tie_list_per_voice.append(tie)
                    print("ID: " + str(element.id) + ", TIED TO NEXT NOTE: " + str(xmlid2))
                    print(xmlid1)
            # And fill the measure with the ties
            for tie in tie_list_per_voice:
                measure.addChild(tie)   

    documentToFile(outcmn_meidoc, args.output_file)