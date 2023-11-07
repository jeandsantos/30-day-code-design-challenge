from dataclasses import dataclass

from command import Command
from editor import TextEditor


@dataclass
class Delete(Command):
    editor: TextEditor
    n_characters: int
    text_removed: str = ""

    def execute(self) -> None:
        self.text_removed = self.editor.text[-self.n_characters :]
        self.editor.text = self.editor.text[: -self.n_characters]
        print(f"Removed {self.n_characters} character(s): '{self.text_removed}'")

    def undo(self) -> None:
        self.editor.text += self.text_removed
        print(f"Undid deletion by re-inserting {len(self.text_removed)} removed character(s): '{self.text_removed}'")

    def redo(self) -> None:
        self.text_removed = self.editor.text[-self.n_characters :]
        self.editor.text = self.editor.text[: -self.n_characters]
        print(f"Redid deletion of {self.n_characters} character(s): '{self.text_removed}'")
