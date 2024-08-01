# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'infodialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_infoDialog(object):
    def setupUi(self, infoDialog):
        if not infoDialog.objectName():
            infoDialog.setObjectName(u"infoDialog")
        infoDialog.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(infoDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label = QLabel(infoDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_row = QLabel(infoDialog)
        self.label_row.setObjectName(u"label_row")
        self.label_row.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_row)

        self.label_3 = QLabel(infoDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_time = QLabel(infoDialog)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_time)

        self.label_5 = QLabel(infoDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.label_wave = QLabel(infoDialog)
        self.label_wave.setObjectName(u"label_wave")
        self.label_wave.setMaximumSize(QSize(400, 16777215))
        self.label_wave.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_wave)

        self.label_7 = QLabel(infoDialog)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.label_length = QLabel(infoDialog)
        self.label_length.setObjectName(u"label_length")
        self.label_length.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_length)

        self.label_9 = QLabel(infoDialog)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_9)

        self.label_speed = QLabel(infoDialog)
        self.label_speed.setObjectName(u"label_speed")
        self.label_speed.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_speed)

        self.label_11 = QLabel(infoDialog)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_11)

        self.label_incident = QLabel(infoDialog)
        self.label_incident.setObjectName(u"label_incident")
        self.label_incident.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.label_incident)

        self.label_13 = QLabel(infoDialog)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_13)

        self.label_reflected = QLabel(infoDialog)
        self.label_reflected.setObjectName(u"label_reflected")
        self.label_reflected.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.label_reflected)

        self.label_15 = QLabel(infoDialog)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_15)

        self.label_distance = QLabel(infoDialog)
        self.label_distance.setObjectName(u"label_distance")
        self.label_distance.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.label_distance)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(infoDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(infoDialog)
        self.buttonBox.accepted.connect(infoDialog.accept)
        self.buttonBox.rejected.connect(infoDialog.reject)

        QMetaObject.connectSlotsByName(infoDialog)
    # setupUi

    def retranslateUi(self, infoDialog):
        infoDialog.setWindowTitle(QCoreApplication.translate("infoDialog", u"\u4fe1\u606f\u786e\u8ba4", None))
        self.label.setText(QCoreApplication.translate("infoDialog", u"\u884c\u53f7\uff1a", None))
        self.label_row.setText(QCoreApplication.translate("infoDialog", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("infoDialog", u"GPS \u65f6\u95f4\uff1a", None))
        self.label_time.setText(QCoreApplication.translate("infoDialog", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("infoDialog", u"\u5e45\u503c\u6570\u7ec4\uff1a", None))
        self.label_wave.setText(QCoreApplication.translate("infoDialog", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("infoDialog", u"\u603b\u957f (m)\uff1a", None))
        self.label_length.setText(QCoreApplication.translate("infoDialog", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("infoDialog", u"\u6ce2\u901f (m/us)\uff1a", None))
        self.label_speed.setText(QCoreApplication.translate("infoDialog", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("infoDialog", u"\u5165\u5c04\u6ce2\u70b9\uff1a", None))
        self.label_incident.setText(QCoreApplication.translate("infoDialog", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("infoDialog", u"\u53cd\u5c04\u6ce2\u70b9\uff1a", None))
        self.label_reflected.setText(QCoreApplication.translate("infoDialog", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("infoDialog", u"\u6545\u969c\u70b9\u8ddd\u79bb (m)\uff1a", None))
        self.label_distance.setText(QCoreApplication.translate("infoDialog", u"TextLabel", None))
    # retranslateUi

