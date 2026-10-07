# pytest：夹具与参数化（摘录）

- 出处：https://docs.pytest.org/en/stable/how-to/fixtures.html ｜ 访问：2026-10-07
- 包版本：pytest 9.1.1（PyPI 实时核验）｜ 许可：MIT ｜ Python：≥3.10
- 仓库：https://github.com/pytest-dev/pytest ｜ 登记见 [../../dependence/deps.json](../../dependence/deps.json)

## 摘录要点

1. 夹具＝按需注入的前置，作用域 `function/class/module/package/session`；
2. `yield` 型夹具：`yield` 前建、后废， teardown 必在夹具内完成；
3. `@pytest.mark.parametrize` 让一条逻辑展开成多条独立用例——失败可单独归因；
4. `tmp_path` 提供每例独占目录，是「不脏外部状态」的官方路径。

## 本技能用法

- 分层跑：`pytest -m unit` → `pytest -m integration`（[自动化执行](../../branch/自动化执行/自动化执行.md)）；
- 参数化例仍须一 trace 一目标，展开后各例继承同一 trace（[用例溯源](../../resistance/用例溯源/用例溯源.md)）；
- 作用域选错＝脆弱用例源头，分诊先查夹具（[失败分诊](../../branch/失败分诊/失败分诊.md)）。

## 落差与风险

- 官方文档不约束「断言强度」，本技能另加严：禁「异常通过」类断言；
- Web 端到端不在 pytest 管辖，派 [webapp-testing]（[委托边界](../../resistance/委托边界/委托边界.md)）。

## 相关

- [上游文献](上游文献.md) · [../用例模板/夹具样例.md](../用例模板/夹具样例.md)
