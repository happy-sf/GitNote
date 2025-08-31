#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
配置GitNote远程仓库脚本
自动配置Gitee远程仓库
"""

import os
import subprocess
import sys

def setup_remote_repo():
    """设置远程仓库"""
    # 获取GitNote仓库路径
    git_note_home = os.path.expanduser("~/.GitNote/notes")
    
    print("正在配置GitNote远程仓库...")
    print(f"仓库路径: {git_note_home}")
    print(f"远程地址: git@gitee.com:happy-sf/git-note.git")
    print("-" * 50)
    
    # 检查仓库是否存在
    if not os.path.exists(os.path.join(git_note_home, '.git')):
        print("❌ 本地Git仓库不存在，请先运行一次GitNote")
        return False
    
    try:
        # 切换到仓库目录
        os.chdir(git_note_home)
        
        # 检查是否已配置远程仓库
        result = subprocess.run(['git', 'remote', '-v'], 
                              capture_output=True, text=True)
        
        if 'origin' in result.stdout:
            print("ℹ 检测到已配置的远程仓库：")
            print(result.stdout)
            overwrite = input("是否要覆盖？(y/N): ")
            if overwrite.lower() != 'y':
                print("配置已取消")
                return True
        
        # 添加远程仓库
        print("正在添加远程仓库...")
        subprocess.run(['git', 'remote', 'add', 'origin', 
                       'git@gitee.com:happy-sf/git-note.git'], 
                       check=True)
        
        # 验证配置
        result = subprocess.run(['git', 'remote', '-v'], 
                              capture_output=True, text=True)
        
        print("\n✅ 远程仓库配置成功！")
        print("当前远程仓库配置：")
        print(result.stdout)
        
        # 测试连接
        print("\n正在测试连接...")
        test_result = subprocess.run(['git', 'ls-remote', 'origin'], 
                                   capture_output=True, text=True)
        
        if test_result.returncode == 0:
            print("✅ 连接成功！")
            print("\n📝 使用说明：")
            print("- 点击GitNote中的更新按钮即可同步")
            print("- 首次同步可能需要输入SSH密码")
            print("- 确保已配置SSH密钥到Gitee")
        else:
            print("⚠️ 连接测试失败，请检查：")
            print("1. SSH密钥是否已添加到Gitee")
            print("2. 网络连接是否正常")
            print("3. 仓库地址是否正确")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ 配置失败: {e}")
        return False
    except Exception as e:
        print(f"❌ 发生错误: {e}")
        return False

def setup_ssh_key():
    """提示设置SSH密钥"""
    print("\n" + "="*50)
    print("SSH密钥设置指南")
    print("="*50)
    print("""
如果没有SSH密钥，请按以下步骤设置：

1. 生成SSH密钥：
   ssh-keygen -t ed25519 -C "your_email@example.com"

2. 查看公钥：
   cat ~/.ssh/id_ed25519.pub

3. 将公钥添加到Gitee：
   - 登录Gitee
   - 进入 设置 -> SSH公钥
   - 复制公钥内容并添加

4. 测试连接：
   ssh -T git@gitee.com

    """)

if __name__ == '__main__':
    print("GitNote 远程仓库配置工具")
    print("="*50)
    
    # 检查git是否可用
    try:
        subprocess.run(['git', '--version'], check=True, 
                      capture_output=True)
    except:
        print("❌ 未找到git命令，请先安装git")
        sys.exit(1)
    
    # 配置远程仓库
    if setup_remote_repo():
        print("\n🎉 配置完成！")
        print("现在可以运行 'python3 run_gitnote.py' 使用GitNote了")
    else:
        print("\n❌ 配置失败")
        setup_ssh_key()