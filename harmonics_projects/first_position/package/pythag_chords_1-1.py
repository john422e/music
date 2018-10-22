import abjad
from string_instrument import StringInstrument
import functions


"""
C3 G3 D4 A4 E5 B5

Seconds = 9/8 (2), 9/4 (14), 9/2 (26)
Fifths = 3/2 (7), 3/1 (19), 6/1 (31)
Octaves = 2/1 (12), 4/1 (24)

"""

def main():

    vla_vln_duo = StringInstrument(-12, 5, 8)  # 7 to exclude doublings (up to 5th) 8 to include

    #intervals = [12, 24, 7, 19, 31] # octaves and fifths
    intervals = [12, 24, 7, 19, 31, 2, 14, 26]  # octaves and fifths and ninths
    #intervals = [12, 24, 19, 31, 2, 14, 26, 5, 17, 29] # octaves, fifths (no P5 though), ninths, fourths

    # include fourths and exclude fifths?

    chords = functions.make_chords(vla_vln_duo.instrument, intervals)
    print("Catalog length:", len(chords))

    # get linear sequence, or run length test on randomized sequences and choose min, max, or median length

    tests = int(input('test total: '))
    sequence = functions.length_test(chords, tests, common_tones=3, repeats_allowed=4)

    #functions.make_score(chords, chords, midi=False)

    #sequence = functions.find_path(chords)
    #print("Sequence Length:", len(sequence))
    #functions.make_score(sequence, chords, midi=True)

    #[-5, -3, 2, 9, 16] [-5, 2, 7, 16, 21] [-12, 2, 2, 16, 21]

    #functions.look_for_chord(chords, [-5, -3, 2, 9, 16])
    #functions.look_for_chord(chords, [-5, 2, 7, 16, 21])
    #functions.look_for_chord(chords, [-12, 2, 2, 16, 21])




main()