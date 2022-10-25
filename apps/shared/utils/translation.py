def from_en_to_ru(word: str):
    if not word:
        return ''
    symbols = (u'abdefghijklmnopqrstuvxyzwcABDEFGHIJKLMNOPQRSTUVXYZC',
               u'абдефгхижклмнопкрстувхйзвкАБДЕФГХИЖКЛМНОПКРСТУВХЙЗК')
    characters = {ord(a): ord(b) for a, b in zip(*symbols)}
    return word.replace('sh', 'ш').replace('ch', 'ч').replace('g\'', 'г'). \
        replace('Sh', 'Ш').replace('Ch', 'Ч').replace('G\'', 'Г').translate(characters)


def from_ru_to_en(word: str):
    if not word:
        return ''
    symbols = (u'абвгдеёжзийклмнопрстуфхъыьэАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЪЫЬЭ',
               u'abvgdeejzijklmnoprstufh_i_eABVGDEEJZIJKLMNOPRSTUFX_I_E')
    characters = {ord(a): ord(b) for a, b in zip(*symbols)}
    return word.replace('ш', 'sh').replace('ч', 'ch').replace('щ', 'sh').replace('ю', 'yu').replace('я', 'ya') \
        .replace('ц', 'ts').replace('Ш', 'Sh').replace('Щ', 'Sh').replace('Ч', 'Ch').replace('Ю', 'Yu') \
        .replace('Я', 'Ya').replace('Ц', 'Ts').translate(characters).replace('_', '')
