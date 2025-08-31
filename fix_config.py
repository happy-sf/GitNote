#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
修复GitNote配置
"""

import os
import subprocess

def fix_gitnote_config():
    """修复GitNote配置"""
    print("=" * 60)
    print("GitNote 配置修复工具")
    print("=" * 60)
    
    # 获取正确的路径
    notes_dir = os.path.expanduser("~/.GitNote/Notes")
    
    if not os.path.exists(notes_dir):
        print("❌ GitNote笔记目录不存在")
        print("请先运行 run_gitnote.py 初始化")
        return
    
    try:
        # 切换到笔记目录
        os.chdir(notes_dir)
        
        # 检查当前分支
        result = subprocess.run(['git', 'branch'], 
                              capture_output=True, text=True)
        current_branch = None
        for line in result.stdout.strip().split('\n'):
            if line.strip().startswith('* '):
                current_branch = line.strip()[2:]
                break
        
        if not current_branch:
            print("❌ 无法确定当前分支")
            return
        
        print(f"当前分支: {current_branch}")
        
        # 检查是否有上游分支
        print("\n正在检查上游分支...")
        result = subprocess.run(['git', 'push', '--dry-run', 'origin', current_branch], 
                              capture_output=True, text=True)
        
        if "no upstream branch" in result.stderr or "has no upstream branch" in result.stderr:
            print("⚠ 没有上游分支，正在设置...")
            
            # 设置上游分支并推送
            result = subprocess.run(['git', 'push', '--set-upstream', 'origin', current_branch], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ 上游分支设置成功！")
            else:
                print(f"❌ 设置失败: {result.stderr}")
        else:
            print("✅ 上游分支已正确配置")
        
        # 测试同步
        print("\n正在测试同步...")
        result = subprocess.run(['git', 'fetch', 'origin'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ 可以正常获取远程更新")
            
            # 检查是否有本地提交需要推送
            result = subprocess.run(['git', 'log', '--oneline', 'origin/' + current_branch + '..HEAD'], 
                                  capture_output=True, text=True)
            if result.stdout.strip():
                print(f"ℹ 有 {len(result.stdout.strip().split(chr(10)))} 个本地提交需要推送")
            
            # 检查是否有远程更新需要拉取
            result = subprocess.run(['git', 'log', '--oneline', 'HEAD..' + current_branch], 
                                  capture_output=True, text=True)
            if result.stdout.strip():
                print(f"ℹ 有 {len(result.stdout.strip().split(chr(10)))} 个远程更新需要拉取")
        else:
            print(f"❌ 同步测试失败: {result.stderr}")
        
        print("\n🎉 修复完成！")
        print("现在您可以正常使用GitNote的同步功能了！")
        
    except Exception as e:
        print(f"❌ 修复失败: {e}")
    
    print("\n按回车键退出...")
    input()

if __name__ == '__main__':
    fix_gitnote_config()