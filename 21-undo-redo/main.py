from delete import Delete
from editor import TextEditor
from insert import Insert


def main() -> None:
    editor = TextEditor()

    insert_1 = Insert(editor, "Hello")
    insert_2 = Insert(editor, " World!")

    editor.execute(insert_1)
    editor.execute(insert_2)

    editor.print_text()

    editor.undo()
    editor.print_text()

    editor.redo()
    editor.print_text()

    delete_1 = Delete(editor, 3)
    editor.execute(delete_1)
    editor.print_text()

    editor.undo()
    editor.print_text()

    editor.redo()
    editor.print_text()

    editor.undo()
    editor.undo()
    editor.undo()
    editor.print_text()


if __name__ == "__main__":
    main()
