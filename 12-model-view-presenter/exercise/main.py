from model import Model
from presenter import Presenter
from view import View


def main() -> None:
    model = Model()
    view = View()
    presenter = Presenter(model, view)
    view.presenter = presenter
    view.master.mainloop()


if __name__ == "__main__":
    main()
