#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
测试左侧面板宽度设置
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def setup_environment():
    """设置GitNote运行环境"""
    import main
    
    # 设置基本路径
    main.gitNoteHome = os.path.expanduser("~/.GitNote")
    main.gitNoteNoteHome = os.path.join(main.gitNoteHome, "Notes")
    
    # 创建必要的目录
    os.makedirs(main.gitNoteHome, exist_ok=True)
    os.makedirs(main.gitNoteNoteHome, exist_ok=True)
    
    # 创建配置文件
    config_file = os.path.join(main.gitNoteHome, "config.json")
    if not os.path.exists(config_file):
        import json
        with open(config_file, 'w') as f:
            json.dump({'theme': 'white'}, f)
    
    main.gitExist = True
    return main

def main():
    """主函数"""
    print("=" * 60)
    print("测试左侧面板宽度设置")
    print("=" * 60)
    print("\n修改内容：")
    print("- 左侧面板总宽度占比：25%（之前约50%）")
    print("- 目录树宽度：左侧的60%")
    print("- 笔记列表宽度：左侧的40%")
    print("- 右侧编辑区：75%")
    print("\n现在启动程序...")
    
    # 设置环境
    main_module = setup_environment()
    
    # 导入并运行GitNote
    from PyQt5.QtWidgets import QApplication
    from GitNote import GitNote
    
    app = QApplication(sys.argv)
    
    # 创建主窗口
    window = GitNote()
    window.setWindowTitle('GitNote - 左侧宽度优化测试版')
    window.resize(1200, 800)
    
    print("\n✅ 程序已启动！")
    print("检查左侧面板宽度是否合适...")
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()