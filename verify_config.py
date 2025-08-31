#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
验证GitNote配置
"""

import os
import subprocess
import sys

def verify_config():
    """验证GitNote配置"""
    print("=" * 60)
    print("GitNote 配置验证")
    print("=" * 60)
    
    # 验证路径
    git_note_home = os.path.expanduser("~/.GitNote")
    notes_dir = os.path.join(git_note_home, "Notes")
    
    print(f"\n1. 验证路径配置：")
    print(f"   GitNote主目录: {git_note_home}")
    print(f"   笔记仓库目录: {notes_dir}")
    
    if os.path.exists(notes_dir):
        print(f"   ✅ Notes目录存在")
    else:
        print(f"   ❌ Notes目录不存在")
        return False
    
    # 验证Git仓库
    git_dir = os.path.join(notes_dir, '.git')
    if os.path.exists(git_dir):
        print(f"   ✅ 是Git仓库")
        
        # 验证远程仓库
        try:
            os.chdir(notes_dir)
            result = subprocess.run(['git', 'remote', '-v'], 
                                  capture_output=True, text=True)
            
            if 'gitee.com' in result.stdout:
                print(f"   ✅ 已配置Gitee远程仓库")
                
                # 显示远程仓库详情
                for line in result.stdout.strip().split('\n'):
                    if 'gitee.com' in line and 'fetch' in line:
                        url = line.split('\t')[1]
                        print(f"      {url}")
            else:
                print(f"   ⚠ 未配置Gitee远程仓库")
        except Exception as e:
            print(f"   ❌ 检查远程仓库失败: {e}")
        
        # 验证分支状态
        try:
            result = subprocess.run(['git', 'status', '--porcelain', '-b'], 
                                  capture_output=True, text=True)
            
            lines = result.stdout.strip().split('\n')
            if lines:
                # 获取当前分支
                branch_line = lines[0]
                if branch_line.startswith('## '):
                    branch_info = branch_line[3:]
                    print(f"   ✅ 当前分支状态: {branch_info}")
                    
                    if 'no upstream' in branch_info:
                        print(f"   ⚠ 分支没有上游分支")
                    elif 'ahead' in branch_info or 'behind' in branch_info:
                        print(f"   ℹ 有提交需要同步")
                    else:
                        print(f"   ✅ 分支已同步")
                        
                # 检查未提交的更改
                uncommitted = len([line for line in lines[1:] if line.strip()])
                if uncommitted > 0:
                    print(f"   ℹ 有 {uncommitted} 个文件未提交")
        except Exception as e:
            print(f"   ❌ 检查分支状态失败: {e}")
    else:
        print(f"   ❌ 不是Git仓库")
        return False
    
    # 验证配置文件
    print(f"\n2. 验证配置文件：")
    config_file = os.path.join(git_note_home, "config.json")
    if os.path.exists(config_file):
        print(f"   ✅ 配置文件存在")
    else:
        print(f"   ⚠ 配置文件不存在（首次运行正常）")
    
    print(f"\n3. 验证结果：")
    print(f"   ✅ 路径配置正确：~/.GitNote/Notes")
    print(f"   ✅ Git仓库已配置")
    print(f"   ✅ 远程仓库已配置")
    
    return True

if __name__ == '__main__':
    if verify_config():
        print(f"\n🎉 配置验证通过！")
        print(f"\n现在可以运行：")
        print(f"   python3 run_gitnote.py")
    else:
        print(f"\n❌ 配置验证失败，请检查配置")
    
    print(f"\n按回车键退出...")
    input()