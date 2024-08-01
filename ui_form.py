# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QTabWidget,
    QTableView, QVBoxLayout, QWidget)

from myFigureCanvas import QmyFigureCanvas

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(925, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_0 = QWidget()
        self.tab_0.setObjectName(u"tab_0")
        self.verticalLayout_2 = QVBoxLayout(self.tab_0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_openFile = QPushButton(self.tab_0)
        self.pushButton_openFile.setObjectName(u"pushButton_openFile")

        self.gridLayout_2.addWidget(self.pushButton_openFile, 0, 0, 1, 1)

        self.pushButton_saveFile = QPushButton(self.tab_0)
        self.pushButton_saveFile.setObjectName(u"pushButton_saveFile")

        self.gridLayout_2.addWidget(self.pushButton_saveFile, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.tableView = QTableView(self.tab_0)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_2.addWidget(self.tableView)

        self.tabWidget.addTab(self.tab_0, "")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.horizontalLayout = QHBoxLayout(self.tab_1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.tab_1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_waveSpeed = QLineEdit(self.frame)
        self.lineEdit_waveSpeed.setObjectName(u"lineEdit_waveSpeed")

        self.gridLayout.addWidget(self.lineEdit_waveSpeed, 0, 3, 1, 1)

        self.label_0 = QLabel(self.frame)
        self.label_0.setObjectName(u"label_0")

        self.gridLayout.addWidget(self.label_0, 0, 0, 1, 1)

        self.spinBox_reflectedWave = QSpinBox(self.frame)
        self.spinBox_reflectedWave.setObjectName(u"spinBox_reflectedWave")
        self.spinBox_reflectedWave.setMaximum(20000)

        self.gridLayout.addWidget(self.spinBox_reflectedWave, 1, 3, 1, 1)

        self.label_1 = QLabel(self.frame)
        self.label_1.setObjectName(u"label_1")

        self.gridLayout.addWidget(self.label_1, 0, 2, 1, 1)

        self.lineEdit_length = QLineEdit(self.frame)
        self.lineEdit_length.setObjectName(u"lineEdit_length")

        self.gridLayout.addWidget(self.lineEdit_length, 0, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.spinBox_incidentWave = QSpinBox(self.frame)
        self.spinBox_incidentWave.setObjectName(u"spinBox_incidentWave")
        self.spinBox_incidentWave.setMinimum(0)
        self.spinBox_incidentWave.setMaximum(20000)

        self.gridLayout.addWidget(self.spinBox_incidentWave, 1, 1, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.lineEdit_timeDifference = QLineEdit(self.frame)
        self.lineEdit_timeDifference.setObjectName(u"lineEdit_timeDifference")

        self.gridLayout.addWidget(self.lineEdit_timeDifference, 2, 1, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)

        self.lineEdit_result = QLineEdit(self.frame)
        self.lineEdit_result.setObjectName(u"lineEdit_result")

        self.gridLayout.addWidget(self.lineEdit_result, 2, 3, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)

        self.horizontalLayout_0 = QHBoxLayout()
        self.horizontalLayout_0.setObjectName(u"horizontalLayout_0")
        self.pushButton_0 = QPushButton(self.frame)
        self.pushButton_0.setObjectName(u"pushButton_0")

        self.horizontalLayout_0.addWidget(self.pushButton_0)

        self.pushButton_1 = QPushButton(self.frame)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.horizontalLayout_0.addWidget(self.pushButton_1)


        self.verticalLayout_4.addLayout(self.horizontalLayout_0)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame)

        self.widgetChart = QmyFigureCanvas(self.tab_1)
        self.widgetChart.setObjectName(u"widgetChart")
        self.widgetChart.setMinimumSize(QSize(500, 0))

        self.horizontalLayout.addWidget(self.widgetChart)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.formLayout = QFormLayout(self.tab_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setOpenExternalLinks(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_7)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.formLayout.setItem(2, QFormLayout.LabelRole, self.horizontalSpacer)

        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_9)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.formLayout.setItem(3, QFormLayout.LabelRole, self.horizontalSpacer_2)

        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_10)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.formLayout.setItem(4, QFormLayout.LabelRole, self.horizontalSpacer_3)

        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_11)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.formLayout.setItem(5, QFormLayout.LabelRole, self.horizontalSpacer_4)

        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.label_12)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.formLayout.setItem(6, QFormLayout.LabelRole, self.horizontalSpacer_5)

        self.label_13 = QLabel(self.tab_2)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.label_13)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.formLayout.setItem(7, QFormLayout.LabelRole, self.horizontalSpacer_6)

        self.label_14 = QLabel(self.tab_2)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.label_14)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 925, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label_0.setBuddy(self.lineEdit_length)
        self.label_1.setBuddy(self.lineEdit_waveSpeed)
        self.label_3.setBuddy(self.spinBox_reflectedWave)
        self.label_2.setBuddy(self.spinBox_incidentWave)
        self.label_4.setBuddy(self.lineEdit_timeDifference)
        self.label_5.setBuddy(self.lineEdit_result)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEdit_length, self.lineEdit_waveSpeed)
        QWidget.setTabOrder(self.lineEdit_waveSpeed, self.spinBox_incidentWave)
        QWidget.setTabOrder(self.spinBox_incidentWave, self.spinBox_reflectedWave)
        QWidget.setTabOrder(self.spinBox_reflectedWave, self.lineEdit_timeDifference)
        QWidget.setTabOrder(self.lineEdit_timeDifference, self.lineEdit_result)
        QWidget.setTabOrder(self.lineEdit_result, self.pushButton_0)
        QWidget.setTabOrder(self.pushButton_0, self.pushButton_1)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_openFile.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6", None))
        self.pushButton_saveFile.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6587\u4ef6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_0), QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u548c\u67e5\u770b", None))
        self.lineEdit_waveSpeed.setText(QCoreApplication.translate("MainWindow", u"165", None))
        self.label_0.setText(QCoreApplication.translate("MainWindow", u"\u603b\u957f s (\u5355\u4f4d: m)", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u901f v (\u5355\u4f4d: m/us)", None))
        self.lineEdit_length.setText(QCoreApplication.translate("MainWindow", u"1400", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u53cd\u5c04\u70b9 b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5165\u5c04\u70b9 a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4\u5dee \u0394t (\u5355\u4f4d: us)", None))
        self.lineEdit_timeDifference.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6545\u969c\u70b9\u8ddd\u79bb (\u5355\u4f4d: m)", None))
        self.lineEdit_result.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButton_0.setText(QCoreApplication.translate("MainWindow", u"\u8ba1    \u7b97", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"\u5199    \u56de", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97\u548c\u6807\u8bb0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"MADE WITH \u2665 BY : ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<a href = \"https://github.com/Li-4\">github/Li-4", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u6b65\u9aa4 : ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"0. \u8bf7\u5148\u70b9\u51fb \u201c\u6253\u5f00\u6587\u4ef6\u201d \u9009\u62e9 CSV \u6570\u636e\u6587\u4ef6", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"1. \u6253\u5f00\u6b63\u786e\u7684 CSV \u6587\u4ef6\u540e\uff0c\u4f1a\u5728\u4e0b\u65b9\u663e\u793a\u8868\u683c\uff0c\u70b9\u51fb\u6bcf\u4e00\u884c\u7684\u8868\u5934\u786e\u8ba4\u8be5\u884c\u5185\u5bb9", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"2. \u70b9\u51fb \u201cOK\u201d \u540e\u4f1a\u81ea\u52a8\u8df3\u8f6c\u81f3 \u201c\u8ba1\u7b97\u548c\u6807\u8bb0\u9875\u201d \u53f3\u65b9\u663e\u793a\u6ce2\u5f62\uff0c\u6ce2\u5f62\u56fe\u652f\u6301\u4ee5\u9f20\u6807\u4f4d\u7f6e\u4e3a\u4e2d\u5fc3\u7f29\u653e", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"3. \u6ce2\u5f62\u56fe\u4e0a\u5177\u6709\u4e24\u6761\u7ad6\u7ebf\uff0c\u5176\u4e2d\u7ea2\u8272\u4ee3\u8868\u5165\u5c04\u6ce2\u8d77\u70b9\uff0c\u84dd\u8272\u4ee3\u8868\u53cd\u5c04\u6ce2\u542f\u52a8\uff0c\u9f20\u6807\u5355\u51fb\u4f1a\u81ea\u52a8\u9009\u62e9\u6700\u8fd1\u7684\u7ad6\u7ebf", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"4. \u62d6\u62fd\u7ad6\u7ebf\u53ef\u79fb\u52a8\u4f4d\u7f6e\uff0c\u505c\u6b62\u62d6\u62fd\u540e\u4f1a\u81ea\u52a8\u8ba1\u7b97\u7ed3\u679c\uff0c\u70b9\u51fb \u201c\u5199\u56de\u201d \u4f1a\u8df3\u8f6c\u81f3 \u201c\u6587\u4ef6\u548c\u67e5\u770b\u201d \u5e76\u9ad8\u4eae\u6807\u8bb0\u7684\u6570\u636e\u884c", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"5. \u8bf7\u52a1\u5fc5\u70b9\u51fb \u201c\u4fdd\u5b58\u6587\u4ef6\u201d \u53ca\u65f6\u4fdd\u5b58", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"6. \u8bf7\u52a1\u5fc5\u70b9\u51fb \u201c\u4fdd\u5b58\u6587\u4ef6\u201d \u53ca\u65f6\u4fdd\u5b58", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9\u548c\u652f\u6301", None))
    # retranslateUi

