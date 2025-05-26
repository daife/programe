import random

# 拼写测试：给中文意思，要求用户输入英文单词
def spelling_test(wordbank, num_questions=5):
    questions = random.sample(wordbank, min(num_questions, len(wordbank)))
    score = 0
    results = []

    print("=== 拼写测试 ===")
    for i, entry in enumerate(questions, 1):
        print(f"\n第 {i} 题：{entry['meaning']}")
        answer = input("请输入英文单词：").strip().lower()
        correct = entry["word"].lower()

        if answer == correct:
            print("✅ 正确")
            score += 1
            results.append((entry["word"], True))
        else:
            print(f"❌ 错误，正确答案是：{correct}")
            results.append((entry["word"], False))

    print(f"\n完成拼写测试，得分：{score}/{len(questions)}")
    return results
