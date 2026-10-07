# Coverage.py：覆盖率作为门禁证据（摘录）

- 出处：https://coverage.readthedocs.io/ ｜ 访问：2026-10-07
- 包版本：coverage 7.16.2（PyPI 实时核验）｜ 许可：Apache-2.0 ｜ Python：≥3.10
- 仓库：https://github.com/nedbat/coveragepy ｜ 登记见 [../../dependence/deps.json](../../dependence/deps.json)

## 摘录要点

1. `coverage run -m pytest` 采集行覆盖，`coverage report`／`coverage html` 出证据；
2. `--fail-under=<pct>` 可把覆盖率变成退出码，门禁可直接消费；
3. 分支覆盖需 `branch = true`——行覆盖高不代表路径全覆盖；
4. 产物（`.coverage`、`htmlcov/`）属运行产物，不入版本库（[.gitignore](../../.gitignore)）。

## 本技能用法

- 覆盖率是**证据之一**，非结论：放行仍须四项齐备
  （[测试门禁](../../resistance/测试门禁/测试门禁.md)：真实运行记录＋失败清单＋归因＋去向）；
- 阈值只可上调不可为凑绿下调（[审查约束](../../resistance/审查约束/审查约束.md) 禁放宽参数）；
- 无覆盖数据时结论写「证据不足」，不写「通过」（[质量门禁](../../branch/质量门禁/质量门禁.md)）。

## 禁止

- 用排除规则（`omit`）隐藏未测模块来抬百分比；
- 把覆盖率截图当记录——要的是可复跑命令与原始输出。

## 相关

- [上游文献](上游文献.md) · [编排判例/ST-001](../编排判例/ST-001-校验脚本参数面漂移.md)
