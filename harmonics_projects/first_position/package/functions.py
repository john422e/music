import abjad, random, csv, ast

def make_chords(instrument, interval_list): # intervals = 2, 7, 12, 14, 19, 24, 26, 31
    combining = True
    note_range = len(instrument[0]) - 1

    # Master list of chords
    chords = []

    # Current index for each string in instrument (starts at 0)
    string_indexes = [0 for string in instrument]
    max = [note_range for string in instrument]

    first_string = 0
    last_string = len(instrument) - 1

    while combining:

        new_chord = []

        for index, string in enumerate(instrument):

            note = instrument[index][(string_indexes[index])]

            if index == 0:
                new_chord.append(note)
            else:
                # interval matching criteria
                for chord_note in new_chord: # make these positive for ascending strings, negative for descending
                    interval = note - chord_note
                    if interval in interval_list:
                        new_chord.append(note)
                        break

        if index == last_string:
            # add chord to list
            if len(new_chord) == len(instrument):
                chords.append(new_chord)
                #print(new_chord)  # remove
            else:
                # reset
                new_chord = []

            # stop condition
            if string_indexes == max:
                combining = False

            check_and_increment(first_string, last_string, index,
                                string_indexes, note_range)

    return chords

def check_and_increment(first_string, last_string, index, string_indexes,
                        note_range):
    if string_indexes[first_string] <= note_range:
        # check if on last note
        if string_indexes[index] == note_range and index > 0:
            # reset to 0
            string_indexes[index] = 0
            # increment next string
            index -= 1
            check_and_increment(first_string, last_string, index,
                                string_indexes, note_range)
        else:
            # increment note
            string_indexes[index] += 1

def sort_chord_into_voices(chord_list, repeats_allowed):
    # sort chords into voices
    past_chords = [[], [], [], [], []]
    for index in range(1, repeats_allowed + 1):
        neg_index = int(index / -1)
        past_chord = chord_list[neg_index]
        for index, note in enumerate(past_chord):
            past_chords[index].append(note)
    return past_chords

def check_voices_for_repetition(past_chords):
    # check each voice/index for maximum repeated notes allowed
    no_repeats = True
    for voice in past_chords:
        no_repeats = True
        for voice in past_chords:
            first_note = voice[0]
            for note in voice:
                if note != first_note:
                    # then we're good and go to next voice
                    repeats = False
                    break
                else:
                    # then keep checking
                    repeats = True
            if repeats == True:
                # then this chord is no good
                no_repeats = False
                break
        if no_repeats:
            return True
        else:
            return False

def find_path(chords, common_tones=4, repeats_allowed=None, seed=0, path='linear'):
    # finds chord sequences where each chord has 4 notes in common
    non_common_tones = len(chords[0]) - common_tones

    # copy chord list
    all_chords = chords[:]

    chord_list = [all_chords[seed]]
    del all_chords[seed]

    sequencing = True

    while sequencing:

        if path == 'linear':

            for chord in all_chords:
                # check against last chord in sequence
                last_chord = chord_list[-1]
                # now check to see if next chord matches
                counter = 0
                for note in last_chord:
                    if note not in chord:
                        counter += 1
                if counter == non_common_tones:
                    if repeats_allowed:
                        # if there is a max repeats condition
                        if len(chord_list) >= repeats_allowed:
                            # sort chords into voices
                            past_chords = sort_chord_into_voices(chord_list, repeats_allowed)
                            no_repeats = check_voices_for_repetition(past_chords)
                            if no_repeats == True:
                                # then chord passed repetition test, add it and move on
                                chord_list.append(chord)
                                all_chords.remove(chord)
                                break
                            else:
                                pass
                        else:
                            # only happens when list is too short
                            chord_list.append(chord)
                            all_chords.remove(chord)
                    else:
                        # happens when no repetition minimum is specified
                        chord_list.append(chord)
                        all_chords.remove(chord)
                # stop after last chord
                if chord == all_chords[-1]:
                    sequencing = False

        elif path == 'random':

            not_it = []

            while all_chords:
                # pick a random chord
                chord = random.choice(all_chords)
                # check against last chord in sequence
                last_chord = chord_list[-1]
                # now check to see if next chord matches--must have x common tones
                counter = 0
                for note in last_chord:
                    if note not in chord:
                        counter += 1
                if counter == non_common_tones:
                    # it's a match!
                    if repeats_allowed: # if there is a max repeats condition
                        if len(chord_list) >= repeats_allowed:
                            # sort chords into voices
                            past_chords = sort_chord_into_voices(chord_list, repeats_allowed)
                            # now check each voice/index for maximum repeated notes allowed
                            no_repeats = check_voices_for_repetition(past_chords)
                            if no_repeats == True:
                                # then chord passed repetition test, add it and move on
                                chord_list.append(chord)
                                all_chords.remove(chord)
                                for checked_chords in not_it:
                                    # add all the non-matches back to catalog
                                    all_chords.append(checked_chords)
                                    # empty not_it
                                    not_it = []
                            else:
                                # remove non-match temporarily
                                not_it.append(chord)
                                all_chords.remove(chord)
                        else:
                            # only happens when list is too short
                            chord_list.append(chord)
                            all_chords.remove(chord)
                            for checked_chords in not_it:
                                # add all the non-matches back to catalog
                                all_chords.append(checked_chords)
                                # empty not_it
                                not_it = []
                    else:
                        # happens when no repetition minimum is specified
                        chord_list.append(chord)
                        # remove from catalog list
                        all_chords.remove(chord)
                        for checked_chords in not_it:
                            # add all the non-matches back to catalog
                            all_chords.append(checked_chords)
                            # empty not_it
                            not_it = []
                else:
                    # remove non-match temporarily
                    not_it.append(chord)
                    all_chords.remove(chord)

                if len(all_chords) == 0:
                    sequencing = False

    return chord_list


