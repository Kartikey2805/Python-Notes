csv.register_dialect('pdv',delimiter=",",quotechar='"',escapechar="\\")

print(csv.list_dialects())
