# scripts（脚本库）

脚本一律**英文名称**；行数不限，但禁裸 `except`、禁 print 调试残留、
禁 >100 字符长行；缓存与状态文件落用户缓存目录，不写本目录。

## 清单

| 脚本 | 职责 |
|---|---|
| [check_links.py](check_links.py) | markdown 悬空链接校验（须＝0） |
| [check_len.py](check_len.py) | `.md` ≤50 行红线校验 |
| [lint_deps.py](lint_deps.py) | `deps.json` 每条须附 `source_url` |
| [deps_check.py](deps_check.py) | 依赖可达性与本地技能存在性自检 |
| [logic_chain.py](logic_chain.py) | 逻辑链 add／debate |
| [process_chain.py](process_chain.py) | 过程链 save／load／interrupt／resume |
| [penalty.py](penalty.py) | 惩罚计数 hit／reset／status（达 10 熔断） |
| [chain_store.py](chain_store.py) | 链存储底座（append 不覆写历史） |
| [garbage_collect.py](garbage_collect.py) | tmp 回收（默认预览） |
| [context_compress.py](context_compress.py) | 长文本压缩为摘要卡片 |
| [sandbox.py](sandbox.py) | 未指定目标时的固定路径沙盒 |
| [self_update.py](self_update.py) | report／compare／release／clean（唯一写盘通道） |

## 用法约定

`python scripts/<name>.py --help` 看参数；写盘类默认预览，需 `--yes` 才落地。
门禁判据由脚本给结果，不接受口头结论（见
[测试门禁](../resistance/测试门禁/测试门禁.md)）。

## 相关

- [../SKILL.md](../SKILL.md) · [../update/update.md](../update/update.md)
