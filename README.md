# WoW Roll Skill

一个简单的 WoW 风格 `/roll` 小技能。

它会随机生成一个 **1-100** 的点数，并附带一句根据手气高低变化的吐槽/评价，适合在聊天、娱乐、测试手气时使用。

## 功能特点

- 随机生成 `1-100` 点数
- 模拟 World of Warcraft `/roll` 风格输出
- 根据点数返回不同的中文吐槽文案
- 轻量、直接、无需额外依赖（仅需 `python3`）

## 使用方式

在技能目录下可直接运行：

```bash
python3 scripts/roll.py "玩家名"
```

例如：

```bash
python3 scripts/roll.py "Lanny"
```

## 示例输出

```text
Lanny 掷出 57 (1-100)

👌 及格以上，希望能Roll过别人。
```

## 文件结构

```text
wow-roll/
├── README.md
├── SKILL.md
└── scripts/
    └── roll.py
```

## 适用场景

适合以下需求：

- 用户发送 `/roll`
- 想随机掷一个 1-100 点数
- 想模拟 WoW 掷骰子效果
- 想简单试试今天手气如何

## 说明

- 点数范围固定为 `1-100`
- 当前版本主打轻量娱乐，不包含复杂参数配置
- 真正供 OpenClaw/Agent 使用的触发规则与调用说明，请看 `SKILL.md`
