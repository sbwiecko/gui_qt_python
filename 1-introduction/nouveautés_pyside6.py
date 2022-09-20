from PySide6.QtWidgets import QTableWidget, QPushButton, QVBoxLayout

table = QTableWidget()
# table.setColumnCount(2)
# same as
table.column_count = 2

# setter and getter
from __feature__ import true_property

button = QPushButton("Add")
# button.setEnabled(False)
# same as
button.enabled = False

# snakecase instead of camelcase
from __feature__ import snake_case

layout = QVBoxLayout()
layout.addWidget(table)
# layout.addWidget(button)
# same as
layout.add_widget(button)