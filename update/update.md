# update（自更新接口）

本技能**唯一写盘通道**：任何内容变更先落 tmp 镜像，再比对释放。
用途限于「使用/测试中发现并纠正错误」，不是任意改写。

## 四条命令

1. `python ../scripts/self_update.py report --error <描述> [--repro <复现>]`
   —— 登记错误（落用户缓存目录）。
2. `python ../scripts/self_update.py compare --tmp <镜像> --target <skill目录>`
   —— 列差异。
3. `python ../scripts/self_update.py release --tmp <镜像> --target <skill目录> --yes`
   —— 差异释放到本体（不加 `--yes` 只预览，禁止静默写盘）。
4. `python ../scripts/self_update.py clean --tmp <镜像> --yes`
   —— 释放后删除镜像（配合 [垃圾回收机制](../resistance/垃圾回收机制/垃圾回收机制.md)）。

## 审批流（resistance/ 与红线区变更）

1. 提出变更动机与影响面，记逻辑链 `logic_chain.py add`；
2. 双链辩论 `logic_chain.py debate --claim ... --pro ... --con ...`；
3. 红线区（见 [约束部分](../resistance/约束部分/约束部分.md)）**只可加严**，不可放宽或删除；
4. compare → release → clean，`CHANGELOG.md` 记条目；
5. git：功能分支 → dev →（整体审查通过）→ main。

## 边界

- 技能自身不执行 `planned_tasks/`（到期由 SMS 调度器读取执行）；
- 不写其他技能目录；专项能力变更归被派发技能自身。

## 相关

- [../SKILL.md](../SKILL.md) · [../scripts/scripts.md](../scripts/scripts.md)
