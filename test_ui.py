#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
测试GitNote界面优化效果
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtWidgets import QApplication
from GitNote import GitNote
import main

if __name__ == '__main__':
    # 初始化主应用
    app = QApplication(sys.argv)
    
    # 设置基本参数
    main.gitNoteHome = os.path.expanduser("~/.GitNote")
    main.gitNoteNoteHome = os.path.join(main.gitNoteHome, "notes")
    main.gitExist = True
    
    # 创建必要的目录
    os.makedirs(main.gitNoteHome, exist_ok=True)
    os.makedirs(main.gitNoteNoteHome, exist_ok=True)
    
    # 创建并显示窗口
    window = GitNote()
    window.setWindowTitle('GitNote - 界面优化测试版')
    window.resize(1200, 800)
    
    print("""
    GitNote 界面优化已完成：
    
    ✓ 按钮尺寸已从 16x16/20x20 增大到 32x32
    ✓ 左侧面板（目录树和笔记列表）已移除最大宽度限制
    ✓ 按钮已添加不同颜色：
      - 更新按钮：蓝色系
      - 保存按钮：绿色系  
      - 添加图片按钮：橙色系
      - 配置按钮：灰色系
      - 功能按钮：紫色系
    ✓ 按钮间距已增加到10像素
    ✓ 所有按钮都添加了悬停和点击效果
    
    界面现在更加美观且易于操作！
    """)
    
    sys.exit(app.exec_())