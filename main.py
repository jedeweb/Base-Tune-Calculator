from PyQt5 import QtCore, QtGui, QtWidgets
import functions
import variables

# Pass input through functions.TuneCar and output to lines on right


def guiTuneCar():
    # check input for lb or kg and set value for weight in kg
    if ui.radbtnLb.isChecked():
        WeightKg = functions.lb_to_kg(ui.lineWeight.text())
    else:
        WeightKg = float(ui.lineWeight.text())
    # set variables from form to input to TuneCar function
    SpringType = ui.listSpringType.currentText()
    FrontDist = ui.spnDistribution.value()
    CarClass = ui.listCarClass.currentText()
    DriveType = ui.listDrivetype.currentText()
    # run the TuneCar function, output saved to variables.Tune[] dictionary
    functions.TuneCar(
        WeightKg,
        SpringType.upper(),
        float(FrontDist),
        CarClass.upper(),
        DriveType.upper(),
    )
    # set line values on right form to calculated output
    ui.lineFrontSpring.setText(str(round(variables.Tune["SpringFrontLb"], 1)))
    ui.lineRearSpring.setText(str(round(variables.Tune["SpringRearLb"], 1)))
    ui.lineFrontArb.setText(str(round(variables.Tune["ArbFront"], 1)))
    ui.lineRearArb.setText(str(round(variables.Tune["ArbRear"], 1)))
    ui.lineFrontRebound.setText(str(round(variables.Tune["ReboundFront"], 1)))
    ui.lineRearRebound.setText(str(round(variables.Tune["ReboundRear"], 1)))
    ui.lineFrontBump.setText(str(round(variables.Tune["BumpFront"], 1)))
    ui.lineRearBump.setText(str(round(variables.Tune["BumpRear"], 1)))


