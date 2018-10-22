import abjad

import functions

filename = input('csv file to be converted: ')

chords = functions.import_csv(filename)

functions.make_vla_vln_score(chords, midi=True)