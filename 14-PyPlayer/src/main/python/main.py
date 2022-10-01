from fbs_runtime.application_context.PySide6 import ApplicationContext

import sys

from package.main_window import MainWindow

if __name__ == '__main__':
    appctxt = ApplicationContext()  # 1. Instantiate ApplicationContext
    window = MainWindow()
    available_geometry = window.screen().availableGeometry()
    # see https://doc.qt.io/qtforpython/examples/example_multimedia__player.html
    window.resize(available_geometry.width() / 3,
                  available_geometry.height()/ 2)
    window.show()
    exit_code = appctxt.app.exec()  # 2. Invoke appctxt.app.exec()
    sys.exit(exit_code)
