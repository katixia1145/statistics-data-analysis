# 统计与大数据分析 - 概念学习资料仓库

## 📖 项目简介

这是一个专门用于**《统计与大数据分析》课程**学习的 Git 仓库，集成了 WorkBuddy AI 的**概念学习资料生成 Skill（v2.0）**，帮助你系统性地掌握课程核心概念以及 AI 相关基础知识。

> **Skill 已升级至 v2.0**：从"统计专用"扩展为**全领域通用**，可学习任何学科的概念！

---

## ✨ 核心功能

### 🎯 概念学习资料生成器（SKILL.md v2.0）

内置 AI 驱动的学习助手，能够为**任意领域的概念**自动生成结构化学习资料：

- 📚 **完整的概念解析**（定义、公式、直观解释、个人理解）
- ⚙️ **核心机制详解**（组成结构、工作原理、技术细节）
- 💡 **实际应用场景**（真实案例 + 行业应用数据）
- ⚠️ **易混淆问题澄清**（对比表格 + 使用边界）
- 🔗 **知识关联图谱**（前置知识、相关概念、进阶方向）
- 📝 **配套练习题**（基础、计算、应用、编程）
- 💻 **代码示例**（Python / R / 其他语言）
- 📚 **可核查来源**（教材、论文、官方文档链接）

### 🎯 适用范围（v2.0 新增）

| 领域 | 示例概念 |
|------|---------|
| **统计与大数据分析** | 假设检验、回归分析、中心极限定理 |
| **AI 基础** | Agent、LLM Context、Skill、Prompt |
| **计算机科学** | 数据结构、算法、操作系统 |
| **数学** | 线性代数、概率论、微积分 |
| **其他领域** | 经济学、物理学、心理学... |

---

## 🚀 快速开始

