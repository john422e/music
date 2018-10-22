import music21 as m21

def make_instrument_notes(open_strings):
    """
    takes the open strings of an instrument (list format) and returns a list of
    all first position chromatic notes
    """
    instrument = []
    for string in open_strings:
        string_notes = make_notes_up_P5(string)
        instrument.append(string_notes)
    return instrument

def make_notes_up_P5(notestring):
    # returns a list of all notes in range of a P5 above entered pitch (ex. 'C4')
    first_note = m21.note.Note(notestring)
    notes_list = [first_note]
    for note in range(7):
        new_note = notes_list[-1].transpose(1)
        notes_list.append(new_note)
    return notes_list

stream1 = m21.stream.Stream()

vln_open_strings = ['G3', 'D4', 'A4', 'E5']

violin = make_instrument_notes(vln_open_strings)

chord = [0, 0, 0, 0] # [IV, III, II, I]

chord_list = []
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

#small_chords = chord_list[:]

# add all notes to stream
for chord in chord_list:
    for note in chord:
        stream1.append(note)

stream1.show()
print('done')