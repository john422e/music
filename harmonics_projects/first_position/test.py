I = ['E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
II = ['A', 'Bb', 'B', 'C', 'C#', 'D', 'Eb', 'E']
III = ['D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A']
IV = ['G', 'G#', 'A' , 'Bb', 'B', 'C', 'C#', 'D']
V = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G']

instrument = [V, IV, III, II, I]



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

            if index == 0:
                new_chord.append(note)
            else:
                # interval matching criteria will go here
                new_chord.append(note)

            if index == last_string:
                # add chord to list
                if len(new_chord) == len(instrument):
                    chords.append(new_chord)
                    print(new_chord) # remove
                else:
                    # reset
                    new_chord = []

                # stop condition
                if string_indexes == max:
                    combining = False

                check_and_increment(first_string, last_string, index,
                                    string_indexes, range)



def check_and_increment(first_string, last_string, index, string_indexes, range):

    if string_indexes[first_string] <= range:
        # check if on last note
        if string_indexes[index] == range and index > 0:
            # reset to 0
            string_indexes[index] = 0
            # increment next string
            index -= 1
            check_and_increment(first_string, last_string, index, string_indexes,
                                range)
        else:
            # increment note
            string_indexes[index] += 1
    else:
        pass


make_chords(instrument, 6)