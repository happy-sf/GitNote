#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GitNote界面优化演示 - 简化版
只展示界面优化效果，不涉及Git功能
"""

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QToolButton, QLineEdit, QSplitter, QTreeWidget, QListWidget, QPlainTextEdit, QTextEdit
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize

class GitNoteDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('GitNote 界面优化演示')
        self.resize(1200, 800)
        
        # 主布局
        main_layout = QVBoxLayout(self)
        
        # 顶部工具栏
        top_layout = QHBoxLayout()
        top_layout.setSpacing(10)
        
        # 更新按钮 - 蓝色
        self.update_btn = QPushButton()
        self.update_btn.setIconSize(QSize(32, 32))
        self.update_btn.setStyleSheet("""
            QPushButton {
                border: 2px solid #0052a3;
                border-radius: 8px;
                padding: 5px;
                min-width: 40px;
                min-height: 40px;
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #4da6ff, stop:1 #0066cc);
            }
            QPushButton:hover {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #66b3ff, stop:1 #0073e6);
                border-color: #0066cc;
            }
        """)
        
        # 配置按钮 - 灰色
        self.config_btn = QToolButton()
        self.config_btn.setIconSize(QSize(32, 32))
        self.config_btn.setStyleSheet("""
            QToolButton {
                border: 2px solid #424242;
                border-radius: 8px;
                padding: 5px;
                min-width: 40px;
                min-height: 40px;
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #9e9e9e, stop:1 #616161);
            }
            QToolButton:hover {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #bdbdbd, stop:1 #757575);
            }
        """)
        
        top_layout.addWidget(self.update_btn)
        top_layout.addStretch()
        top_layout.addWidget(self.config_btn)
        
        # 主要分割器
        splitter = QSplitter(Qt.Horizontal)
        
        # 左侧面板
        left_splitter = QSplitter(Qt.Horizontal)
        
        # 目录树
        self.tree = QTreeWidget()
        self.tree.setHeaderHidden(True)
        self.tree.setMinimumWidth(10)
        # 注意：这里没有设置maximumWidth，所以可以自由调整
        
        # 笔记列表
        self.list = QListWidget()
        self.list.setMinimumWidth(10)
        # 注意：这里没有设置maximumWidth，所以可以自由调整
        
        left_splitter.addWidget(self.tree)
        left_splitter.addWidget(self.list)
        
        # 右侧编辑区
        editor_widget = QWidget()
        editor_layout = QVBoxLayout(editor_widget)
        
        # 编辑工具栏
        edit_toolbar = QHBoxLayout()
        edit_toolbar.setSpacing(10)
        
        # 保存按钮 - 绿色
        self.save_btn = QPushButton()
        self.save_btn.setIconSize(QSize(32, 32))
        self.save_btn.setStyleSheet("""
            QPushButton {
                border: 2px solid #398439;
                border-radius: 8px;
                padding: 5px;
                min-width: 40px;
                min-height: 40px;
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #5cb85c, stop:1 #449d44);
            }
            QPushButton:hover {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #6fc86c, stop:1 #4cae4c);
            }
        """)
        
        # 标题输入框
        self.title_edit = QLineEdit()
        self.title_edit.setReadOnly(True)
        self.title_edit.setPlaceholderText("笔记标题")
        
        # 添加图片按钮 - 橙色
        self.add_pic_btn = QPushButton()
        self.add_pic_btn.setIconSize(QSize(32, 32))
        self.add_pic_btn.setStyleSheet("""
            QPushButton {
                border: 2px solid #d58512;
                border-radius: 8px;
                padding: 5px;
                min-width: 40px;
                min-height: 40px;
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #f0ad4e, stop:1 #ec971f);
            }
            QPushButton:hover {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #f2c690, stop:1 #eea236);
            }
        """)
        
        # 功能按钮 - 紫色
        self.func_btn = QToolButton()
        self.func_btn.setIconSize(QSize(32, 32))
        self.func_btn.setStyleSheet("""
            QToolButton {
                border: 2px solid #6a1b9a;
                border-radius: 8px;
                padding: 5px;
                min-width: 40px;
                min-height: 40px;
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ba68c8, stop:1 #8e24aa);
            }
            QToolButton:hover {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ce93d8, stop:1 #ab47bc);
            }
        """)
        
        edit_toolbar.addWidget(self.save_btn)
        edit_toolbar.addWidget(self.title_edit)
        edit_toolbar.addWidget(self.add_pic_btn)
        edit_toolbar.addWidget(self.func_btn)
        
        # 编辑区域
        edit_area = QHBoxLayout()
        self.markdown_edit = QPlainTextEdit()
        self.markdown_edit.setPlaceholderText("Markdown 编辑区")
        self.preview_edit = QTextEdit()
        self.preview_edit.setReadOnly(True)
        self.preview_edit.setPlaceholderText("预览区")
        
        edit_area.addWidget(self.markdown_edit)
        edit_area.addWidget(self.preview_edit)
        
        editor_layout.addLayout(edit_toolbar)
        editor_layout.addLayout(edit_area)
        
        # 添加到分割器
        splitter.addWidget(left_splitter)
        splitter.addWidget(editor_widget)
        
        # 设置分割器比例
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 3)
        
        # 添加到主布局
        main_layout.addLayout(top_layout)
        main_layout.addWidget(splitter)
        
        # 设置一些示例图标（如果存在）
        icon_path = os.path.dirname(os.path.abspath(__file__))
        try:
            if os.path.exists(os.path.join(icon_path, "loading.png")):
                self.update_btn.setIcon(QIcon(os.path.join(icon_path, "loading.png")))
            if os.path.exists(os.path.join(icon_path, "config.ico")):
                self.config_btn.setIcon(QIcon(os.path.join(icon_path, "config.ico")))
            if os.path.exists(os.path.join(icon_path, "edit.ico")):
                self.save_btn.setIcon(QIcon(os.path.join(icon_path, "edit.ico")))
            if os.path.exists(os.path.join(icon_path, "addpicture.png")):
                self.add_pic_btn.setIcon(QIcon(os.path.join(icon_path, "addpicture.png")))
            if os.path.exists(os.path.join(icon_path, "convert.ico")):
                self.func_btn.setIcon(QIcon(os.path.join(icon_path, "convert.ico")))
        except:
            pass
        
        # 添加示例内容
        self.tree.addTopLevelItem(self.createTreeItem("文件夹1"))
        self.tree.addTopLevelItem(self.createTreeItem("文件夹2"))
        self.list.addItem("笔记1.md")
        self.list.addItem("笔记2.md")
        
    def createTreeItem(self, name):
        from PyQt5.QtWidgets import QTreeWidgetItem
        item = QTreeWidgetItem([name])
        return item

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # 设置应用样式
    app.setStyle('Fusion')
    
    window = GitNoteDemo()
    window.show()
    
    print("""
    ╔══════════════════════════════════════════════════════════════╗
   ║                GitNote 界面优化演示                            ║
    ╠══════════════════════════════════════════════════════════════╣
    ║  ✓ 按钮尺寸已增大到32x32像素                                 ║
    ║  ✓ 左侧面板可以自由拖拽调整宽度（已移除宽度限制）               ║
    ║  ✓ 按钮颜色区分：                                             ║
    ║    - 蓝色：更新按钮                                           ║
    ║    - 绿色：保存按钮                                           ║
    ║    - 橙色：添加图片按钮                                       ║
    ║    - 灰色：配置按钮                                           ║
    ║    - 紫色：功能按钮                                           ║
    ║  ✓ 按钮间距增加到10像素                                       ║
    ║  ✓ 所有按钮都有悬停效果                                       ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    sys.exit(app.exec_())