import os
import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QButtonGroup, QRadioButton, QLabel
from PyQt5.QtCore import Qt

class DirectoryCopier(QWidget):
    def __init__(self):
        super().__init__()
        self.src_dir = None
        self.dst_dir = None
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

        btn_src = QPushButton('複製したいフォルダを選択', self)
        btn_src.clicked.connect(self.select_src_directory)
        layout.addWidget(btn_src)

        self.label_src = QLabel('', self)
        layout.addWidget(self.label_src)

        btn_dst = QPushButton('複製先を選択', self)
        btn_dst.clicked.connect(self.select_dst_directory)
        layout.addWidget(btn_dst)

        self.label_dst = QLabel('', self)
        layout.addWidget(self.label_dst)

        btn_ok = QPushButton('OK', self)
        btn_ok.clicked.connect(self.copy_directory)
        layout.addWidget(btn_ok)

    def select_src_directory(self):
        self.src_dir = QFileDialog.getExistingDirectory(self, 'コピー元のディレクトリを選択してください')
        self.label_src.setText('コピー元: ' + self.src_dir)

    def select_dst_directory(self):
        self.dst_dir = QFileDialog.getExistingDirectory(self, 'コピー先のディレクトリを選択してください')
        self.label_dst.setText('コピー先: ' + self.dst_dir)

    def copy_directory(self):
        if self.src_dir and self.dst_dir:
            if self.radiobutton2.isChecked():
                for file_ in os.listdir(self.src_dir):
                    src_file = os.path.join(self.src_dir, file_)
                    if os.path.isfile(src_file):
                        shutil.copy(src_file, self.dst_dir)
            else:
                shutil.copytree(self.src_dir, os.path.join(self.dst_dir, os.path.basename(self.src_dir)))

if __name__ == '__main__':
    app = QApplication([])
    ex = DirectoryCopier()
    ex.show()
    ex.move(app.desktop().screen().rect().center() - ex.rect().center())
    app.exec_()
