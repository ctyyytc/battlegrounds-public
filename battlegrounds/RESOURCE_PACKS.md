# 外部内容包接口

接口将功能规则与显示内容分离。外部包由使用者自行准备，只读取本地 JSON 和包内图片；仓库不提供原内容包、下载地址或下载器。这里是源码接口说明，本核心归档缺少内置视觉依赖，未做游戏启动或安装界面验证。

## 离线模板与检查

从仓库根目录运行，需要 Python 3.10+ 标准库：

```sh
python battlegrounds/tools/resource_pack.py template --output my-pack
python battlegrounds/tools/resource_pack.py check --pack my-pack/pack.json
```

模板生成 `pack.json`、`image_requirements.json`、`field_requirements.json`。目标文件存在时拒绝覆盖。生成结果含中性默认数值和空名称/说明键，不包含原图文和原值恢复包。

```json
{
  "schema_version": 2,
  "definitions": {
    "BG20_HERO_101": {"name": "示例英雄", "health": 30, "armor": 0}
  },
  "assets": {},
  "templates": {},
  "phrases": {},
  "ui": {},
  "terms": {}
}
```

示例编号仅展示兼容关联；资源、名称和说明由使用者合法准备。空包示例另见 `examples/resource_pack/pack.json`。

## 契约

| 区域 | 用途 | 定义 |
| --- | --- | --- |
| definitions | 显示名、正文和允许的基础数值 | `resource_contract/fields.json` |
| assets | 按稳定图片键填写包内相对路径或显式 null | `resource_contract/images.json` |
| templates | 显示参数模板，不能执行代码或改变效果 | `resource_contract/fields.json` |
| phrases | 计算分支使用的显示片段 | `resource_contract/phrases.json` |
| ui / terms | 界面显示和机制标识的显示用词 | `content/packs/resource_schema.json` |

数字字段按逐 ID/字段白名单及整数边界验证；0 是合法费用、攻击或护甲值，生命须大于 0。`schema_version: 1` 保留旧图文接口，v2 增加允许的基础数值、模板和界面字段。数值身份变化时不能把旧对局档直接套用到不同数值配置。

图片路径须位于包目录内，不接受网络地址、绝对路径、上级路径或符号链接；允许 PNG/JPG/WebP/SVG。省略图片键表示沿用默认，v2 显式 null 表示故意停用。格式参数与模板字段按契约验证，不从文字反推或执行游戏规则。

运行接口支持 `--resource-pack=本地包路径`，默认位置为工程内 `local_resources/pack.json`。安装副本与对局数据分开；源包不应加入公开提交。图片解码、安装/卸载和对局兼容性的实际行为需要在补齐合法视觉依赖后的完整工程中单独验证。
