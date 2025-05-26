import random

# 义项选择测试：给英文单词，选择正确中文意思
def meaning_test(wordbank, num_questions=5):
    questions = random.sample(wordbank, min(num_questions, len(wordbank)))
    score = 0
    results = []

    print("=== 释义选择测试 ===")
    for i, entry in enumerate(questions, 1):
        correct_definition = entry["meaning"]
        options = [correct_definition]

        # 随机选三个错误释义
        wrong_options = [w["meaning"] for w in random.sample(wordbank, min(10, len(wordbank))) if w["word"] != entry["word"]]
        options.extend(random.sample(wrong_options, min(3, len(wrong_options))))
        random.shuffle(options)

        print(f"\n第 {i} 题：{entry['word']}")
        for idx, opt in enumerate(options):
            print(f"{idx + 1}. {opt}")

        try:
            choice = int(input("请选择正确的释义（输入序号）："))
            if options[choice - 1] == correct_definition:
                print("✅ 正确")
                score += 1
                results.append((entry["word"], True))
            else:
                print(f"❌ 错误，正确释义是：{correct_definition}")
                results.append((entry["word"], False))
        except (ValueError, IndexError):
            print("⚠️ 输入无效，视为错误")
            results.append((entry["word"], False))

    print(f"\n完成释义测试，得分：{score}/{len(questions)}")
    return results
