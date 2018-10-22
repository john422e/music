import music21 as m21

def make_instrument_notes(open_strings, interval):
    """
    takes the open strings of an instrument (list format) and returns a list of
    all first position chromatic notes
    """
    instrument = []
    for string in open_strings:
        string_notes = make_notes_up_to(string, interval)
        instrument.append(string_notes)
    return instrument

def make_notes_up_to(notestring, interval):
    # returns a list of all notes in range of desired interval above entered pitch (ex. 'C4')
    first_note = m21.note.Note(notestring)
    notes_list = [first_note]
    for note in range(interval):
        new_note = notes_list[-1].transpose(1)
        notes_list.append(new_note)
    return notes_list

def make_chords(instrument):

    # instrument = [[notes, notes], [notes, notes], [D string], [A string], [E string]]
    chord = [0 for string in instrument] # [0, 0, 0, 0, 0]

    chord_list = []

    while True:
        for index, string in enumerate(instrument):
            new_chord = []
            for note in string:
                # C is index 0, G is index 1, D is index 2, A is index 3, E is index 4
                string_index = chord[index] # get current string note
                # copy note object
                note_string = note.nameWithOctave
                new_note = m21.note.Note(note_string)
                # Always add lowest string note
                if index == 0:
                    new_chord.append(new_note)
                    break
                else:
                    for chord_note in new_chord:
                        # 9/8
                        if chord_note.transpose(2) == new_note:
                            new_chord.append(new_note)
                            break
                        # 3/2
                        if chord_note.transpose(7) == new_note:
                            new_chord.append(new_note)
                            break
                        # 2/1
                        elif chord_note.transpose(12) == new_note:
                            new_chord.append(new_note)
                            break
                        # 9/4
                        elif chord_note.transpose(14) == new_note:
                            new_chord.append(new_note)
                            break
                        # 3/1
                        elif chord_note.transpose(19) == new_note:
                            new_chord.append(new_note)
                            break
                        # 4/1
                        elif chord_note.transpose(24) == new_note:
                            new_chord.append(new_note)
                            break
                        # 9/2
                        elif chord_note.transpose(26) == new_note:
                            new_chord.append(new_note)
                            break
                        # 6/1
                        elif chord_note.transpose(31) == new_note:
                            new_chord.append(new_note)
                            break






            if len(new_chord) == len(instrument):
                chord_list.append(new_chord)
            #if index < len(instrument):
            #    print(index)
            #    chord[index] = 0
            #    chord[index - 1] += 1
                #make_chords(instrument)

    print(len(chord_list))


    """
    for string_IV_note in range(len(violin[0])):
        for string_III_note in range(len(violin[1])):
            for string_II_note in range(len(violin[2])):
                for string_I_note in range(len(violin[3])):
                    new_chord = []
                    #chord_string = []
                    for index, string in enumerate(violin):
                        # G is index 0, D is index 1, A is index 2, E is index 3
                        string_index = chord[index]
                        # copy note object
                        note_string = string[string_index].nameWithOctave
                        new_note = m21.note.Note(note_string)
                        # Always add IV note
                        if index == 0:
                            new_chord.append(new_note)
                        else:
                            for chord_note in new_chord:
                                # 9/8
                                if chord_note.transpose(2) == new_note:
                                    new_chord.append(new_note)
                                    break
                                # 3/2
                                if chord_note.transpose(7) == new_note:
                                    new_chord.append(new_note)
                                    break
                                # 2/1
                                elif chord_note.transpose(12) == new_note:
                                    new_chord.append(new_note)
                                    break
                                # 9/4
                                elif chord_note.transpose(14) == new_note:
                                    new_chord.append(new_note)
                                    break
                                # 3/1
                                elif chord_note.transpose(19) == new_note:
                                    new_chord.append(new_note)
                                    break
                                # 4/1
                                elif chord_note.transpose(24) == new_note:
                                    new_chord.append(new_note)
                                    break
                                # 9/2
                                elif chord_note.transpose(26) == new_note:
                                    new_chord.append(new_note)
                                    break
                                # 6/1
                                elif chord_note.transpose(31) == new_note:
                                    new_chord.append(new_note)
                                    break
    
                    if len(new_chord) == 4:
                        chord_list.append(new_chord)
                    # increment string I
                    chord[3] += 1
                # reset string I
                chord[3] = 0
                # increment string II
                chord[2] += 1
            # reset string II
            chord[2] = 0
            # increment string III
            chord[1] += 1
        # reset string III
        chord[1] = 0
        # increment string IV
        chord[0] += 1
    # reset string IV
    chord[0] = 0
    
    print(len(chord_list))
    """

def main():

    stream1 = m21.stream.Stream()

    vla_vln_strings = ['C3', 'G3', 'D4', 'A4', 'E5']

    vla_vln_duo = make_instrument_notes(vla_vln_strings, 7)

    for string in vla_vln_duo:
        print(string[0])

    make_chords(vla_vln_duo)

    #small_chords = chord_list[:]

    # add all notes to stream
    #for chord in chord_list:
    #    for note in chord:
    #        stream1.append(note)

    #stream1.show()
    #print('done')

main()