# utils/search_filter.py

def search_data(data, keyword):

    results = []

    for item in data:

        item_text = str(item).lower()

        if keyword.lower() in item_text:
            results.append(item)

    return results


def filter_by_category(data, category):

    return [
        item for item in data
        if item.get("category", "").lower() == category.lower()
    ]