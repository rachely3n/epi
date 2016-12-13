def normalize_path(string):
  #assuming a valid path
  url_tokens = []
  is_abs = False
  if string[0] == '/': #abs path
    is_abs = True

  tokens = string.split('/')

  for token in tokens:
    if token == '.':
      continue
    elif token == "..":
      if not url_tokens or url_tokens[-1] == "..": # still need to go up directory , like "../code/meow.py"
        url_tokens.append(token)
      else:
        url_tokens.pop()
    else:
      if token != "":
        url_tokens.append(token)

  res = '/'.join(url_tokens)
  if is_abs:
    return '/' + res
  else:
    return res

print normalize_path("/usr/lib/../bin/gcc")
print normalize_path("scripts//./../scripts/awkscripts/././")
print normalize_path("../kittykat/../meow.py")