from translate import Translator


def city():
    search = input("აირჩიეთ ქალაქი: ").lower()
    if search == "telaviv":
        search = "tel aviv"
    return search


def translated_city(search):
    # To translate information to preferred language (in this case Georgian "ka")
    translator = Translator(to_lang="ka")
    translated = translator.translate(search)
    if search.lower() == "georgia":
        translated = "ჯორჯია"

    return translated
