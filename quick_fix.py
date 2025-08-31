#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
快速修复Git配置
"""

import os
import subprocess

def quick_fix():
    """快速修复Git配置"""
    print("=" * 60)
    print("GitNote 快速修复")
    print("=" * 60)
    
    notes_dir = os.path.expanduser("~/.GitNote/Notes")
    
    if not os.path.exists(notes_dir):
        print("❌ Notes目录不存在")
        return
    
    try:
        os.chdir(notes_dir)
        
        # 1. 检查并修复 fetch refspec
        print("\n1. 修复 fetch refspec...")
        try:
            result = subprocess.run(['git', 'config', '--get', 'remote.origin.fetch'], 
                                  capture_output=True, text=True)
            if not result.stdout.strip():
                print("   正在设置 fetch refspec...")
                subprocess.run(['git', 'config', '--add', 'remote.origin.fetch', 
                              '+refs/heads/*:refs/remotes/origin/*'], 
                              check=True)
                print("   ✅ fetch refspec 设置成功")
            else:
                print("   ✅ fetch refspec 已配置")
        except Exception as e:
            print(f"   ⚠ 设置 fetch refspec 时出错: {e}")
        
        # 2. 检查远程仓库名
        print("\n2. 检查远程仓库配置...")
        result = subprocess.run(['git', 'remote'], capture_output=True, text=True)
        remotes = result.stdout.strip().split('\n') if result.stdout.strip() else []
        
        if 'origin' not in remotes and 'gitee' in remotes:
            print("   检测到 'gitee' 远程仓库名，添加 'origin' 别名...")
            subprocess.run(['git', 'remote', 'add', 'origin', 'git@gitee.com:happy-sf/git-note.git'], 
                          check=True)
            print("   ✅ origin 别名添加成功")
        
        # 3. 测试 fetch
        print("\n3. 测试远程连接...")
        try:
            result = subprocess.run(['git', 'fetch', 'origin'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print("   ✅ 远程连接正常")
            else:
                print(f"   ⚠ fetch 可能有问题: {result.stderr}")
        except Exception as e:
            print(f"   ❌ fetch 失败: {e}")
        
        # 4. 显示当前状态
        print("\n4. 当前状态：")
        try:
            result = subprocess.run(['git', 'status', '-sb'], 
                                  capture_output=True, text=True)
            print(f"   {result.stdout.strip()}")
        except Exception as e:
            print(f"   ❌ 获取状态失败: {e}")
        
        print("\n🎉 修复完成！")
        print("现在可以正常使用GitNote的同步功能了。")
        
    except Exception as e:
        print(f"❌ 修复失败: {e}")
    
    print("\n按回车键退出...")
    input()

if __name__ == '__main__':
    quick_fix()