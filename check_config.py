#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
检查和修复GitNote配置
"""

import os
import json
import subprocess

def check_git_note_config():
    """检查GitNote的配置"""
    print("=" * 60)
    print("GitNote 配置检查")
    print("=" * 60)
    
    # 检查实际的Git仓库位置
    actual_git_repo = os.path.expanduser("~/.GitNote")
    notes_dir = os.path.join(actual_git_repo, "Notes")
    
    print(f"\n1. 检查Git仓库位置：")
    print(f"   期望位置: {notes_dir}")
    
    if os.path.exists(notes_dir):
        print(f"   ✅ 目录存在")
        
        # 检查是否是Git仓库
        git_dir = os.path.join(notes_dir, '.git')
        if os.path.exists(git_dir):
            print(f"   ✅ Git仓库存在")
            
            # 检查远程仓库配置
            try:
                os.chdir(notes_dir)
                result = subprocess.run(['git', 'remote', '-v'], 
                                      capture_output=True, text=True)
                if result.stdout:
                    print(f"   ✅ 远程仓库配置：")
                    for line in result.stdout.strip().split('\n'):
                        if line.strip():
                            print(f"      {line}")
                        
                        # 检查是否是gitee仓库
                        if 'gitee.com' in line:
                            print(f"   ✅ 正确配置了Gitee仓库")
                            
                else:
                    print(f"   ⚠ 未配置远程仓库")
            except Exception as e:
                print(f"   ❌ 检查远程仓库失败: {e}")
            
            # 检查分支
            try:
                result = subprocess.run(['git', 'branch'], 
                                      capture_output=True, text=True)
                if result.stdout:
                    current_branch = None
                    for line in result.stdout.strip().split('\n'):
                        if line.strip().startswith('* '):
                            current_branch = line.strip()[2:]
                            print(f"   ✅ 当前分支: {current_branch}")
                            break
                    
                    if current_branch:
                        # 检查上游分支
                        result = subprocess.run(['git', 'status', '--porcelain'], 
                                              capture_output=True, text=True)
                        if "no upstream branch" in result.stderr:
                            print(f"   ⚠ 分支 {current_branch} 没有上游分支")
                            print(f"   💡 运行 git push --set-upstream origin {current_branch}")
            except Exception as e:
                print(f"   ❌ 检查分支失败: {e}")
        else:
            print(f"   ❌ 不是Git仓库")
    else:
        print(f"   ❌ 目录不存在")
    
    # 检查GitNote程序配置
    print(f"\n2. 检查GitNote程序配置：")
    config_file = os.path.join(actual_git_repo, "config.json")
    if os.path.exists(config_file):
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
            print(f"   ✅ 配置文件存在")
            print(f"   主题: {config.get('theme', 'white')}")
            if 'font' in config:
                print(f"   字体: 已自定义")
        except Exception as e:
            print(f"   ❌ 读取配置文件失败: {e}")
    else:
        print(f"   ⚠ 配置文件不存在")
    
    # 检查Notes目录
    print(f"\n3. 检查Notes目录：")
    notes_path = os.path.expanduser("~/Notes")
    if os.path.exists(notes_path):
        print(f"   ✅ ~/Notes 目录存在")
        # 检查是否有内容
        if os.listdir(notes_path):
            print(f"   ℹ ~/Notes 目录包含文件，但GitNote使用 ~/.GitNote/notes")
    
    print(f"\n4. 建议的修复方案：")
    
    # 如果需要，设置上游分支
    try:
        os.chdir(notes_dir)
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True)
        if "no upstream branch" in result.stderr:
            print(f"   - 运行: git push --set-upstream origin master")
    except:
        pass
    
    print(f"\n按回车键退出...")
    input()

if __name__ == '__main__':
    check_git_note_config()