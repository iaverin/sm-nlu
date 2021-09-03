from typing import List
from smnlu.spacynlu import Intent

PATTERN_ORDER_STATUS = [
    [{"LEMMA": "где"}, {"OP": "*"}, {"LEMMA": "заказ"}, {"OP": "*"}],
    [{"LEMMA": "узнать"}, {"OP": "*"}, {"LEMMA": "заказ"}, {"OP": "*"}],
    [{"LEMMA": "посмотреть"}, {"OP": "*"}, {"LEMMA": "заказ"}, {"OP": "*"}],
    [{"lower": "пришёл"}, {"OP": "*"}, {"LEMMA": "заказ"}, {"OP": "*"}],
    [{"lower": "пришел"}, {"OP": "*"}, {"LEMMA": "заказ"}, {"OP": "*"}],
    [{"LEMMA": "заказ"}, {"OP": "*"}, {"lower": "пришёл"}, {"OP": "*"}],
    [{"LEMMA": "заказ"}, {"OP": "*"}, {"lower": "пришел"}, {"OP": "*"}],
    [{"LEMMA": "мой"}, {"OP": "*"}, {"lemma": "заказ"}, {"OP": "*"}],
    [{"LEMMA": "заказ"}, {"OP": "*"}, {"lemma": "мой"}, {"OP": "*"}]
]

PATTERN_ORDER_STATUS_STOP = [
    [{"LEMMA": "отменить"}],
    [{"LEMMA": "оформлять"}]
]

INTENTS: List[Intent] = [
    Intent(
        id="order_status",
        patterns_match=PATTERN_ORDER_STATUS,
        patterns_stop=PATTERN_ORDER_STATUS_STOP)
]
