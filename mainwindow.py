# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QHeaderView, QMessageBox, QDialog, QTableView
from PySide6.QtCore import Slot, QAbstractTableModel, Qt

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from ui_infodialog import Ui_infoDialog

import numpy as np
import pandas as pd
import matplotlib as mpl


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Demo")
        self.setCentralWidget(self.ui.tabWidget)
        # mpl.rcParams['font.sans-serif'] = ['SimHei']
        mpl.rcParams['font.size'] = 9
        mpl.rcParams['axes.unicode_minus'] = False

        self.x_data = None
        self.y_data = None
        self.dataModel = None
        self.row_data = None

        # 自动拉伸列宽
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 连接信号
        self.ui.pushButton_0.clicked.connect(self.calculate)
        self.ui.spinBox_incidentWave.valueChanged.connect(self.calculate)
        self.ui.spinBox_reflectedWave.valueChanged.connect(self.calculate)
        self.ui.pushButton_1.clicked.connect(self.writeBack)
        self.ui.pushButton_openFile.clicked.connect(self.openFile)
        self.ui.pushButton_saveFile.clicked.connect(self.saveFile)
        self.ui.tableView.verticalHeader().sectionClicked.connect(self.onSectionClicked)
        self.ui.widgetChart.x1_update_signal.connect(self.x1_update)
        self.ui.widgetChart.x2_update_signal.connect(self.x2_update)

    def __drawWave(self):
        if self.row_data is None:
            QMessageBox.critical(self, "错误", "未获取到一行数据")
            return
        self.y_data = np.array(eval(self.row_data['waveform']))
        if self.y_data is None:
            QMessageBox.critical(self, "错误", "未获取到幅值数组")
            return
        print("绘图时的数组长度：\n")
        print(self.y_data.shape)
        self.x_data = np.arange(len(self.y_data))
        self.ui.widgetChart.drawWave(self.x_data, self.y_data)


    @Slot()
    def calculate(self):
        s = eval(self.ui.lineEdit_length.text())
        v = eval(self.ui.lineEdit_waveSpeed.text())
        a = self.ui.spinBox_incidentWave.value()
        b = self.ui.spinBox_reflectedWave.value()
        deltaT = (b - a) * 0.02
        result = s - 0.5 * deltaT * v
        self.ui.lineEdit_timeDifference.setText(str(deltaT))
        self.ui.lineEdit_result.setText(str(result))
        if a == 0 and b == 0:
            self.ui.lineEdit_timeDifference.setText('/')
            self.ui.lineEdit_result.setText('/')
        self.ui.statusbar.showMessage("计算故障点距离" , 2000)

    @Slot()
    def writeBack(self):
        self.row_data['length'] = str(self.ui.lineEdit_length.text())
        self.row_data['speed'] = str(self.ui.lineEdit_waveSpeed.text())
        self.row_data['in_wave'] = str(self.ui.spinBox_incidentWave.value())
        self.row_data['back_wave'] = str(self.ui.spinBox_reflectedWave.value())
        self.row_data['distance'] = str(self.ui.lineEdit_result.text())
        print("写回的数据\n")
        print(self.row_data)
        self.dataModel.setRowData(self.row_data.name, self.row_data)
        self.ui.tabWidget.setCurrentIndex(0)
        row = int(self.row_data.name)
        index = self.dataModel.index(row, 0)
        self.ui.tableView.scrollTo(index, QTableView.PositionAtTop)
        self.ui.tableView.selectRow(row)
        self.ui.statusbar.showMessage("数据行写回 DataModel", 2000)

    @Slot()
    def openFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "打开 CSV 文件", "", "CSV 文件 (*.csv);;所有文件 (*.*)", options=options)
        if fileName:
            self.loadCSVFile(fileName)
        self.ui.statusbar.showMessage(f'打开文件 : {fileName}', 2000)

    def loadCSVFile(self, fileName):
        try:
            df = pd.read_csv(fileName)
            df = df.fillna('')
        except Exception as e:
            QMessageBox.critical(self, "错误", f"加载 CSV 文件失败:\n{str(e)}")
            return
        if df.empty:
            QMessageBox.warning(self, "空的 CSV", "选择的 CSV 文件是空的。")
            return
        # 检查是否存在指定的列，如果不存在，则添加列
        required_columns = ['gps_time', 'waveform', 'length', 'speed', 'in_wave', 'back_wave', 'distance']
        existing_columns = df.columns.tolist()
        columns_to_add = [col for col in required_columns if col not in existing_columns]
        if columns_to_add:
            for col in columns_to_add:
                df[col] = ''  # 在 DataFrame 中添加空列
        self.dataModel = PandasModel(df)
        self.ui.tableView.setModel(self.dataModel)


    @Slot()
    def saveFile(self):
        if self.dataModel is None:
            QMessageBox.warning(self, "无数据", "没有要保存的 CSV 数据。")
            return
        fileName, _ = QFileDialog.getSaveFileName(self, "保存 CSV 文件", "", "CSV 文件 (*.csv)")
        if fileName:
            try:
                if not fileName.endswith(".csv"):
                    fileName = fileName + '.csv'
                self.dataModel._data.to_csv(fileName, index=False)
                QMessageBox.information(self, "文件已保存", f"CSV 文件保存成功:\n{fileName}")
            except Exception as e:
                QMessageBox.critical(self, "错误", f"保存 CSV 文件失败:\n{str(e)}")
        self.ui.statusbar.showMessage(f'保存文件 : {fileName}', 2000)

    @Slot()
    def onSectionClicked(self, logicalIndex):
        # logicalIndex 是点击的行号
        if self.dataModel is None:
            QMessageBox.warning(self, "错误", "数据模型不存在。")
            return

        self.row_data = self.dataModel.getRowData(logicalIndex)
        if self.row_data is None:
            QMessageBox.critical(self, "错误", "获取数据失败。")
            return

        # 创建对话框实例
        infoDialog = QDialog()
        dialog_ui = Ui_infoDialog()
        dialog_ui.setupUi(infoDialog)
        dialog_ui.label_row.setText(str(self.row_data.name))
        dialog_ui.label_time.setText(str(self.row_data['gps_time']))
        dialog_ui.label_wave.setText(str(self.row_data['waveform']))
        dialog_ui.label_length.setText(str(self.row_data['length']))
        dialog_ui.label_speed.setText(str(self.row_data['speed']))
        dialog_ui.label_incident.setText(str(self.row_data['in_wave']))
        dialog_ui.label_reflected.setText(str(self.row_data['back_wave']))
        dialog_ui.label_distance.setText(str(self.row_data['distance']))

        # 显示对话框
        if infoDialog.exec() == QDialog.Accepted:
            self.ui.statusbar.showMessage('开始标注' , 2000)
            if self.row_data['length'] != '':
                self.ui.lineEdit_length.setText(str(self.row_data['length']))
            else:
                self.ui.lineEdit_length.setText('1400')
            if self.row_data['speed'] != '':
                self.ui.lineEdit_waveSpeed.setText(str(self.row_data['speed']))
            else:
                self.ui.lineEdit_waveSpeed.setText('165')
            if self.row_data['in_wave'] != '':
                self.ui.spinBox_incidentWave.setValue(int(self.row_data['in_wave']))
            else:
                self.ui.spinBox_incidentWave.setValue(0)
            if self.row_data['back_wave'] != '':
                self.ui.spinBox_reflectedWave.setValue(int(self.row_data['back_wave']))
            else:
                self.ui.spinBox_reflectedWave.setValue(0)
            if self.row_data['distance'] != '':
                self.ui.lineEdit_result.setText(str(self.row_data['distance']))
            else:
                self.ui.lineEdit_result.setText('/')
            self.__drawWave()
            self.ui.tabWidget.setCurrentIndex(1)

    @Slot()
    def x1_update(self, x1_current):
        if x1_current == None:
            return
        self.ui.spinBox_incidentWave.setValue(int(x1_current))

    @Slot()
    def x2_update(self, x2_current):
        if x2_current == None:
            return
        self.ui.spinBox_reflectedWave.setValue(int(x2_current))


class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent = None):
        return len(self._data.index)

    def columnCount(self, parent = None):
        return len(self._data.columns)

    # 获取索引位置的数据
    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            return str(self._data.iloc[index.row(), index.column()])
        return None

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            row = index.row()
            col = index.column()
            self._data.iat[row, col] = value
            return True
        return False

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return str(self._data.columns[section])
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return str(self._data.index[section])
        return None

    def getRowData(self, row):
        if 0 <= row < self.rowCount():
            row_data = self._data.iloc[row].copy()
            # 转换 'waveform' 列为 numpy 数组
            # row_data['waveform'] = np.array(row_data['waveform'])
            return row_data
        return None

    def setRowData(self, row, row_data):
        if 0 <= row < self.rowCount():
            self._data.iloc[int(row)] = row_data
        return None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
