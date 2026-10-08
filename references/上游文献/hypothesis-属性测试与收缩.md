# Hypothesis：属性测试与反例收缩（摘录）
- 出处：https://hypothesis.readthedocs.io ｜ 访问：2026-10-08
- 包版本：hypothesis 6.168.5（PyPI 实时核验）｜ 许可：MPL-2.0 ｜ Python：≥3.10
- 仓库：https://github.com/HypothesisWorks/hypothesis ｜ 登记见
  [../../dependence/deps.json](../../dependence/deps.json)
## 摘录要点
1. `@given(...)` 用策略（strategy）生成输入，把「等价类＋边界」写成名可执行的生成器；
2. 失败时自动**收缩**到最小反例（shrinking），归因成本远低于随机 fuzz；
3. `settings(deadline=None)` 仅用于确证慢用例，默认保留超时以防不可复跑；
4. `derandomize=True`／固定 `--hypothesis-seed` 才可在门禁里引用为可复现证据；
5. 数据库 `.hypothesis/` 属运行产物，不入版本库（[.gitignore](../../.gitignore)）。
## 本技能用法
- 用在 [用例设计](../../branch/用例设计/用例设计.md) 第 1 项之后：等价类→属性断言；
- 证据四件套需附最小反例与种子，否则记「证据不足」（[测试门禁]
  (../../resistance/测试门禁/测试门禁.md)）；
- 变异测试（mutmut）与属性测试互补：前者证断言会红，后者证输入面够宽。
## 禁止
- 把属性测试当「随机跑很多次绿」——无收缩与种子即不可复跑；
- 用 `assume` 过滤掉全部失败输入来抬通过率。
## 相关
- [上游文献](上游文献.md) · [用例模板](../用例模板/用例模板.md)
