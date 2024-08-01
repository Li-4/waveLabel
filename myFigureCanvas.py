# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtWidgets import QVBoxLayout, QMessageBox

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure as mplfig
from matplotlib.backends.backend_qtagg import (FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar)


class QmyFigureCanvas(QtWidgets.QWidget):
    # 自定义信号
    x1_update_signal = QtCore.Signal(int)
    x2_update_signal = QtCore.Signal(int)
    def __init__(self, parent=None, toolbarVisible=True, showHint=True):
        super().__init__(parent)
        self.figure = mplfig.Figure()           # 公共属性 figure
        self.figCanvas = FigureCanvasQTAgg(self.figure)  # 创建 FigureCanvasQTAgg 对象
        self.naviBar = NavigationToolbar(self.figCanvas, self)   # 公共属性 naviBar
        self.__changeActionLanguage()           # 工具栏改为汉语

        actList=self.naviBar.actions()          # 关联的 Action 列表
        count = len(actList)                    # Action 的个数
        self.__lastActionHint=actList[count-1]  # 最后的坐标提示
        self.__showHint=showHint                # 是否在工具栏上显示坐标提示
        self.__lastActionHint.setVisible(self.__showHint)
        self.__showToolbar=toolbarVisible       # 是否显示工具栏
        self.naviBar.setVisible(self.__showToolbar)

        layout = QVBoxLayout(self)
        layout.addWidget(self.naviBar)          # 添加工具栏
        layout.addWidget(self.figCanvas)             # 添加 FigureCanvas 对象
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.x_data = None
        self.y_data = None
        self.vline1 = None
        self.vline2 = None
        self.text1 = None
        self.text2 = None
        self.press = None
        self.initial_x = [10, 30]
        self.selected_lines = {0: self.initial_x[0], 1: self.initial_x[1]}

        self.__cid = self.figCanvas.mpl_connect("scroll_event", self.do_scrollZoom)  # 支持鼠标滚轮缩放
        self.__cidpress = self.figCanvas.mpl_connect('button_press_event', self.on_press)
        self.__cidrelease = self.figCanvas.mpl_connect('button_release_event', self.on_release)
        self.__cidmotion = self.figCanvas.mpl_connect('motion_notify_event', self.on_motion)