def make_one_part(chord_list, parenthesis=None, chord_style="block"):
    """
    :param chord_list: list of chords
    :param parenthesis: single index (integer) of note to be parenthesized
    :param chord_style: 'block' or 'arpeggiated'
    :return: abjad.Staff(chords)
    """
    notes = []

    if chord_style == 'block':
        for chord in chord_list:
            new_chord = abjad.Chord(chord, 1)
            if parenthesis >= 0:
                new_chord.note_heads[parenthesis].is_parenthesized = True
            notes.append(new_chord)

        time_signature = abjad.indicatortools.TimeSignature((4, 4))

    elif chord_style == 'arpeggiated':
        for pitch in chord:
            note = abjad.Note(pitch, 0.25)
            notes.append(note)

        time_signature = abjad.indicatortools.TimeSignature((5, 4))

    staff = abjad.Staff(notes)

    abjad.attach(time_signature, staff)

    return staff

def make_score(sequence, chords, midi=False):
    print("Length of sequence:", len(sequence), "of", len(chords))
    staff = make_one_part(sequence)
    abjad.show(staff)
    if midi:
        abjad.play(staff)

    # make csv
    filename = 'chords.csv'
    with open(filename, 'w') as csvfile:
        chord_writer = csv.writer(csvfile, delimiter=',')
        for chord in sequence:
            chord_writer.writerow([chord])

def make_vla_vln_score(chords, midi=False):
    vla_chords = []
    vln_chords = []

    for chord in chords:
        vla_chord = chord[:4]
        vln_chord = chord[1:]
        vla_chords.append(vla_chord)
        vln_chords.append(vln_chord)

    vla_staff = make_one_part(vla_chords, parenthesis=3)
    clef = abjad.Clef(name='alto')
    abjad.attach(clef, vla_staff[0])
    viola = abjad.instrumenttools.Viola()
    abjad.attach(viola, vla_staff)
    #vla_staff.name = 'Viola'
    vln_staff = make_one_part(vln_chords, parenthesis=0)
    violin = abjad.instrumenttools.Violin()
    abjad.attach(violin, vln_staff)
    #vln_staff.name = 'Violin'
    score = abjad.Score([vln_staff, vla_staff])
    score.add_final_bar_line()

    lilypond_file = abjad.LilyPondFile.new(score,
                                           default_paper_size=('letter', 'landscape'),
                                           global_staff_size=20)

    #postscript = abjad.Postscript()

    lilypond_file.header_block.title = abjad.Markup("tuning no. 4:")

    lilypond_file.header_block.title.setfont("Arial")
    lilypond_file.header_block.subtitle = abjad.Markup('Pythagorean chains')
    lilypond_file.header_block.composer = abjad.Markup('John Eagle')
    lilypond_file.header_block.tagline = " "
    lilypond_file.paper_block.top_margin = 15
    lilypond_file.paper_block.left_margin = 20

    abjad.show(lilypond_file)
    if midi:
        abjad.play(score)


def look_for_duplicates(chord_list, query_chord):

    duplicates = []

    for index, chord in enumerate(chord_list):
        if chord == query_chord:
            duplicates.append(index)
    if len(duplicates) > 1:
        return duplicates
    else:
        return None

def length_test(chords, test_size, common_tones=4, repeats_allowed=None):

    sequences = []

    # longest so far is 391 of 608 chord group (octaves, fifths, and ninths)
    # longest so far is 61 of 124 chord group (octaves and fifths)
    for i in range(test_size):  # number of sequences to test
        sequence = find_path(chords, common_tones, repeats_allowed, path='random')
        print(i, len(sequence))
        sequences.append(sequence)

    selecting = True

    while selecting:

        selection = int(input("1. longest 2. shortest 3. median 4. quit "))
        if selection == 4:
            selecting = False
        elif selection == 1:
            sequence = max(sequences, key=len)
            print("Sequence Length:", len(sequence))

            # check for duplicates
            dup_list = []
            for chord in sequence:
                duplicates = look_for_duplicates(sequence, chord)
                if duplicates:
                    dup_list.append(duplicates)
            if dup_list:
                print(dup_list)
            else:
                print('no duplicates')

            export = input('export? y/n ')
            if export == 'y':
                make_score(sequence, chords, midi=True)
        elif selection == 2:
            sequence = min(sequences, key=len)
            print("Sequence Length:", len(sequence))
            export = input('export? y/n ')
            if export == 'y':
                make_score(sequence, chords, midi=True)
        elif selection == 3:
            median = int((len(sequences) / 2)) - 1
            sequences.sort()
            sequence = sequences[median]
            print("Sequence Length:", len(sequence))
            export = input('export? y/n ')
            if export == 'y':
                make_score(sequence, chords, midi=True)

def import_csv(filename): # 0217.csv
    # imports csv file into list
    chords = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for chord in reader:
            chords.append(ast.literal_eval(chord[0]))
    return chords
