# Operate with rudder objects

def invert(include = None):
  if include != "include":
    return "include"
  else:
    return "exclude"


def rudder_categories(cat, name):
  try:
    for c in cat:
#      print(name)
      if c["name"] == name:
#        print("%s" % json.dumps(c))
        return c
  except:
    pass
  return None


def rule_group(rule, group):
  if not rule:
    return None

  rule = rule[0]
  if group in rule["include"]["or"]:
    return "include"
  elif group in rule["exclude"]["or"]:
    return "exclude"
  else:
    return None


def rudder_groups(group, name):
  try:
    for g in group:
      if g["displayName"] == name:
#        print("%s" % json.dumps(g))
        return g
  except:
    pass
  return None


def rudder_rules(rule, name): # The same as rudder_groups()
  return rudder_groups(rule, name)


def rule_by_name(rules, name):
  for r in rules:
    if r["displayName"] == name:
      return r["id"], r["targets"]
  return None, None


def rule_by_id(rules, id):
  for r in rules:
    if r["id"] == id:
      return r
  return None


# O(n^2), but "n" is small 
def directive_by_name(directives, name):
  for d in directives:
    if d["displayName"] == name:
      return d
  return None


# O(n^2), but "n" is small 
def directive_by_id(directives, id):
  for d in directives:
    if d["id"] == id:
      return d
  return None


def directives_dict_by_id(directives):
  DICT = {}
  try:
    for d in directives:
      DICT[d["id"]] = d["displayName"]
  except:
    pass
  return DICT


def directives_dict_by_name(directives):
  DICT = {}
  try:
    for d in directives:
      DICT[d["displayName"]] = d["id"]
  except:
    pass
  return DICT


def directive_by_id(directives, id):
  try:
    for d in directives:
      if d["id"] == id:
        return d
  except:
    pass
  return None


# Print group tree with categories
def print_groups(tree, path):
  groups = [g["displayName"] for g in tree["groups"]]
  for name in sorted(groups):
    print(f"{path}{name}")

  c = {}
  for cat in tree["categories"]:
    c[cat["name"]] = cat

  for name in sorted(c):
    print_groups(c[name], f"{path}{name}/")

  return


# Print rule tree with categories
def print_rules(tree, path):
  rules = [r["displayName"] for r in tree["rules"]]
  for name in sorted(rules):
    print(f"{path}{name}")

  c = {}
  for cat in tree["categories"]:
    c[cat["name"]] = cat

  for name in sorted(c):
    print_rules(c[name], f"{path}{name}/")

  return
