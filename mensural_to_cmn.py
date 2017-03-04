from fractions import *
import argparse

from pymei import *


# Function: changes the value of a mensural note into a cmn note
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

    if value_in_minims == 2:
        # whole note
        attribute_dur.setValue('1')
        cmn_voice.addChild(noterest)

    elif value_in_minims == 3:
        # dotted whole note
        attribute_dur.setValue('1')
        noterest.addAttribute('dots', '1')
        cmn_voice.addChild(noterest)

    elif value_in_minims == 4:
        # square note
        attribute_dur.setValue('breve')
        cmn_voice.addChild(noterest)

    elif value_in_minims == 6:
        # dotted square note
        attribute_dur.setValue('breve')
        noterest.addAttribute('dots', '1')
        cmn_voice.addChild(noterest)

    elif value_in_minims == 9:
        # dotted square note + dotted whole note
        # Since there is more than one note, we need to create new note elements with the same value for the 
        # attributes related to pitch (@pname and @oct), but with distinct values for the attributes related
        # to duration (@dur and @dots). The xml:id for these notes will be the same as the xml:id of the 
        # original mensural note they represent, but with an added number (indicating the number of the note
        # in the collection of notes tied together to sum up to the number of minims the mensural note has).
        
        # Getting the xml:id and attributes from the mensural note
        xmlid = noterest.getId()
        noterest.removeAttribute('dur')
        old_attributes = noterest.getAttributes()
        # First Note: dotted square note
        newnote = MeiElement('note')
        newnote.setId(xmlid + "_1")
        newnote.setAttributes(old_attributes)
        newnote.addAttribute('dur', 'breve')
        newnote.addAttribute('dots', '1')
        cmn_voice.addChild(newnote)
        # Second Note: dotted whole note
        newnote = MeiElement('note')
        newnote.setId(xmlid + "_2")
        newnote.setAttributes(old_attributes)
        newnote.addAttribute('dur', '1')
        newnote.addAttribute('dots', '1')
        cmn_voice.addChild(newnote)
        
    elif value_in_minims == 8:
        # long note
        attribute_dur.setValue('long')
        cmn_voice.addChild(noterest)

    elif value_in_minims == 12:
        # dotted long note
        attribute_dur.setValue('long')
        noterest.addAttribute('dots', '1')
        cmn_voice.addChild(noterest)

    elif value_in_minims == 18:
        print(18)
        # Two cases based on the default value of the breve (either of 9 or 6 minims -the case of 4 is not pertinent-)
        if prolatio * tempus == 6:
            print(6)
            # dotted long note + dotted square note
            # Getting the xml:id and attributes from the mensural note
            xmlid = noterest.getId()
            noterest.removeAttribute('dur')
            old_attributes = noterest.getAttributes()
            # First Note: dotted long note
            newnote = MeiElement('note')
            newnote.setId(xmlid + "_1")
            newnote.setAttributes(old_attributes)
            newnote.addAttribute('dur','long')
            newnote.addAttribute('dots','1')
            cmn_voice.addChild(newnote)
            print(newnote)
            # Second Note: dotted square note
            newnote = MeiElement('note')
            newnote.setId(xmlid + "_2")
            newnote.setAttributes(old_attributes)
            newnote.addAttribute('dur','breve')
            newnote.addAttribute('dots','1')
            cmn_voice.addChild(newnote)

        elif prolatio * tempus == 9:
            # 2 x (dotted square note + dotted whole note)
            # Getting the xml:id and attributes from the mensural note
            xmlid = noterest.getId()
            noterest.removeAttribute('dur')
            old_attributes = noterest.getAttributes()
            # Encoding the two times the two (dotted square and dotted whole) notes
            for i in [1,2]:
                # First Note: dotted square note
                newnote = MeiElement('note')
                newnote.setId(xmlid + "_" + str(2*i-1))
                newnote.setAttributes(old_attributes)
                newnote.addAttribute('dur','breve')
                newnote.addAttribute('dots','1')
                cmn_voice.addChild(newnote)
                # Second Note: dotted whole note
                newnote = MeiElement('note')
                newnote.setId(xmlid + "_" + str(2*i))
                newnote.setAttributes(old_attributes)
                newnote.addAttribute('dur','1')
                newnote.addAttribute('dots','1')
                cmn_voice.addChild(newnote)
        else:
            # should not happen
            pass

    elif value_in_minims == 27:
        # 3 x (dotted square note + dotted whole note)
        # Since there is more than one note, we need to create new note elements with the same value for the 
        # attributes related to pitch (@pname and @oct), but with distinct values for the attributes related
        # to duration (@dur and @dots). The xml:id for these notes will be the same as the xml:id of the 
        # original mensural note they represent, but with an added number (indicating the number of the note
        # in the collection of notes tied together to sum up to the number of minims the mensural note has).
        
        # Getting the xml:id and attributes from the mensural note
        xmlid = noterest.getId()
        noterest.removeAttribute('dur')
        old_attributes = noterest.getAttributes()
        # Encoding the three times the two (dotted square and dotted whole) notes
        for i in [1,2,3]:
            # First Note: dotted square note
            newnote = MeiElement('note')
            newnote.setId(xmlid + "_" + str(2*i-1))
            newnote.setAttributes(old_attributes)
            newnote.addAttribute('dur','breve')
            newnote.addAttribute('dots','1')
            cmn_voice.addChild(newnote)
            # Second Note: dotted whole note
            newnote = MeiElement('note')
            newnote.setId(xmlid + "_" + str(2*i))
            newnote.setAttributes(old_attributes)
            newnote.addAttribute('dur','1')
            newnote.addAttribute('dots','1')
            cmn_voice.addChild(newnote)

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