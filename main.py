import root

root_privilege = root.get_root()

if root_privilege == True:
    next = "roo and user commands"
else:
    next = "only user commands"