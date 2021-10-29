/*类的实现*/
#include "mainwindow.h"
#include "ui_mainwindow.h"//qt根据.ui文件自动生成的

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);//进行界面初始化
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pushButton_clicked()
{
    this->close();
}
