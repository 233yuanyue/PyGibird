import random
from PySide6.QtCharts import QSplineSeries, QChart, QChartView, QValueAxis, QScatterSeries, QDateTimeAxis
from PySide6.QtCore import QTimer, QEvent, QPointF, QRect, QDateTime
from PySide6.QtGui import QResizeEvent, Qt, QPainter, QFont, QMouseEvent, QPen, QColor, QBrush, QPaintEvent
from PySide6.QtWidgets import QWidget, QFrame, QGraphicsLineItem, QLabel


class TableView(QWidget):
    def __init__(self, parent, title: str, xLabel: str, yLabel: str, width, height, scatter=False, subline=False):
        super(TableView, self).__init__()
        self.parent = parent
        self.id = "".join([title, yLabel])
        self.view = QFrame()
        self.view.setParent(parent)
        self.view.setGeometry(0, 0, width, height)
        self.bLoad = False
        self.splineSeries = QSplineSeries()
        self.chart = QChart()
        self.chartView = QChartView()
        self.axisX = QDateTimeAxis()
        self.axisY = QValueAxis()
        self.timer = QTimer(self)
        self.data: list = []
        self.font = QFont()
        self.hoverPoint = None
        self.showCoor = False
        self.tracking = False
        self.minute = -1
        self.timerStart = False

        if subline:
            self.x_line = QGraphicsLineItem()
            self.y_line = QGraphicsLineItem()
            self.posLabel = QLabel(self.parent)
            # self.posLabel.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
            self.posLabel.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
            self.posLabel.setAttribute(Qt.WA_TranslucentBackground)
            self.posLabel.setFixedSize(227, 21)
            self.posLabel.setStyleSheet("background:none;""padding-left:6px;"
                                        "font: 12pt \"Microsoft YaHei UI\";"
                                        "color:rgb(0, 0, 0);")
            self.setSubline()

        def resizeView(event: QResizeEvent):
            # Geometry is incorrect when the window is loaded for the first time
            if self.bLoad:
                self.resizeView()
            else:
                self.bLoad = True
            event.accept()
        self.parent.resizeEvent = resizeView

        self.InitView(title, xLabel, width, height, yLabel, scatter)
        if scatter:
            self.scatterSeries1 = QScatterSeries()
            self.scatterSeries2 = QScatterSeries()
            self.chart.addSeries(self.scatterSeries1)
            self.chart.addSeries(self.scatterSeries2)
            self.scatterSeries1.attachAxis(self.axisX)
            self.scatterSeries2.attachAxis(self.axisX)
            self.scatterSeries1.attachAxis(self.axisY)
            self.scatterSeries2.attachAxis(self.axisY)
            self.scatterSeries1.setMarkerShape(QScatterSeries.MarkerShapeCircle)
            self.scatterSeries1.setBorderColor(QColor(62, 192, 247))
            self.scatterSeries1.setBrush(QBrush(QColor(62, 192, 247)))
            self.scatterSeries1.setMarkerSize(8)
            self.scatterSeries2.setMarkerShape(QScatterSeries.MarkerShapeCircle)
            self.scatterSeries2.setBorderColor(QColor(255, 255, 255))
            self.scatterSeries2.setBrush(QBrush(QColor(255, 255, 255)))
            self.scatterSeries2.setMarkerSize(3)

    def InitView(self, title, xLabel, width, height, yLabel, scatter):
        self.font.setPixelSize(14)
        self.chart.legend().hide()
        self.chart.setTitle(title)
        # self.chart.setTitleBrush(Qt.white)
        self.chart.addSeries(self.splineSeries)
        self.axisY.setLabelFormat("%g")
        self.axisY.setTitleText(yLabel)
        # self.axisY.setTitleBrush(Qt.white)
        self.axisY.setLabelsFont(self.font)
        self.font.setPixelSize(16)
        self.chart.setTitleFont(self.font)
        self.chart.addAxis(self.axisY, Qt.AlignLeft)
        self.axisY.setRange(0.2, 1.0)
        self.axisY.setTickCount(5)
        self.axisY.setMinorTickCount(4)
        # Set spline for Axis
        self.splineSeries.attachAxis(self.axisY)
        self.axisX.setTitleText(xLabel)
        self.axisX.setTickCount(6)
        # self.axisX.setTitleBrush(Qt.white)
        self.axisX.setLabelsFont(self.font)
        self.chart.addAxis(self.axisX, Qt.AlignBottom)
        self.axisX.setRange(QDateTime(2022, 5, 8, 12, 0, 0), QDateTime(2022, 5, 8, 12, 30, 0))
        self.axisX.setFormat("mm:ss")
        self.splineSeries.attachAxis(self.axisX)
        self.chartView.setChart(self.chart)
        # Set Anti-aliasing
        self.chartView.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)
        self.chartView.setParent(self.view)
        self.chartView.setGeometry(0, 0, width, height)
        # self.chart.setBackgroundVisible(False)
        # self.chart.layout().setContentsMargins(0, 0, 0, 0)
        # self.chart.setMargins(QMargins(0, 0, 0, 0))
        # self.chart.setBackgroundRoundness(0)
        self.timer.start(1000)

        def test():
            self.appendVal(self.splineSeries)
            if scatter:
                self.appendVal(self.scatterSeries1)
                self.appendVal(self.scatterSeries2)
                if self.timerStart:
                    self.data.append(random.randint(15, 95) / 100)
                    while len(self.data) > 30:
                        self.data.pop(0)

        self.timer.timeout.connect(test)

    def resizeView(self, width=0, height=0):
        if height == 0 and width == 0:
            self.view.setGeometry(0, 0, self.parent.width(), self.parent.height())
            self.chartView.setGeometry(0, 0, self.parent.width(), self.parent.height())
        else:
            self.view.setGeometry(0, 0, width, height)
            self.chartView.setGeometry(0, 0, width, height)

    def changePlayStatus(self, bClose=False):
        if bClose:
            self.tracking = False
            self.showCoor = False
            self.timerStart = False
        else:
            self.timerStart = not self.timerStart

    def setSubline(self):
        # Make the lines float at the top level
        # self.x_line.setZValue(100)
        # self.y_line.setZValue(100)
        # Create QPen object
        pen = QPen(QColor(62, 192, 247), 2, Qt.DashLine)
        self.x_line.setPen(pen)
        self.y_line.setPen(pen)

        def mouseMove(e: QMouseEvent):
            # print(self.chart.mapToValue(e.pos()).x(), self.chart.mapToValue(e.pos()).y())
            if self.showCoor:
                curPos = e.globalPos()
                chartPos = self.chart.mapToValue(e.pos())
                datetime: QDateTime = QDateTime.fromMSecsSinceEpoch(chartPos.x())
                minute = datetime.time().minute()
                self.hoverPoint = None
                if (0 <= minute < 30) and (0.2 < chartPos.y() < 1):
                    self.x_line.setLine(e.x(), 0, e.x(), self.chartView.height())
                    mStr = ("0" + str(minute) if minute < 10 else str(minute))
                    second = datetime.time().second()
                    sStr = ("0" + str(second) if second < 10 else str(second))
                    if not self.tracking or self.data == [] or self.timerStart:
                        self.posLabel.setText("当前坐标[{} , {}]".format(
                            "{}:{}".format(mStr, sStr), format(chartPos.y(), ".4f")))
                        self.posLabel.move(curPos.x() + 20, curPos.y())
                        self.y_line.setLine(0, e.y(), self.chartView.width(), e.y())
                    else:
                        minute += 0 if second < 30 else 1
                        posX = QDateTime(2022, 5, 8, 12, minute, 0).toSecsSinceEpoch() * 1e3
                        rightTopPos = self.view.mapToGlobal(QPointF(self.view.width(), 0))
                        if minute != self.minute and minute < len(self.data):
                            y = self.data[minute]
                            mapPos = self.chart.mapToPosition(QPointF(posX, y))
                            self.y_line.setLine(0, mapPos.y(), self.chartView.width(), mapPos.y())
                            self.minute = minute
                            rightTopPos = self.view.mapToGlobal(QPointF(self.view.width(), 0))
                            self.posLabel.setText("追踪坐标[{} , {}]".format(mStr + ":00", format(y, ".4f")))
                            self.hoverPoint = QPointF(posX, y)
                        elif minute > len(self.data):
                            self.posLabel.setText("追踪坐标[{} , {}]".format("{}:{}".format(mStr, sStr), "??????"))
                            self.y_line.setLine(0, 0, 0, 0)
                        self.posLabel.move(rightTopPos.x() - self.posLabel.width(), rightTopPos.y())
                    self.chartView.scene().addItem(self.x_line)
                    self.chartView.scene().addItem(self.y_line)
                    self.posLabel.show()
                    self.x_line.setVisible(True)
                    self.y_line.setVisible(True)
                else:
                    self.y_line.setLine(0, 0, 0, 0)
                    self.x_line.setVisible(False)
                    self.y_line.setVisible(False)
                    self.posLabel.hide()

        self.chartView.mouseMoveEvent = mouseMove

        def mouseEnter(e: QEvent):
            if self.showCoor:
                self.x_line.setVisible(True)
                self.y_line.setVisible(True)
            e.accept()

        self.chartView.enterEvent = mouseEnter

        def mouseLeave(e: QEvent):
            self.x_line.setVisible(False)
            self.y_line.setVisible(False)
            self.minute = -1
            e.accept()

        self.chartView.leaveEvent = mouseLeave

    def appendVal(self, series):
        series.clear()
        for i in range(len(self.data)):
            # ERROR: Python int too large to convert to C long
            series.append(QDateTime(2022, 5, 8, 12, i, 0).toSecsSinceEpoch() * 1e3, self.data[i])

    def changeTrackStatus(self):
        self.tracking = not self.tracking


