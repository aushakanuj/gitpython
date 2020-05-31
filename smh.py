# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import json
s="Hello my name is aushak anuj"


# %%
l=s.split()


# %%
print(l)


# %%
path="Course1/datasets/example.json"


# %%
with open(path,"r") as f:
    l=f.readlines()
    for line in l:
        d=json.loads(line)
        print(json.dumps(d,indent=3))
    


# %%



# %%


