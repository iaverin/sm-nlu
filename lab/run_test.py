from smnlu.spacynlu import SpacyNlu
from intents import INTENTS


nlu = SpacyNlu("ru_core_news_sm", INTENTS)

phrases = list()

file_name = 'trigger_test.txt'

with open(file_name, encoding='utf-8') as f:
    phrases = f.readlines()
print(f"Total Lines readed {len(phrases)}")

match_count = 0
unmatched = list()
matched = list()
for i, phrase in enumerate(phrases):
    if i % 50 == 0:
        print(f' {i}/{len(phrases)} ')

    result = nlu.intent(phrase)
    if result:
        match_count += 1
        matched.append(phrase)
        # print(f'"result": {phrase.strip()}')

    else:
        unmatched.append(phrase)

print(f'Total matches: {match_count}/{len(phrases)} Ratio:{round(match_count / len(phrases), 2) * 100}%')

print("================")

with open(file_name + '_unmatched.txt', mode='w', encoding='utf-8') as f:
    f.writelines(unmatched)

with open(file_name + '_matched.txt', mode='w', encoding='utf-8') as f:
    f.writelines(matched)
