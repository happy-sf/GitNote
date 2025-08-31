# GitNote 使用说明

## 快速开始

### 1. 运行程序
```bash
python3 run_gitnote.py
```

### 2. 配置Git同步（可选）
如需使用云同步功能，按顺序运行：
```bash
# 1. 验证配置
python3 verify_config.py

# 2. 如果需要配置远程仓库
python3 setup_git.py

# 3. 如果需要修复分支配置
python3 fix_config.py
```

**注意**：GitNote 使用 `~/.GitNote/Notes`（大写N）作为笔记存储目录

## 问题已修复

✅ **mistune版本兼容性问题** - 已适配mistune 3.x版本
✅ **Git远程仓库错误** - 添加了异常处理
✅ **按钮样式与功能冲突** - 修复后不影响正常使用

## 功能说明

### 界面优化
- 按钮尺寸：32x32像素，更易点击
- 颜色区分：
  - 🔵 蓝色：更新/同步
  - 🟢 绿色：保存笔记
  - 🟠 橙色：插入图片
  - ⚫ 灰色：配置选项
  - 🟣 紫色：导出PDF
- 左侧面板可自由拖拽调整宽度

### 基本功能
- ✅ 创建、编辑、保存笔记
- ✅ 文件夹管理
- ✅ Markdown实时预览
- ✅ 图片插入
- ✅ 本地Git版本控制
- ✅ PDF导出

### Git同步功能
- ✅ 本地仓库自动初始化
- ⚠️ 远程同步需要手动配置

## 常见问题

**Q: 程序可以运行，但同步失败？**
A: 运行 `python3 setup_git.py` 配置远程仓库

**Q: 配置SSH密钥？**
A: 参考 Gitee 官方文档：https://gitee.com/help/articles/4181

**Q: 修改远程仓库地址？**
A: 在 ~/.GitNote/notes 目录下运行：
```bash
git remote set-url origin git@gitee.com:happy-sf/git-note.git
```

## 项目结构
```
GitNote/
├── main.py              # 原始主程序
├── run_gitnote.py       # 优化版运行程序
├── setup_git.py         # Git配置工具
├── GitNote.py           # 主程序逻辑
├── GitNote.ui           # 界面设计文件
├── GitNoteUi.py         # 编译后的界面文件
└── 界面优化说明.md       # 优化详情说明
```