# the all so familiar key value pairs, similiar to objects
# in js and maps in golang

# but in python, keys are uniques in dictionaries
user = {
    "name": "prime",
    "age": 10000,
    # "age": 2, if this is added, the former will be ignored
    "role": "superadmin",
    "is_awakened": True
}
print(user["role"])  # remember,case sensitive

# can mutate as so
user["age"] = "infinity"  # so funny and dangerous without type safety


# a better way to query for a key, and add a default
# if not avail
print(user.get("friends", "daveads"))