## ========== 公共函数接口 ==========
    def __changeActionLanguage(self):
        """汉化工具栏"""
        actList = self.naviBar.actions()        # 关联的 Action 列表
        actList[0].setText("复位")      # Home
        actList[0].setToolTip("复位到原始图像") # Reset original view
        actList[1].setText("回退")      # Back
        actList[1].setToolTip("回退到前一视图") # Back to previous view
        actList[2].setText("前进")      # Forward
        actList[2].setToolTip("前进到下一视图") # Forward to next view
        actList[4].setText("平动")      # Pan
        actList[4].setToolTip("左键平移坐标轴, 右键缩放坐标轴")
        actList[5].setText("缩放")      # Zoom
        actList[5].setToolTip("框选矩形框缩放") # Zoom to rectangle
        actList[6].setText("子图")      # Subplots
        actList[6].setToolTip("设置子图")      # Configure subplots
        actList[7].setText("定制")      # Customize
        actList[7].setToolTip("定制图表参数")
        actList[9].setText("保存")      # Save
        actList[9].setToolTip("保存图表")      # Save the figure

    def setToolbarVisible(self, isVisible=True):
        """ 是否显示工具栏 """
        self.__showToolbar = isVisible
        self.naviBar.setVisible(isVisible)

    def setDataHintVisible(self, isVisible=True):
        """ 是否显示坐标提示 """
        self.__showHint = isVisible
        self.__lastActionHint.setVisible(isVisible)

    def redraw(self):
        """ 重绘曲线 """
        self.figure.canvas.draw()

    def do_scrollZoom(self, event):
        """ 通过鼠标滚轮缩放 """
        ax = event.inaxes       # 产生事件 axes 对象
        assert ax is not None, "axes is None"

        self.naviBar.push_current()

        # 获取鼠标当前位置的数据坐标
        x_data = event.xdata
        y_data = event.ydata

        # 获取当前坐标轴的数据范围
        xmin, xmax = ax.get_xbound()
        xlen = xmax - xmin
        ymin, ymax = ax.get_ybound()
        ylen = ymax - ymin

        # 计算缩放比例，这里根据需要调整系数
        scale_factor = 0.1  # 缩放因子，根据需要调整
        if event.step < 0:
            scale_factor = -scale_factor

        # 计算新的坐标轴范围
        xmin_new = x_data - (x_data - xmin) * (1 + scale_factor)
        xmax_new = x_data + (xmax - x_data) * (1 + scale_factor)
        # ymin_new = y_data - (y_data - ymin) * (1 + scale_factor)
        # ymax_new = y_data + (ymax - y_data) * (1 + scale_factor)

        # 设置新的坐标轴范围
        ax.set_xbound(xmin_new, xmax_new)
        # ax.set_ybound(ymin_new, ymax_new)

        event.canvas.draw()

    def drawWave(self, x_data, y_data):
        self.x_data = x_data
        self.y_data = y_data
        self.figure.clear()
        self.ax = self.figure.add_subplot(1, 1, 1)
        self.ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
        self.ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
        self.ax.plot(self.x_data, self.y_data, marker='s', markersize=3, markeredgewidth=0)
        self.ax.grid()

        # 添加可拖动竖条
        self.vline1 = self.ax.axvline(x=self.initial_x[0], color='r', linestyle='--', linewidth=2)
        self.vline2 = self.ax.axvline(x=self.initial_x[1], color='b', linestyle='--', linewidth=2)
        self.text1 = self.ax.text(0.7, 0.95, '', transform=self.ax.transAxes, verticalalignment='top', color='r')
        self.text2 = self.ax.text(0.7, 0.9, '', transform=self.ax.transAxes, verticalalignment='top', color='b')
        self.press = None
        self.figure.canvas.draw()


    def find_closest_line(self, x_press):
        x1 = self.vline1.get_xdata()[0]
        x2 = self.vline2.get_xdata()[0]

        dist1 = abs(x1 - x_press)
        dist2 = abs(x2 - x_press)

        if dist1 < dist2:
            return 0, x1
        else:
            return 1, x2

    def on_press(self, event):
        if event.inaxes != self.ax:
            QMessageBox.warning(self, "警告", "ax 错误")
            return
        if event.button != 1:
            QMessageBox.warning(self, "警告", "button 错误")
            return

        x_press = event.xdata
        closest_line = self.find_closest_line(x_press)
        line_idx = closest_line[0]
        x_data = closest_line[1]

        self.press = line_idx, x_data, x_press, event.ydata
        self.update_text()

    def update_text(self):
        x_val1 = self.vline1.get_xdata()[0]
        x_val2 = self.vline2.get_xdata()[0]

        idx1 = np.argmin(np.abs(self.x_data - x_val1))
        idx2 = np.argmin(np.abs(self.x_data - x_val2))

        x_closest1 = self.x_data[idx1]
        y_closest1 = self.y_data[idx1]

        x_closest2 = self.x_data[idx2]
        y_closest2 = self.y_data[idx2]

        self.text1.set_text(f'x1={int(x_closest1)}, y1={int(y_closest1)}')
        self.text2.set_text(f'x2={int(x_closest2)}, y2={int(y_closest2)}')


    def on_motion(self, event):
        if self.press is None:
            return
        line_idx, x_data, x_press, y_press = self.press
        if event.xdata is None:
            return

        dx = event.xdata - x_press
        new_x = x_data + dx
        idx = np.argmin(np.abs(self.x_data - new_x))
        x_closest = self.x_data[idx]

        if line_idx == 0:
            self.vline1.set_xdata([x_closest])
        elif line_idx == 1:
            self.vline2.set_xdata([x_closest])

        self.update_text()
        self.ax.figure.canvas.draw()


    def on_release(self, event):
        if self.press is None:
            return
        line_idx, _, _, _ = self.press
        x_current = self.vline1.get_xdata()[0] if line_idx == 0 else self.vline2.get_xdata()[0]

        if line_idx == 0:
            self.x1_update_signal.emit(x_current)
        elif line_idx == 1:
            self.x2_update_signal.emit(x_current)
        self.selected_lines[line_idx] = x_current
        self.press = None
        self.update_text()

    def update_text(self):
        x_val1 = self.vline1.get_xdata()[0]
        x_val2 = self.vline2.get_xdata()[0]

        idx1 = np.argmin(np.abs(self.x_data - x_val1))
        idx2 = np.argmin(np.abs(self.x_data - x_val2))

        x_closest1 = self.x_data[idx1]
        y_closest1 = self.y_data[idx1]

        x_closest2 = self.x_data[idx2]
        y_closest2 = self.y_data[idx2]

        self.text1.set_text(f'x1={int(x_closest1)}, y1={int(y_closest1)}')
        self.text2.set_text(f'x2={int(x_closest2)}, y2={int(y_closest2)}')


