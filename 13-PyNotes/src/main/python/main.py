from fbs_runtime.application_context.PySide6 import ApplicationContext

import sys

from package.main_window import MainWindow

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWindow(ctx=appctxt)
    window.resize(550, 600)              # bigger size of the final app
    window.show()
    exit_code = appctxt.app.exec()       # 2. Invoke appctxt.app.exec()
    sys.exit(exit_code)