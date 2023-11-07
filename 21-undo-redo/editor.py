from dataclasses import dataclass, field

from command import Command


@dataclass
class TextEditor:
    text: str = ""
    undo_stack: list[Command] = field(default_factory=list)
    redo_stack: list[Command] = field(default_factory=list)

    def execute(self, command: Command) -> None:
        command.execute()
        self.undo_stack.append(command)
        self.redo_stack.clear()

    def undo(self) -> None:
        if self.undo_stack:
            command = self.undo_stack.pop()
            command.undo()
            self.redo_stack.append(command)

    def redo(self) -> None:
        if self.redo_stack:
            command = self.redo_stack.pop()
            command.redo()
            self.undo_stack.append(command)

    def print_text(self) -> None:
        print(self.text)
