class StringInstrument():
    """
    returns a data set containing chromatic pitch integers (C4=0) which can be
    converted to abjad notes [[0,1...], [7,8...], [14,15...], [21,22...]...]
    """

    def __init__(self, ref_pitch, total_strings, pitch_range, offset=0,
                 direction='ascending'):
        self.ref_pitch = ref_pitch
        self.total_strings = total_strings
        self.pitch_range = pitch_range
        self.direction = direction

        # store's the instruments pitch integers
        self.instrument = []
        open_string = self.ref_pitch

        # add all the pitch integers
        for string in range(self.total_strings):
            # get this string's pitch
            pitch = open_string
            # add open string
            string_pitches = [pitch]
            # add offset
            pitch += offset
            # add all the notes for this string
            for i in range(self.pitch_range):
                string_pitches.append(pitch)
                pitch += 1
            self.instrument.append(string_pitches)
            # to next string
            open_string += 7

