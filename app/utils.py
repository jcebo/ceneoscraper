#funkcja do ekstrakcji składowych opinii
def extract_feature(opinion,selector, attribute = None):
    try:
        if not attribute:
            return opinion.select(selector).pop().get_text().strip()
        else:
            return opinion.select(selector).pop()[attribute]
    except IndexError:
        return None
#funkcja do usuwania znaków formatujących
def remove_whitespaces(text):
    for char in ["\n", "\r"]:
        try:
            return text.replace(char, ". ")
        except AttributeError:
            pass