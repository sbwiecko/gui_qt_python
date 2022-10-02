from fbs_runtime.application_context.PySide6 import ApplicationContext

import sys

from package.main_window import MainWindow

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWindow(ctx=appctxt)
    window.resize(1920 / 2, 1200 / 2)
    window.show()
    exit_code = appctxt.app.exec()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)