# 我的 Rime 词库

基于[雾凇拼音](https://github.com/iDvel/rime-ice)的个人词库。电脑全拼与紫毫手机九键使用独立配置，只同步词库数据。

| 用途 | 位置 | 配置 |
| --- | --- | --- |
| 电脑 26 键全拼 | 仓库根目录 | 保留发布前的电脑配置，只启用 `rime_ice`，保留原置顶与容错设置 |
| 紫毫手机九键 | [`mobile/`](mobile/) | 仅叠加词库和手机快捷短语，使用紫毫自带的键盘、九键算法和整句模型 |

## 紫毫手机订阅

- 仓库：`https://github.com/liuhaoxin10/rime-personal`
- 分支：`main`
- **配置目录：`mobile`**

此前订阅根目录的手机，请将配置目录改为 `mobile`，更新后部署并启用。手机不再导入电脑的 `default.custom.yaml`、方案文件、置顶规则或键盘设置。

[最新手机词库 ZIP](https://github.com/liuhaoxin10/rime-personal/releases/latest/download/rime-personal.zip)同样只包含手机词库覆盖层，依赖紫毫先部署其内置雾凇资源。不是独立的完整 Rime 方案。参见[手机目录说明](mobile/README.md)、[紫毫导入说明](https://hareime.com/guide)。

## 词库内容

组合词库为 `custom_rime_ice`，包含当前雾凇中文词表及四套个人专题词库：编程与计算机 93 条、数据结构与算法 75 条、AI 与机器学习 146 条、数学 131 条，共 445 条。

电脑与手机的词库条目一致，个人学习记录分别由各设备保存。公开仓库不保存 `*.userdb`、同步数据、备份、编译结果或本机安装信息。

手机快捷短语保存在 `mobile/personal_phrase_t9.txt`，目前将 `444` 优先设为「哈哈哈」。它不修改电脑候选或任何其他整句的排序。

## 九键整句准确率的已知限制

完整输入「这很贵了」时，本机 Rime 九键和紫毫内置方案对照均出现不合适的整句候选。仅去除模糊规则、关闭补全或接入八股文通用模型，均未稳定修复。因此本仓库不捆绑实验模型或未经验证的九键调参，也不承诺词库覆盖层可以修复客户端全部整句问题。可用「选拼音」锁定音节或分段选词。

## 更新与打包

修改根目录的词库后，以下命令只同步词库数据到手机目录，再生成手机导入包：

```sh
python3 tools/sync_mobile_dictionary.py
python3 tools/package.py --profile mobile
```

手机包输出为 `dist/rime-personal.zip`。电脑完整源码可另外打包：

```sh
python3 tools/package.py --profile desktop --output dist/rime-desktop.zip
```

更新手机配置只编辑 `mobile/`；更新电脑配置只编辑根目录。同步脚本不复制 `.schema.yaml` 或 `.custom.yaml`。提交并推送后，GitHub 目录订阅才能获取新内容；ZIP 用户还需要发布新 Release。

保留上游作者署名与 [GPLv3 LICENSE](LICENSE)。
