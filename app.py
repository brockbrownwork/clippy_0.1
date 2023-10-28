import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QApplication, QWidget
from random import randint
from glob import glob

class ImageCycleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.loading_animation = randint(1,2)
        # self.image_paths = [f"render\\loading_animation_{self.loading_animation}\\{i:04d}.png" for i in range(1, 81)]
        self.image_paths = [f"render\\loading_animation_1\\{i:04d}.png" for i in range(1, 81)]
        self.current_image_index = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.nextImage)
        self.timer.start(int(1000 / 25))  # 25 fps

        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Image Cycle')
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.show()

    def nextImage(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        print(self.current_image_index)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap(self.image_paths[self.current_image_index])
        painter.drawPixmap(self.rect(), pixmap)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageCycleWidget()
    sys.exit(app.exec_())
