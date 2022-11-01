import root

root_privilege = root.get_root()

if root_privilege == True:
    next = "root and user commands"
else:
    next = "only user commands"