### 前提条件
- 已安装 [WorkBuddy](https://www.workbuddy.cn)
- 已配置 Git 和 GitHub 账户

### 使用方式

1. **克隆仓库到本地**
   ```bash
   git clone https://github.com/katixia1145/statistics-data-analysis.git
   cd statistics-bigdata-learning
   ```

2. **在 WorkBuddy 中使用 Skill**

   打开此项目目录后，你可以直接使用自然语言命令：

   #### 统计与大数据分析概念
   ```
   帮我学习"中心极限定理"
   帮我规划《统计与大数据分析》的复习计划
   解释均值、中位数和众数的区别
   为"假设检验"生成练习题
   ```

   #### AI / 计算机科学概念（v2.0 新增）
   ```
   帮我学习"Agent（智能体）"是什么
   解释 LLM Context 的作用机制
   什么是 Skill？和 Prompt 有什么区别？
   ```

3. **查看生成的学习资料**

   所有生成的学习资料会保存在 `learning-materials/` 目录中。

---

## 📁 项目结构

```
statistics-data-analysis/
├── .workbuddy/
│   └── skills/
│       └── concept-learning-generator/
│           └── SKILL.md              # ⭐ 核心 Skill 定义 (v2.0)
├── learning-materials/               # 📚 学习资料文档
│   │
│   │── 📖 Markdown 学习资料（推荐阅读）
│   │   ├── agent.md                 # Agent（智能体）概念深度解析
│   │   ├── llm-context.md           # 大数据分析的上下文（Context）机制全解
│   │   ├── skill.md                 # Skill（技能模块）完整说明
│   │   └── concept-relationship.md  # 三概念关系图谱（含 Mermaid 图）
│   │
│   │── 🌐 HTML 可视化版本（带交互式图表）
│       ├── agent.html               # AI 智能体架构可视化
│       ├── llm-context.html         # 上下文管理交互式演示
│       ├── skill.html               # Skill 规范详细展示
│       └── concept-relationship.html# 概念关系网络图
│
├── README.md                        # 📖 本文件
└── .gitignore                       # Git 忽略规则
```

---

## 📚 已生成的学习资料

### 核心概念资料（Markdown 版本）

| 文档 | 内容概览 | 类比 | 来源数 |
|------|---------|------|--------|
| **[agent.md](./learning-materials/agent.md)** | Agent（智能体）概念深度解析 | 🚗 自动驾驶汽车 | 15个 |
| **[llm-context.md](./learning-materials/llm-context.md)** | 大数据分析的上下文（Context）机制全解 | 📊 数据分析师的工作记忆 | 13个 |
| **[skill.md](./learning-materials/skill.md)** | Skill（技能模块）完整说明 | 👨‍🍳 厨师的食谱卡 | 13个 |
| **[concept-relationship.md](./learning-materials/concept-relationship.md)** | Agent、Context、Skill 三者关系图谱 | 🔗 Mermaid 图 + 表格 | - |

#### 每份资料都包含 5 大要素

✅ **个人解释** - 用通俗类比帮助快速理解  
✅ **核心机制** - 技术细节和组成结构  
✅ **应用场景** - 真实案例（如阿里智能客服、GitHub Copilot）  
✅ **易混淆问题** - 对比表格澄清常见误区  
✅ **可核查来源** - 教材、论文、官方文档链接（共 48 个去重链接）

---

### 可视化版本（HTML）

| 文档 | 特色功能 |
|------|---------|
| **[agent.html](./learning-materials/agent.html)** | 架构图、能力矩阵、工作流程动画 |
| **[llm-context.html](./learning-materials/llm-context.html)** | 5层结构图、Token窗口演示、优化策略 |
| **[skill.html](./learning-materials/skill.html)** | 完整规范、触发条件、输出模板预览 |
| **[concept-relationship.html](./learning-materials/concept-relationship.html)** | 交互式知识网络、学习路径图、对比矩阵 |

---

## 🎯 使用示例

### 示例 1：学习统计概念
**输入：**
> 帮我学习"中心极限定理"

**输出：**
- 完整的数学定义和直观解释
- Python 模拟实验代码（演示样本均值的分布）
- 实际应用场景（置信区间、假设检验）
- 5道配套练习题 + 可核查来源

### 示例 2：学习 AI 概念（v2.0 新增）
**输入：**
> 帮我学习"Agent（智能体）"

**输出：**
- 个人解释（自动驾驶汽车类比）
- 核心机制（感知→认知→记忆→行动→学习 5大组件）
- 应用场景（阿里智能客服、GitHub Copilot）
- 易混淆问题（vs Bot / Algorithm / Model）
- 15 个权威来源链接

### 示例 3：理解概念间的关系
**输入：**
> Agent、Context 和 Skill 之间有什么关系？

**输出：**
- 核心观点：Agent = 行动主体, Context = 工作记忆, Skill = 能力模块
- Mermaid 序列图和架构图
- 重点解答：上下文如何影响 Agent？Skill 如何沉淀知识？
- 对比表格和相互作用矩阵

### 示例 4：期末复习计划
**输入：**
> 我要准备《统计与大数据分析》期末考试，帮我制定复习计划

**输出：**
- 4周学习路线图
- 每周重点知识点
- 自测题库（每章10题）
- 高频考点总结

---

## 🔄 Skill 工作流程（v2.0）

当你提出学习请求时，Skill 会按照以下流程工作：

```
用户输入 → 概念识别 → 需求分析 → 资料检索 → 内容生成 → 自检确认 → 输出保存
   ↓          ↓          ↓          ↓          ↓          ↓          ↓
 10秒       15秒       20秒      30-60秒    2-3分钟     30秒      自动保存
```

**详细步骤**（共8步）：
1. 接收并理解用户输入
2. 识别目标概念及领域
3. 分析学习需求（深度、广度、格式偏好）
4. 检索高质量资料来源
5. 按标准模板生成内容
6. 执行质量自检（8项检查清单）
7. 输出结构化学习资料
8. 保存到 `learning-materials/` 目录

---

## 🛠️ 技术栈

- **AI 引擎**: WorkBuddy AI Assistant
- **Skill 版本**: v2.0（全领域通用）
- **格式**: Markdown + LaTeX（数学公式）+ Mermaid（图表）
- **编程语言**: Python 3.x / R
- **版本控制**: Git & GitHub
- **数据可视化**: Matplotlib, Seaborn, Plotly, Mermaid.js

---

## 🤝 贡献指南

欢迎贡献！你可以：

1. **📝 提出概念请求**：在 Issues 中提出你想学习的概念
2. **💾 分享学习资料**：提交你生成的优质学习笔记
3. **⚡ 改进 Skill**：优化 `SKILL.md` 的模板或流程
4. **💻 添加代码示例**：提供更多实际案例
5. **🔗 补充资料来源**：添加权威参考链接

---

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

---

## 🙏 致谢

- WorkBuddy 团队提供的 AI 能力支持
- 《统计与大数据分析》学习社区的优质资源
- 所有贡献者的努力

---

## 📊 项目统计

| 指标 | 数值 |
|------|------|
| **Skill 版本** | v2.0 |
| **已生成学习资料** | 8 份（4 Markdown + 4 HTML） |
| **引用来源总数** | 48 个（跨文档去重链接） |
| **Git 提交次数** | 9 次 |
| **文档总行数** | 5100+ 行 |
| **最后更新** | 2026-09-04 |

---

**🚀 开始你的学习之旅吧！**

如有问题，欢迎在 [GitHub Issues](https://github.com/katixia1145/statistics-data-analysis/issues) 中提问。
