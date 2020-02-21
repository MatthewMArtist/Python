# initial_list = [1, 2, 3]

# def duplicate_last(a_list):
#     last_element = a_list[-1]
#     a_list.append(last_element)
#     return a_list

# new_list = duplicate_last(a_list = initial_list)
# print(new_list)
# print(initial_list)

# content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

# def make_percentages(a_dictionary):
#     total = 0
#     for key in a_dictionary:
#         count = a_dictionary[key]
#         total += count

#     for key in a_dictionary:
#         a_dictionary[key] = (a_dictionary[key] / total) * 100

#     return a_dictionary

# c_ratings_percentages = make_percentages(content_ratings)
# print(c_ratings_percentages)
# print(content_ratings)

this_dict = {
  "medical_supplies": "false",
  "guns": "false",
  "radiation_pills": "false"
}
print(this_dict)

def test_function():
    this_dict.update({"medical_supplies": "true"})
    print(this_dict)

test_function()

x = this_dict.get("medical_supplies")
if x == "true":
    print("success")
else:
    print("failure")
