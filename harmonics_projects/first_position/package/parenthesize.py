import abjad

chord = [-12, -5, 2, 9, 16]

new_chord = abjad.Chord(chord, 1)

new_chord.note_heads[4].is_parenthesized = True

#staff = abjad.Staff(new_chord)

abjad.show(new_chord)