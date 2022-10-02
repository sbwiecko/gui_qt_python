from fbs_runtime.application_context.PySide6 import ApplicationContext, cached_property
from PySide6 import QtGui

import sys

from package.main_window import MainWindow


class AppContext(ApplicationContext):
    def run(self):
        main_window = MainWindow(ctx=self)
        main_window.resize(1920 / 4, 1200 / 2)
        main_window.show()
        return self.app.exec()

    # speed process by keeping the images of the icons in the cache
    @cached_property
    def img_checked(self):
        return QtGui.QIcon(self.get_resource("images/checked.png"))

    @cached_property
    def img_unchecked(self):
        return QtGui.QIcon(self.get_resource("images/unchecked.png"))


if __name__ == '__main__':
    appctxt = AppContext()
    sys.exit(appctxt.run())
