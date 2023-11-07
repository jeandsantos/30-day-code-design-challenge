from dataclasses import dataclass

from command import Command
from editor import TextEditor


@dataclass
class Insert(Command):
    editor: TextEditor
    new_text: str

    def execute(self) -> None:
        self.editor.text += self.new_text
        print(f"Inserted {len(self.new_text)} character(s): '{self.new_text}'")

    def undo(self) -> None:
        self.editor.text = self.editor.text[: -len(self.new_text)]
        print(f"Undid insertion of {len(self.new_text)} character(s): '{self.new_text}'")

    def redo(self) -> None:
        self.editor.text += self.new_text
        print(f"Redid insertion of {len(self.new_text)} character(s): '{self.new_text}'")
