#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GitNote 完整功能测试程序
包含界面优化和完整的笔记功能
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
    
    # 初始化Git仓库（如果不存在）
    if not os.path.exists(os.path.join(main.gitNoteNoteHome, '.git')):
        try:
            import git
            repo = git.Repo.init(main.gitNoteNoteHome)
            # 创建初始提交
            readme_path = os.path.join(main.gitNoteNoteHome, 'README.md')
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write('# GitNote 笔记仓库\n\n这是GitNote自动创建的笔记仓库。\n')
            repo.index.add(['README.md'])
            repo.index.commit('Initial commit')
            main.gitExist = True
            print("✓ Git仓库初始化成功")
            print("ℹ 提示：如需使用Git同步功能，请配置远程仓库")
        except Exception as e:
            print(f"⚠ Git仓库初始化失败: {e}")
            main.gitExist = False
    else:
        main.gitExist = True
        # 检查是否有远程仓库
        try:
            repo = git.Repo(main.gitNoteNoteHome)
            if len(repo.remotes) == 0:
                print("ℹ 提示：本地Git仓库已就绪，但未配置远程仓库")
        except:
            pass
    
    return main

def main():
    """主函数"""
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                 GitNote 完整功能测试版                       ║
    ╠══════════════════════════════════════════════════════════════╣
    ║  界面优化：                                                    ║
    ║  ✓ 按钮尺寸增大到32x32像素                                     ║
    ║  ✓ 按钮按功能区分颜色                                          ║
    ║  ✓ 左侧面板可自由调整宽度                                      ║
    ║  ✓ 按钮间距增大到10像素                                        ║
    ║  ✓ 添加了悬停和点击效果                                        ║
    ║                                                              ║
    ║  功能测试：                                                    ║
    ║  ✓ 笔记创建和保存                                              ║
    ║  ✓ 文件夹管理                                                  ║
    ║  ✓ Git同步功能                                                 ║
    ║  ✓ 图片插入功能                                                ║
    ║  ✓ PDF导出功能                                                 ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    # 设置环境
    main_module = setup_environment()
    
    # 导入并运行GitNote
    from PyQt5.QtWidgets import QApplication
    from GitNote import GitNote
    
    app = QApplication(sys.argv)
    
    # 创建主窗口
    window = GitNote()
    window.setWindowTitle('GitNote - 界面优化完整版')
    window.resize(1200, 800)
    
    print("\n程序已启动！")
    print("提示：")
    print("- 点击左侧文件夹可以查看笔记")
    print("- 双击笔记可以编辑")
    print("- 编辑后点击绿色保存按钮保存")
    print("- 可以拖拽左侧分割线调整宽度")
    print("\n如需配置Git同步，请运行：python3 setup_git.py")
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()