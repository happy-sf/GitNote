#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
配置Git远程仓库脚本
"""

import os
import subprocess
import sys

def setup_git_remote():
    """配置Git远程仓库"""
    # 获取Git仓库路径
    home_dir = os.path.expanduser("~")
    git_repo = os.path.join(home_dir, ".GitNote", "notes")
    
    if not os.path.exists(git_repo):
        print("❌ Git仓库不存在，请先运行 run_gitnote.py 初始化")
        return False
    
    # 远程仓库URL
    remote_url = "git@gitee.com:happy-sf/git-note.git"
    
    try:
        # 切换到仓库目录
        os.chdir(git_repo)
        
        # 检查是否已有远程仓库
        result = subprocess.run(['git', 'remote', '-v'], 
                              capture_output=True, text=True)
        
        if 'origin' in result.stdout:
            print("✅ 远程仓库 'origin' 已存在")
            print("当前配置：")
            print(result.stdout)
            
            # 询问是否要更新
            update = input("\n是否要更新远程仓库地址？(y/N): ")
            if update.lower() == 'y':
                subprocess.run(['git', 'remote', 'set-url', 'origin', remote_url])
                print("✅ 远程仓库地址已更新")
        else:
            # 添加远程仓库
            print(f"正在添加远程仓库: {remote_url}")
            subprocess.run(['git', 'remote', 'add', 'origin', remote_url])
            print("✅ 远程仓库添加成功")
        
        # 测试连接
        print("\n正在测试连接...")
        result = subprocess.run(['git', 'ls-remote', 'origin'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ 远程仓库连接成功！")
            print("\n您现在可以使用GitNote的同步功能了！")
            return True
        else:
            print("❌ 远程仓库连接失败")
            print("请检查：")
            print("1. SSH密钥是否已配置")
            print("2. 网络连接是否正常")
            print("3. 仓库地址是否正确")
            return False
            
    except Exception as e:
        print(f"❌ 配置失败: {e}")
        return False

if __name__ == '__main__':
    print("=" * 60)
    print("GitNote 远程仓库配置工具")
    print("=" * 60)
    print("\n将配置远程仓库：git@gitee.com:happy-sf/git-note.git")
    print("\n注意：请确保您已：")
    print("1. 生成并配置了SSH密钥")
    print("2. 在Gitee上创建了该仓库")
    print("3. 拥有仓库的推送权限")
    
    input("\n按回车键继续，Ctrl+C 取消...")
    
    if setup_git_remote():
        print("\n🎉 配置成功！")
    else:
        print("\n💡 配置失败，请检查后重试")
    
    input("\n按回车键退出...")