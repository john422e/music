import abjad, functions
from string_instrument import StringInstrument

vla_vln_duo = StringInstrument(-12, 5, 8, offset=4)

octaves = [12, 24]
fifths = [7, 19, 31]
ninths = [2, 14, 26]
thirds = [3, 4, 8, 9, 15, 16, 21, 22, 27, 28, 33, 34]

intervals = [12, 24, 7, 19, 31, 2, 14, 26, 3]  # octaves and fifths and ninths

notes = []
for string in vla_vln_duo.instrument:
    for pitch in string:
        note = abjad.Note(pitch, 0.25)
        notes.append(note)

time_signature = abjad.indicatortools.TimeSignature((9, 4))

staff = abjad.Staff(notes)

abjad.attach(time_signature, staff)

#abjad.show(staff)

file_path = "/Users/johneagle/PycharmProjects/harmonics_projects/first_position/package/output/"
ly = file_path + "test1.ly"
pdf = file_path + "test.pdf"

abjad.IOManager.save_last_ly_as(ly)
abjad.IOManager.run_lilypond(ly)