from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from db_utils import create_med, create_pet
from variables import SGM_DB, TABELA, TABELA_


create_pet(SGM_DB, TABELA_)
create_med(SGM_DB, TABELA)

app = QApplication()
window = MainWindow()

window.show()
app.exec()


