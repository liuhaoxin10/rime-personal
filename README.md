# 我的 Rime 词库与方案

基于[雾凇拼音](https://github.com/iDvel/rime-ice)。电脑26键全拼与紫毫手机九键使用两套独立的完整方案，只共用四套个人专题词条。

| 用途 | GitHub 配置目录 | 方案 |
| --- | --- | --- |
| 电脑26键全拼 | 根目录 | 保留首次发布前的电脑配置，只启用 `rime_ice`；保留原置顶与容错设置 |
| 紫毫手机九键 | [`mobile/`](mobile/) | 独立完整手机方案：紫毫官方雾凇基线＋手机九键适配＋个人词库 |

## 手机导入与远程更新

在紫毫添加一套独立的 GitHub 方案：

- 仓库：`https://github.com/liuhaoxin10/rime-personal`
- 分支：`main`
- **配置目录：`mobile`**

部署并启用后使用九键。以后通过该方案的「立即更新」或定时更新取得新版本。原先导入根目录的是电脑方案，手机请使用独立的 `mobile` 目录。

也可下载[完整手机方案 ZIP](https://github.com/liuhaoxin10/rime-personal/releases/latest/download/rime-personal.zip)导入；ZIP解压后直接是方案文件，没有外层目录。

## 两套配置的边界

电脑根目录的75个原始运行时源文件已与首次发布前的版本逐字节比对，保持一致。手机更改只编辑 `mobile/`，不改变电脑的键盘、方案菜单、置顶、容错或学习记录。

手机方案以[紫毫官方公开的雾凇版本和适配配置](https://hareime.com/rime-ice)为基础，包含方案、基础词库、英文资源、Lua与OpenCC。保留手机原生词典名称 `rime_ice`，基础词表和个人词条共同参与排序。手机中文词表已更新到雾凇官方 `da1fbe6`（2026-10-05），具体来源及验证见 [mobile/README.md](mobile/README.md)。电脑继续使用原来的 `custom_rime_ice` 组合词典。

四套共用个人词库：编程与计算机93条、数据结构与算法75条、AI与机器学习146条、数学131条，共445条。手机快捷短语 `mobile/personal_phrase_t9.txt` 另将 `444` 优先设为「哈哈哈」。

用户学习记录由各设备保存。公开仓库不包含 `*.userdb`、同步数据、备份、编译结果或本机安装信息。

## 更新与打包

修改个人专题词库后，只同步这四份词条文件，再生成手机包：

```sh
python3 tools/sync_mobile_dictionary.py
python3 tools/package.py --profile mobile
```

输出为 `dist/rime-personal.zip`。同步脚本不复制电脑的基础词库、`.schema.yaml` 或 `.custom.yaml`，手机方案基线独立维护。

电脑完整源码另行打包：

```sh
python3 tools/package.py --profile desktop --output dist/rime-desktop.zip
```

提交并推送后，GitHub目录订阅才能取得新内容；ZIP用户还需要发布新的Release。

## 已知限制

紫毫内置九键对完整输入也可能发生整句判断错误。本方案会与相同手机基线做按键对照，但不承诺消除客户端的全部整句误判。此前试验的通用语法模型没有稳定改善，未捆绑发布。可在输入时用「选拼音」锁定音节或分段选词。

保留上游作者署名与 [GPLv3 LICENSE](LICENSE)。
