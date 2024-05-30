import re

def remove_html_tags(review: str) -> str:
    """
    Function that removes HTML tags from a review (str)
    Parameters:
    review (str): the review to preprocess

    Returns:
    str: the review without HTML tags
    """

    # Test case
    assert type(review) ==  str, "The argument passed is not a string"

    # Cleaning step
    clean = re.compile('<.*?>')
    review = [word.strip() for word in review.strip().split() if word != " "]
    review = " ".join(review)

    return re.sub(clean, '', review)


def convert_target_variable(target: str) -> int:
    """
    Function that transforms the target variable from string to integer

    Parameter:
    target (str): 'positive' or 'negative'

    Returns:
    int:Returning 1 if 'positive' 0 if 'negative'
    """

    assert type(target.lower()) == str and target.lower() in ['positive', 'negative'], "The parameter does not respect the pre-defined conditions"

    if target.lower() == 'positive':
        return 1
    else:
        return 0