# All this window fun was generated from QT Designer
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frmLeft = QtWidgets.QFrame(self.centralwidget)
        self.frmLeft.setGeometry(QtCore.QRect(0, 0, 341, 521))
        self.frmLeft.setFrameShape(QtWidgets.QFrame.Box)
        self.frmLeft.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frmLeft.setObjectName("frmLeft")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frmLeft)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 460, 321, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layoutLeftBottom = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layoutLeftBottom.setContentsMargins(0, 0, 0, 0)
        self.layoutLeftBottom.setObjectName("layoutLeftBottom")
        self.btnTuneCar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnTuneCar.setObjectName("btnTuneCar")
        self.layoutLeftBottom.addWidget(self.btnTuneCar)
        self.formLayoutWidget = QtWidgets.QWidget(self.frmLeft)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 321, 451))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.layoutLeft = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.layoutLeft.setContentsMargins(0, 0, 0, 0)
        self.layoutLeft.setObjectName("layoutLeft")
        self.lblCarClass = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblCarClass.setObjectName("lblCarClass")
        self.layoutLeft.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblCarClass)
        self.listCarClass = QtWidgets.QComboBox(self.formLayoutWidget)
        self.listCarClass.setObjectName("listCarClass")
        self.listCarClass.addItem("")
        self.listCarClass.setItemText(0, "D")
        self.listCarClass.addItem("")
        self.listCarClass.setItemText(1, "C")
        self.listCarClass.addItem("")
        self.listCarClass.setItemText(2, "B")
        self.listCarClass.addItem("")
        self.listCarClass.setItemText(3, "A")
        self.listCarClass.addItem("")
        self.listCarClass.setItemText(4, "S1")
        self.listCarClass.addItem("")
        self.listCarClass.setItemText(5, "S2")
        self.listCarClass.addItem("")
        self.listCarClass.setItemText(6, "X")
        self.layoutLeft.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.listCarClass)
        self.lblSpringType = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblSpringType.setObjectName("lblSpringType")
        self.layoutLeft.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.lblSpringType
        )
        self.listSpringType = QtWidgets.QComboBox(self.formLayoutWidget)
        self.listSpringType.setObjectName("listSpringType")
        self.listSpringType.addItem("")
        self.listSpringType.addItem("")
        self.listSpringType.addItem("")
        self.listSpringType.addItem("")
        self.layoutLeft.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.listSpringType
        )
        self.lblDriveType = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblDriveType.setObjectName("lblDriveType")
        self.layoutLeft.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblDriveType)
        self.listDrivetype = QtWidgets.QComboBox(self.formLayoutWidget)
        self.listDrivetype.setObjectName("listDrivetype")
        self.listDrivetype.addItem("")
        self.listDrivetype.setItemText(0, "RWD")
        self.listDrivetype.addItem("")
        self.listDrivetype.setItemText(1, "FWD")
        self.listDrivetype.addItem("")
        self.listDrivetype.setItemText(2, "AWD")
        self.layoutLeft.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.listDrivetype
        )
        self.lblWeightUnit = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblWeightUnit.setObjectName("lblWeightUnit")
        self.layoutLeft.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.lblWeightUnit
        )
        self.layoutWeightButtons = QtWidgets.QHBoxLayout()
        self.layoutWeightButtons.setObjectName("layoutWeightButtons")
        self.radbtnLb = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radbtnLb.setObjectName("radbtnLb")
        self.layoutWeightButtons.addWidget(self.radbtnLb)
        self.radbtnLb.setChecked(True)
        self.radbtnKg = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radbtnKg.setObjectName("radbtnKg")
        self.layoutWeightButtons.addWidget(self.radbtnKg)
        self.layoutLeft.setLayout(
            3, QtWidgets.QFormLayout.FieldRole, self.layoutWeightButtons
        )
        self.lblWeight = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblWeight.setObjectName("lblWeight")
        self.layoutLeft.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblWeight)
        self.lineWeight = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineWeight.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineWeight.setText("0")
        self.lineWeight.setObjectName("lineWeight")
        self.layoutLeft.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineWeight)
        self.lblDistribution = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblDistribution.setObjectName("lblDistribution")
        self.layoutLeft.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.lblDistribution
        )
        self.spnDistribution = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spnDistribution.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spnDistribution.setMinimum(1)
        self.spnDistribution.setProperty("value", 50)
        self.spnDistribution.setObjectName("spnDistribution")
        self.layoutLeft.setWidget(
            5, QtWidgets.QFormLayout.FieldRole, self.spnDistribution
        )
        self.lblSpringTightness = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblSpringTightness.setObjectName("lblSpringTightness")
        self.layoutLeft.setWidget(
            6, QtWidgets.QFormLayout.LabelRole, self.lblSpringTightness
        )
        self.lblArbTightnes = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblArbTightnes.setObjectName("lblArbTightnes")
        self.layoutLeft.setWidget(
            7, QtWidgets.QFormLayout.LabelRole, self.lblArbTightnes
        )
        self.sldrSpring = QtWidgets.QSlider(self.formLayoutWidget)
        self.sldrSpring.setMinimum(1)
        self.sldrSpring.setProperty("value", 50)
        self.sldrSpring.setOrientation(QtCore.Qt.Horizontal)
        self.sldrSpring.setObjectName("sldrSpring")
        self.layoutLeft.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.sldrSpring)
        self.sldrArb = QtWidgets.QSlider(self.formLayoutWidget)
        self.sldrArb.setMinimum(1)
        self.sldrArb.setProperty("value", 50)
        self.sldrArb.setOrientation(QtCore.Qt.Horizontal)
        self.sldrArb.setObjectName("sldrArb")
        self.layoutLeft.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.sldrArb)
        self.frmRight = QtWidgets.QFrame(self.centralwidget)
        self.frmRight.setGeometry(QtCore.QRect(340, 0, 341, 521))
        self.frmRight.setFrameShape(QtWidgets.QFrame.Box)
        self.frmRight.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frmRight.setObjectName("frmRight")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.frmRight)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 321, 331))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.layoutRight = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.layoutRight.setContentsMargins(0, 0, 0, 0)
        self.layoutRight.setObjectName("layoutRight")
        self.lblSpringFront = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lblSpringFront.setObjectName("lblSpringFront")
        self.layoutRight.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.lblSpringFront
        )
        self.lblSpringRear = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lblSpringRear.setObjectName("lblSpringRear")
        self.layoutRight.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.lblSpringRear
        )
        self.lblFrontArb = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lblFrontArb.setObjectName("lblFrontArb")
        self.layoutRight.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblFrontArb)
        self.lblRearArb = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lblRearArb.setObjectName("lblRearArb")
        self.layoutRight.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblRearArb)
        self.lblFrontRebound = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lblFrontRebound.setObjectName("lblFrontRebound")
        self.layoutRight.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.lblFrontRebound
        )
        self.lblRearRebound = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lblRearRebound.setObjectName("lblRearRebound")
        self.layoutRight.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.lblRearRebound
        )
        self.lblFrontBump = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lblFrontBump.setObjectName("lblFrontBump")
        self.layoutRight.setWidget(
            6, QtWidgets.QFormLayout.LabelRole, self.lblFrontBump
        )
        self.lblRearBump = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lblRearBump.setObjectName("lblRearBump")
        self.layoutRight.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.lblRearBump)
        self.lineFrontSpring = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineFrontSpring.setEnabled(True)
        self.lineFrontSpring.setReadOnly(True)
        self.lineFrontSpring.setObjectName("lineFrontSpring")
        self.layoutRight.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.lineFrontSpring
        )
        self.lineRearSpring = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineRearSpring.setEnabled(True)
        self.lineRearSpring.setReadOnly(True)
        self.lineRearSpring.setObjectName("lineRearSpring")
        self.layoutRight.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.lineRearSpring
        )
        self.lineFrontArb = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineFrontArb.setEnabled(True)
        self.lineFrontArb.setReadOnly(True)
        self.lineFrontArb.setObjectName("lineFrontArb")
        self.layoutRight.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.lineFrontArb
        )
        self.lineRearArb = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineRearArb.setEnabled(True)
        self.lineRearArb.setReadOnly(True)
        self.lineRearArb.setObjectName("lineRearArb")
        self.layoutRight.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineRearArb)
        self.lineFrontRebound = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineFrontRebound.setEnabled(True)
        self.lineFrontRebound.setReadOnly(True)
        self.lineFrontRebound.setObjectName("lineFrontRebound")
        self.layoutRight.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.lineFrontRebound
        )
        self.lineRearRebound = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineRearRebound.setEnabled(True)
        self.lineRearRebound.setReadOnly(True)
        self.lineRearRebound.setObjectName("lineRearRebound")
        self.layoutRight.setWidget(
            5, QtWidgets.QFormLayout.FieldRole, self.lineRearRebound
        )
        self.lineFrontBump = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineFrontBump.setEnabled(True)
        self.lineFrontBump.setReadOnly(True)
        self.lineFrontBump.setObjectName("lineFrontBump")
        self.layoutRight.setWidget(
            6, QtWidgets.QFormLayout.FieldRole, self.lineFrontBump
        )
        self.lineRearBump = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineRearBump.setEnabled(True)
        self.lineRearBump.setReadOnly(True)
        self.lineRearBump.setObjectName("lineRearBump")
        self.layoutRight.setWidget(
            7, QtWidgets.QFormLayout.FieldRole, self.lineRearBump
        )
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Forza Horizon 5 Car Tuner"))
        self.btnTuneCar.setText(_translate("MainWindow", "Tune Car"))
        self.lblCarClass.setText(_translate("MainWindow", "Car Class"))
        self.lblSpringType.setText(_translate("MainWindow", "Spring Type"))
        self.listSpringType.setItemText(0, _translate("MainWindow", "Rally"))
        self.listSpringType.setItemText(1, _translate("MainWindow", "Race"))
        self.listSpringType.setItemText(2, _translate("MainWindow", "Drift"))
        self.listSpringType.setItemText(3, _translate("MainWindow", "Stock Buggy"))
        self.lblDriveType.setText(_translate("MainWindow", "Drive Type"))
        self.lblWeightUnit.setText(_translate("MainWindow", "Weight Unit"))
        self.radbtnLb.setText(_translate("MainWindow", "Lb"))
        self.radbtnKg.setText(_translate("MainWindow", "Kg"))
        self.lblWeight.setText(_translate("MainWindow", "Weight"))
        self.lblDistribution.setText(_translate("MainWindow", "Weight Distribution"))
        self.lblSpringTightness.setText(_translate("MainWindow", "Spring Tightness"))
        self.lblArbTightnes.setText(_translate("MainWindow", "ARB Tightness"))
        self.lblSpringFront.setText(_translate("MainWindow", "Front Spring"))
        self.lblSpringRear.setText(_translate("MainWindow", "Rear Spring"))
        self.lblFrontArb.setText(_translate("MainWindow", "Front ARB"))
        self.lblRearArb.setText(_translate("MainWindow", "Rear ARB"))
        self.lblFrontRebound.setText(_translate("MainWindow", "Front Rebound"))
        self.lblRearRebound.setText(_translate("MainWindow", "Rear Rebound"))
        self.lblFrontBump.setText(_translate("MainWindow", "Front Bump"))
        self.lblRearBump.setText(_translate("MainWindow", "Rear Bump"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # run tune car function on click
    ui.btnTuneCar.clicked.connect(guiTuneCar)

    sys.exit(app.exec_())
