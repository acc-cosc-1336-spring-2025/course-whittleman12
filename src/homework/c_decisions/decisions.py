def get_options_ratio(options, total):
    ratio = options / total
    return float(ratio)

def get_faculty_rating(ratio):
    ratio
    if .9 <= ratio <= 1:
        return "Excellent"
    elif ratio >= .8:
        return "Very Good"
    elif ratio >= .7:
        return "Good"
    elif ratio >= .6:
        return "Needs Improvement"
    else:
        return "Unacceptable"