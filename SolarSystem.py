import sys
import math
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter

class CelestialBody(QGraphicsEllipseItem):
    def __init__(self, radius, color, parent=None):
        super().__init__(parent)
        self.setRect(-radius, -radius, 2 * radius, 2 * radius)
        self.setBrush(color)

class SolarSystem(QGraphicsScene):
    def __init__(self):
        super().__init__()

        self.sun = CelestialBody(30, Qt.yellow)
        self.earth = CelestialBody(15, Qt.blue, self.sun)
        self.moon = CelestialBody(6, Qt.gray, self.earth)

        self.addItem(self.sun)

        self.earth_angle = 0
        self.moon_angle = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_positions)
        self.timer.start(20)

    def update_positions(self):
        self.earth_angle += 0.005
        self.earth.setPos(150 * math.cos(self.earth_angle), 150 * math.sin(self.earth_angle))

        self.moon_angle += 0.02
        self.moon.setPos(40 * math.cos(self.moon_angle), 40 * math.sin(self.moon_angle))

        view.setSceneRect(self.sun.sceneBoundingRect())

        view.setScene(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = QGraphicsView()
    scene = SolarSystem()
    view.setScene(scene)
    view.setRenderHint(QPainter.Antialiasing, True)
    
    view.setFixedSize(1000, 800)
    
    view.setWindowTitle("Solar System Simulation")
    view.show()
    sys.exit(app.exec_())