"""
C3 G3 D4 A4 E5 B5

Seconds = 9/8 (2), 9/4 (14), 9/2 (26)
Fifths = 3/2 (7), 3/1 (19), 6/1 (31)
Octaves = 2/1 (12), 4/1 (24)

"""


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

def make_chords(instrument, range):
    combining = True

    # Master list of chords
    chords = []

    # Current index for each string in instrument (starts at 0)
    string_indexes = [0 for string in instrument]
    max = [range for string in instrument]

    first_string = 0
    last_string = len(instrument) - 1

    while combining:

        new_chord = []

        for index, string in enumerate(instrument):

            note = instrument[index][(string_indexes[index])]

            # copy note object
            note_string = note.nameWithOctave
            new_note = m21.note.Note(note_string)

            if index == 0:
                new_chord.append(new_note)
            else:
                # interval matching criteria


                for chord_note in new_chord: # make these positive for ascending strings, negative for descending
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

        if index == last_string:
            # add chord to list
            if len(new_chord) == len(instrument):
                chords.append(new_chord)
                print(new_chord)  # remove
            else:
                # reset
                new_chord = []

            # stop condition
            if string_indexes == max:
                combining = False

            check_and_increment(first_string, last_string, index,
                                string_indexes, range)

    return chords

def check_and_increment(first_string, last_string, index, string_indexes,
                        range):
    if string_indexes[first_string] <= range:
        # check if on last note
        if string_indexes[index] == range and index > 0:
            # reset to 0
            string_indexes[index] = 0
            # increment next string
            index -= 1
            check_and_increment(first_string, last_string, index,
                                string_indexes, range)
        else:
            # increment note
            string_indexes[index] += 1

def make_one_part(chord_list, strings):
    # make single stream
    single_part = m21.stream.Stream()
    # make time sig based on number of strings
    time_sig_num = str(len(strings))
    time_sig_den = '4'

    time_sig_string = time_sig_num + '/' + time_sig_den

    time_sig = m21.meter.TimeSignature(time_sig_string)
    single_part.append(time_sig)
    # add all notes to stream
    for chord in chord_list:
        for note in chord:
            single_part.append(note)

    return single_part

def make_two_parts(chord_list, output_format): # 'block-chords' or 'arpeggio'
    # make two part streams and one score stream
    part1 = m21.stream.Part()
    part1.id = 'viola'
    part2 = m21.stream.Part()
    part2.id = 'violin'
    score = m21.stream.Score()

    # divide chord into two and add to part streams
    for ref_chord in chord_list:
        part1_chord = m21.chord.Chord(ref_chord[:4]) # viola
        part2_chord = m21.chord.Chord(ref_chord[1:]) # violin

        if output_format == 'block-chords':
            part1_chord.duration.type = 'whole'
            part2_chord.duration.type = 'whole'
            part1.append(part1_chord)
            part2.append(part2_chord)

        elif output_format == 'arpeggio':
            for note in part1_chord:
                part1.append(note)
            for note in part2_chord:
                # copy note object
                note_string = note.nameWithOctave
                new_note = m21.note.Note(note_string)
                part2.append(new_note)

    # add part streams to score stream, 2 goes first for ascending, 1 for descending

    score.insert(0, part2)
    score.insert(0, part1)

    score.show()

def divide_chords(chords):
    vla, vln = [], []
    for chord in chords:
        vla_chord = chord[:4]
        vln_chord = chord[1:]
        if vla_chord not in vla:
            vla.append(vla_chord)
        if vln_chord not in vln:
            vln.append(vln_chord)
    return vla, vln

def filter_chords(vla, vln):
    # incomplete
    new_vla = []
    new_vln = []
    for vla_chord in vla:
        temp_vln_chords = []
        for vln_chord in vln:
            if vla_chord[1:] == vln_chord[:3]:
                temp_vln_chords.append(vln_chord)
        beats = len(temp_vln_chords)

def find_paths(chords):
    # finds chord sequences where each chord has 4 notes in common
    chord_list = [chords[0]]
    while parsing:
        for index, chord in enumerate(chord_list):
            if index == 0:
                continue
            else:
                # check against last chord in sequence
                chord_1 = chord_list[-1]
                # now check to see if next chord matches



def main():

    vla_vln_strings = ['C3', 'G3', 'D4', 'A4', 'E5']
    #vla_vln_strings = ['E5', 'A4', 'D4', 'G3', 'C3'] # reverse order - does this generate same chords?

    vla_vln_duo = make_instrument_notes(vla_vln_strings, 7)

    chords = make_chords(vla_vln_duo, 7) # 7

    #vla, vln = divide_chords(chords)

    #print(len(vla), len(vln))

    #find_paths(chords)
    score = make_one_part(chords, vla_vln_strings)
    score.show()
    #make_two_parts(chords, 'block-chords')

    #filter_chords(vla, vln)




main()