
from music21 import *

stream1 = stream.Stream()
octave = '4'


HE_acc = style.TextStyle()
ff = HE_acc.fontFamily
ff.append('HE-maestro')
HE_acc.fontSize = 20

flat_nat7 = pitch.Accidental()
flat_nat7.set('>', allowNonStandardValue=True)
flat_nat7.name = -.3
flat_nat7.alter = -.3
flat_nat7.modifier = '>'



C_nat7 = pitch.Pitch('C')
C_nat7.accidental = flat_nat7


note1 = note.Note(C_nat7)
stream1.append(note1)

note2 = note.Note('C#')
stream1.append(note2)

note3 = note.Note(C_nat7)
stream1.append(note3)

note4 = note.Note('C#')
stream1.append(note4)

print(note1.pitch.accidental.modifier)
print(note2.pitch.accidental.modifier)
print(note3.pitch.accidental.modifier)
print(note4.pitch.accidental.modifier)
#print(pitch.Accidental('flat_nat7').modifier)

#fp = stream1.write('xml', fp='stream1.xml')

#stream1.show()