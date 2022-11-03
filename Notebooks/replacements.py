bio_words = [
    "DNA", "RNA", "AIDS", "HIV", "Hepatitis C", "Hepatitis", "Pneumonia",
    "rRNA", "Kadipiro", "PCR"
]
abv = ["MAHERY"]
species = ['Plasmodium falciparum'
           ]  # Make these ittalic, second word in lower case

country_words = [
    "South-African", "South African", "South-Africa", "South Africa", "Malawi",
    "Malawian", "Egypt", "Egyptian", "Sahara", "Saharan", "sub-Sahara",
    "sub-Saharan", "Asia", "Asian", "USA", "U.S.", "Indonesia", "Liberia",
    "Kenya", "Kenyan", "Ethiopia", "Ethiopian", "Italian", "Itali", "Gambia",
    "Gambian", "Morocco", "Moroccan", "Africans", "Uganda", "Ugandan",
    "Cameroonian", "Cameroonians", "Cameroon", "Alaska", "Nigeria", "Nigerian",
    "Bassa", "Nairobi", "Kenya", "Kenyan", "Tanzania", "Tanzanian", "Botswana",
    "Madagascar", "Africa", "African", "Europe", "European", "Germany",
    "German", "Bamako", "Mali", "Rakai"
]
ethnicity_words = ["Hadza", "Bantu", "Baaka", "Pygmies", "Watwa", "Batwa"]


def replacement_func(change):
    # print(change)
    changes = change.split("//")  #
    tchanges = []
    for change in changes:
        # print(change)
        change = change.strip()
        change = change.capitalize()
        if change.startswith("Aids"):
            change = change.replace("Aids", "AIDS")
        for rep in bio_words + abv + country_words + ethnicity_words + species:
            if change.startswith(rep) or " " + rep.lower() in change:
                change = change.replace(rep.lower(), rep)
        tchanges.append(change)
    return " // ".join(tchanges)


if __name__ == '__main__':
    replacement_func("Who am I?")
