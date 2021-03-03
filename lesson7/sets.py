python = {'alisher', 'bobur', 'davron'}
web = {'davron', 'sevara', 'madina'}
mobile = {'sevara', 'alisher', 'kamol', 'fazlidin'}

python_web = python.union(web)
# print(python_web)

web_mobile = web.union(mobile)
# print(web_mobile)

# all_students = python.union(web).union(mobile)
all_students = python | web | mobile
# print(all_students)

full_stack = python.intersection(web).union(python_web)
print(full_stack)