import sys
import random

def get_comment(score):
    if score == 100:
        return "🔥 100点！天呐！欧皇降临！服务器第一！把装备都给他！"
    elif score >= 95:
        return "✨ 绝杀！这手气可以去买彩票了！"
    elif score >= 80:
        return "💪 相当强力的点数，这装备稳了。"
    elif score >= 60:
        return "👌 及格以上，希望能Roll过别人。"
    elif score == 50:
        return "😐 50点... 不偏不倚，极其平庸。"
    elif score >= 20:
        return "😰 有点悬，看来今天要空车了。"
    elif score > 1:
        return "💩 这种点数也好意思roll？退团吧。"
    elif score == 1:
        return "💀 1点... 传说中的‘大黑手’！团长把他踢了！"
    return ""

def main():
    user = sys.argv[1] if len(sys.argv) > 1 else "User"
    # WOW style output format
    score = random.randint(1, 100)
    
    print(f"{user} 掷出 {score} (1-100)")
    print(f"\n{get_comment(score)}")

if __name__ == "__main__":
    main()
