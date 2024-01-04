def sort_string_chars(string):
  """Sorts the characters in a string and returns the sorted string."""

  sorted_chars = sorted(string)
  print(sorted_chars)
  return ''.join(sorted_chars)

# Example usage:
string = "applebanana"
sorted_string = sort_string_chars(string)
print(sorted_string)  # Output: aaabelnnp