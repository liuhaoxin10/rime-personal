# 我的 Rime 词库

基于 [雾凇拼音](https://github.com/iDvel/rime-ice) 的个人 Rime 配置，供电脑和支持 Rime 的手机输入法使用。此仓库保存当前本机方案及词库的源码快照，保留上游文件中的作者信息和 [LICENSE](LICENSE)。

## 手机下载与订阅

### 紫毫（当前使用的手机输入法）

GitHub 仓库填写 `https://github.com/liuhaoxin10/rime-personal`，使用默认分支 `main`，配置目录为根目录。已有订阅可在「方案 → 我的 RIME 方案 → 立即更新」拉取新配置，再回到键盘切换九键或 26 键。更新后如仍显示旧候选，切换到其他键盘再切回来。

本仓库已启用 `rime_ice` 全拼及 `t9` 九键，九键使用[紫毫官方公开的配置](https://hareime.com/rime-ice)，并挂载相同的个人词库。紫毫点按九键会输入数字编码，因此只切换成九键外观、却未启用 `t9` 方案时，无法正常进行中文九键输入。九键的中英混输依赖附带的 `melt_eng_t9.schema.yaml`。

### ZIP 导入

支持从网络下载 ZIP 方案的输入法，可以填写这个固定地址：

```text
https://github.com/liuhaoxin10/rime-personal/releases/latest/download/rime-personal.zip
```

- 仓输入法：下载 ZIP 后，通过「输入方案设置 → ＋ → 导入方案」导入，也可以通过系统分享交给仓。参见[官方说明](https://ihsiao.com/apps/hamster/docs/guides/input_schema/)。
- 元书输入法：在「输入方案 → 菜单 → 下载方案 → ＋」中填写上面的下载地址，文件名填写 `rime-personal.zip`，保存并下载，再切换到该方案目录。参见[官方说明](https://ihsiao.com/apps/hamster/v3/docs/guides/schema/)。
- 其他 Rime 输入法：使用应用提供的 ZIP 导入、网络下载或 Git 仓库功能。Git 仓库地址为 `https://github.com/liuhaoxin10/rime-personal`，分支为 `main`。导入后重新部署，并启用「雾凇拼音」。

Release 中的 ZIP 不含外层目录，解压后直接得到 Rime 配置文件。GitHub 的「Download ZIP」会多包一层目录，部分手机输入法不能直接导入。

这个地址提供已发布的最新版本；是否支持自动检查更新，取决于手机输入法。修改本机文件后，还需要提交到 GitHub 并发布新的 Release，手机才能取得更新。

## 当前配置

默认方案列表包含雾凇全拼和中文九键，全拼仍放在首位；两个方案的主词典均为 `custom_rime_ice`，包含原雾凇基础词库和四套个人专题词库：

| 词库 | 词条数 |
| --- | ---: |
| 编程与计算机 | 93 |
| 数据结构与算法 | 75 |
| AI 与机器学习 | 146 |
| 数学 | 131 |
| 合计 | 445 |

同时保留英文、中英混输、部件拆字、Emoji、Lua 功能、自定义短语，以及「公式」置顶和 `dain → dian` 的容错配置。需要支持 Lua 与 OpenCC 的 Rime 客户端。

个人词库补丁分别保存在 `rime_ice.custom.yaml`（全拼）和 `t9.custom.yaml`（九键）。仓库中的双拼文件保留原配置；如果要使用双拼，需要另行启用方案，并将其 `translator/dictionary` 设置为 `custom_rime_ice`。

发布前已在独立临时目录完成编译及真实按键测试：全拼 `nihao` →「你好」、`gongshi` →「公式」；九键 `42633` →「好的」、`64426` →「你好」、`73646649446364` →「人工智能」。手机端仍需更新后部署，尚未做手机实机验证。

## 本机更新和打包

词库源码位于 `cn_dicts/`，组合词库入口是 `custom_rime_ice.dict.yaml`，个性化设置保存在 `rime_ice.custom.yaml`、`t9.custom.yaml` 和 `default.custom.yaml`。

在仓库目录运行以下命令生成手机导入包：

```sh
python3 tools/package.py
```

输出为 `dist/rime-personal.zip`。打包脚本只收集可移植的 Rime 源文件，不包含学习记录、同步目录、编译文件、本机安装信息和桌面前端设置。

日常修改后的发布步骤：

```sh
git add cn_dicts custom_rime_ice.dict.yaml rime_ice.custom.yaml t9.custom.yaml default.custom.yaml
git commit -m "Update personal Rime dictionaries"
git push origin main
python3 tools/package.py
# 每次发布使用新的版本号，例如 v2026.10.23。
gh release create v2026.10.23 dist/rime-personal.zip --target main --title v2026.10.23 --notes "更新个人词库"
```

仓库不保存 `*.userdb`、`sync/`、`backups/`、`build/`、`installation.yaml` 或 `user.yaml`，因此下载方案不会获得本机输入历史或学习记录。
