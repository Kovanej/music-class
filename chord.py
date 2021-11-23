
from typing import Optional, List

from note import Note


class Scale(object):

    def __init__(
            self,
            base_note: Note
    ):
        self.base_note = base_note
        self.sequence_of_notes = self._get_the_sequence_of_notes


class ScaleType(object):

    def __init__(
            self,
            type_name: str
    ):
        self.type_name = type_name

