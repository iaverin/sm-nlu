print("hello world")
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("ru_core_news_sm")
matcher = Matcher(nlp.vocab)

pattern = [[{"LEMMA": "где"}, {"OP":"*"}, {"LEMMA": "заказ"},{"OP":"*"}],
[{"LEMMA":"узнать"}, {"OP":"*"},{"LEMMA":"заказ"}, {"OP":"*"}], 
[{"LEMMA":"посмотреть"}, {"OP":"*"},{"LEMMA":"заказ"}, {"OP":"*"}],
[{"lower":"пришёл"}, {"OP":"*"},{"LEMMA":"заказ"}, {"OP":"*"}],
[{"lower":"пришел"}, {"OP":"*"},{"LEMMA":"заказ"}, {"OP":"*"}],    
[{"LEMMA":"заказ"}, {"OP":"*"},{"lower":"пришёл"}, {"OP":"*"}],
[{"LEMMA":"заказ"}, {"OP":"*"},{"lower":"пришел"}, {"OP":"*"}],
# [{"LEMMA":"заказ"}, {"OP":"*"},{"lemma":"отменить"}, {"OP":"*"}],
# [{"LEMMA":"отменить"}, {"OP":"*"},{"lemma":"заказ"}, {"OP":"*"}], 
[{"LEMMA":"мой"}, {"OP":"*"},{"lemma":"заказ"}, {"OP":"*"}], 
[{"LEMMA":"заказ"}, {"OP":"*"},{"lemma":"мой"}, {"OP":"*"}]
]

pattern_stop = [[{"LEMMA":"отменить"}], [{"LEMMA":"оформлять"}]]

matcher.add("order_status", pattern)
matcher.add("order_status_stop", pattern_stop)

def match(s:str, pattern: list):
    doc = nlp(s)

    matches = matcher(doc)
    string_id = str
    has_stop_word = False     

    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]  # Get string representation
        
        if string_id == 'order_status_stop': 
            has_stop_word = True 

        span = doc[start:end]  # The matched span
        # print(match_id, string_id, start, end, span.text)

    if len(matches)>0 and has_stop_word == False :
        return True

phrases = list()

with open('trigger_test.txt') as f:
    phrases = f.readlines()
print(f"Total Lines readed {len(phrases)}")

match_count = 0 
unmatched = list()
matched = list()
for i,phrase in enumerate(phrases):
    if i % 50 == 0:
        print(f' {i}/{len(phrases)} ')

    result = match(phrase, pattern)
    if result: 
        match_count += 1
        matched.append(phrase)
        # print(f'"result": {phrase.strip()}')
        
    else:
        unmatched.append(phrase)


print(f'Total matches: {match_count}/{len(phrases)} Ratio:{round(match_count/len(phrases),2)*100}%')

print("================")

with open('_unmatched.txt', mode='w') as f:
    f.writelines(unmatched)

with open('_matched.txt', mode='w') as f:
    f.writelines(matched)



