from django import template

register = template.Library()

BAD_WORDS = [
    'дурак', 'ублюдок', 'тупица', 'идиот',  'баран', 'говно', 'сволочь', 'блядь', 'подонок', 'ублюдок', 'тварь', 'гадина', 'скотина',
    'bastard', 'jerk', 'idiot', 'dumb', 'moron', 'scumbag', 'loser', 'freak', 'creep', 'ugly', 'fuck'
]

@register.filter(name='censor')
def censor(text):
    if not isinstance(text, str):
        raise TypeError("Censor filter can only be applied to strings.")

    def replace_bad_word(word):
        for bad_word in BAD_WORDS:
            if word.lower().startswith(bad_word.lower()):
                return word[0] + '*' * (len(word) - 1)
        return word

    words = text.split()
    censored_text = ' '.join(replace_bad_word(word) for word in words)

    return censored_text
