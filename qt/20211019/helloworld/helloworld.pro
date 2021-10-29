QT       += core gui#添加了qt的支持模块

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets#比较qt5版本，在main.cpp中application是在QTWidgets中的，因此要包含这个库

CONFIG += c++11#配置的是c++11

# The following define makes your compiler emit warnings if you use
# any Qt feature that has been marked deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
# 如果您使用任何被标记为已弃用的 Qt 功能，以下定义将使您的编译器发出警告（确切的警告取决于您的编译器）。 请查阅已弃用 API 的文档，以了解如何将您的代码从中移植
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if it uses deprecated APIs.如果您的代码使用已弃用的 API，您还可能使您的代码无法编译。   deprecated-> 已弃用
# In order to do so, uncomment the following line.为此，请取消注释以下行。
# You can also select to disable deprecated APIs only up to a certain version of Qt.您还可以选择仅禁用特定版本的 Qt 之前不推荐使用的 API。
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0禁用 Qt 6.0.0 之前弃用的所有 API
#c文件
SOURCES += \
    main.cpp \
    mainwindow.cpp
#头文件
HEADERS += \
    mainwindow.h
#ui界面文件
FORMS += \
    mainwindow.ui

# Default rules for deployment.部署默认的规则
#判断系统
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

#如果需要修改生成目标的可执行程序的名字，默认为项目名字
#TARGET = XXX
