#Check the string and tell whether it’s a palindrome or not:


# function
def is_palindrome(word):
    word = str(word)
    return word == word[::-1]


# Given a string, find the longest substring that is a palindrome.

def longestPalindrome(text):
    lst = text.split()
    lst = list(map(str.lower, lst))
    word = ""
    count = 0

    for i in lst:
        if i == i[::-1]:
            if len(i) > count:
                count = len(i)
                word = i

    return f"The longest palindrome is '{word}'" if word else "No palindromes found."


# Given a list of customer transactions (customer_id, order_id), return the customer who made the most purchases.

def most_frequent(List):
    customers = []
    for i in List:
        customers.append(i[0])

    return f"The most frequent customer is: {max(set(customers), key=customers.count)}"


# or

from collections import Counter


def most_frequent(List):
    customer_counts = Counter(customer_id for customer_id, _ in List)  # Count occurrences
    most_common_customer = customer_counts.most_common(1)[0][0]  # Get most frequent customer

    return f"The most frequent customer is: {most_common_customer}"

