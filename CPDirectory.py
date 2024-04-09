import os
import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QButtonGroup, QRadioButton

class DirectoryCopier(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ディレクトリを複製')
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.radiobutton1 = QRadioButton('フォルダ全体を複製', self)
        self.radiobutton2 = QRadioButton('フォルダの中のファイルだけを複製', self)
        self.radiobutton1.setChecked(True)

        self.buttongroup = QButtonGroup(self)
        self.buttongroup.addButton(self.radiobutton1)
        self.buttongroup.addButton(self.radiobutton2)

        layout.addWidget(self.radiobutton1)
        layout.addWidget(self.radiobutton2)

        btn = QPushButton('ディレクトリを複製', self)
        btn.clicked.connect(self.copy_directory)
        layout.addWidget(btn)

    def copy_directory(self):
        src_dir = QFileDialog.getExistingDirectory(self, 'コピー元のディレクトリを選択してください')
        dst_dir = QFileDialog.getExistingDirectory(self, 'コピー先のディレクトリを選択してください')
        if self.radiobutton2.isChecked():
            for file_ in os.listdir(src_dir):
                src_file = os.path.join(src_dir, file_)
                if os.path.isfile(src_file):
                    shutil.copy(src_file, dst_dir)
        else:
            shutil.copytree(src_dir, os.path.join(dst_dir, os.path.basename(src_dir)))

if __name__ == '__main__':
    app = QApplication([])
    ex = DirectoryCopier()
    ex.show()
    app.exec_()