class Meter(QWidget):
    def __init__(self, parent: QFrame, bgColor: QColor, bgWidth, bgHeight,
                 barPct, scale_begVal, scale_endVal, scale_LSize=100, scale_SSize=10, showPct=0, label=None):
        super(Meter, self).__init__()
        self.label = label
        self.setParent(parent)
        self.parent = parent
        self.bgColor = bgColor
        self.bgWidth = bgWidth
        self.bgHeight = bgHeight
        self.barPct = barPct
        self.scale_begVal = scale_begVal
        self.scale_endVal = scale_endVal
        self.scale_LSize = scale_LSize
        self.scale_SSize = scale_SSize
        self.showPct = showPct
        self.timer = QTimer()
        self.painter = QPainter(self)
        self.initProperty()

    def initProperty(self):
        self.timer.start(1000)
        self.timer.timeout.connect(lambda: self.valueChange(random.randint(2, 98)))

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)
        # Draw background
        self.__drawBg(painter)
        # Draw bar
        self.__drawBar(painter)
        # Draw scale and text
        self.__drawScale(painter)

    def __drawBg(self, painter: QPainter):
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(self.bgColor))
        painter.drawRect((self.parent.width() - self.bgWidth) / 2,
                         (self.parent.height() - self.bgHeight) / 2, self.bgWidth, self.bgHeight)

    def __drawBar(self, painter: QPainter):
        pct = self.showPct
        painter.setPen(Qt.NoPen)
        if 35 <= pct <= 65:
            color = Qt.green
            """do nothing"""
        elif 15 < pct < 35 or 65 < pct < 85:
            color = Qt.yellow
            """warning, you should be careful about the data now"""

        else:
            color = Qt.red
            """error, something wrong must have happened """
        painter.setBrush(QBrush(color))
        offX = self.bgHeight * (1 - self.showPct / 100)
        painter.drawRect((self.parent.width() - self.bgWidth * self.barPct) / 2,
                         (self.parent.height() - self.bgHeight) / 2 + offX,
                         self.bgWidth * self.barPct, self.bgHeight * self.showPct / 100)

    def __drawScale(self, painter: QPainter):
        x = (self.parent.width() + self.bgWidth) / 2 + self.bgWidth * 0.2
        bottomY = (self.parent.height() + self.bgHeight) / 2
        topY = (self.parent.height() - self.bgHeight) / 2
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor(255, 255, 255))
        painter.setPen(pen)
        intervalSize = self.bgHeight / self.scale_SSize / self.scale_LSize
        intervalVal = (self.scale_endVal - self.scale_begVal) / self.scale_LSize
        val = self.scale_begVal
        painter.drawLine(x, topY, x, bottomY + intervalSize * 0.5)
        for i in range(self.scale_LSize * self.scale_SSize + 1):
            if i == 0 or i % self.scale_SSize == 0:
                tmpX = x + 6
                painter.drawText(QRect(tmpX + 5, bottomY - 10, 20, 20), Qt.AlignLeft, format(val, ".1f"))
                val += intervalVal
            else:
                tmpX = x + 3
            painter.drawLine(x, bottomY, tmpX, bottomY)
            bottomY -= intervalSize

    def valueChange(self, currentValPct):
        if self.label is not None:
            self.label.setText(format(self.scale_begVal +
                                      (self.scale_endVal - self.scale_begVal)
                                      * currentValPct / 100, ".4f"))
        self.showPct = currentValPct
        self.update()
