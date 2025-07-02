from translate import Translator

# Dictionary of special city input cases and their normalized forms
SPECIAL_CASES = {
    "telaviv": "tel aviv",
    "newyork": "new york",
    "sanfrancisco": "san francisco",
    "mexicocity": "mexico city",
    "washingtondc": "washington",
    "la": "los angeles",
    "nyc": "new york"
}

def normalize_city_name(raw_input: str) -> str:
    """
    Normalize city name by handling known edge cases, removing spaces,
    and mapping to API-compatible names.
    """
    cleaned = raw_input.lower().replace(" ", "")
    return SPECIAL_CASES.get(cleaned, raw_input.lower())

def city():
    """Prompt user to enter a city name and normalize it for API use."""
    search = input("აირჩიეთ ქალაქი: ")
    return normalize_city_name(search)

def translated_city(search):
    """
    Translate the city name into Georgian using the `translate` library.
    Includes special case handling (like Georgia the country).
    """
    translator = Translator(to_lang="ka")
    translated = translator.translate(search)

    # Special case for Georgia
    if search.lower() == "georgia":
        translated = "ჯორჯია"

    return translated
