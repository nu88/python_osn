from random import choice


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def slo(from_, used_, unique):
    while True:
        n_nouns = choice(from_)

        if not (unique and n_nouns in used_):
            used_.append(n_nouns)
            break

    return (n_nouns, used_)

def get_jokes(count, unique=False):

    used = []
    answer = []

    if unique and count < len([*nouns, *adverbs, *adjectives]):
        return []
    for _ in range(count):

        nons, used_ = slo(nouns, used, unique)
        used.append(used_)

        adv, used_ = slo(adverbs, used, unique)
        used.append(used_)

        adj, used_ = slo(adjectives, used, unique)
        used.append(used_)

        answer.append(f"{nons} {adv} {adj}")


    return answer

print(get_jokes(2))