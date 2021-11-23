from typing import Optional


class Note(object):

    def __init__(
            self,
            name: Optional[str] = None,
            # freq: Optional[str] = None,
            octave: Optional[str] = None

    ):
        self.name = name
        # self.freq = freq
        self.octave = octave
