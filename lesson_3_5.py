from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverds = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["весёлый", "яркий", "зелёный", "утопичный", "мягкий"]

nou, adv, adj = nouns.copy(), adverds.copy(), adjectives.copy()
list_joke = []
list_min = min(nou, adv, adj)

def some_jokes(n, repeat=False):
    while n and len(list_min):
        num = randrange(len(list_min))
        if repeat:
            list_joke.append(f"{nou.pop(num)}, {adv.pop(num)}, {adj.pop(num)}")
        else:
            list_joke.append(f"{choice(nouns)}, {choice(adverds)}, {choice(adjectives)}")
        n -= 1
    return list_joke

print(some_jokes(5))


