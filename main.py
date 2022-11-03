import root
import attacker
import proc

root_privilege = root.get_root()

if root_privilege == True:
    proc.process()
    attacker.virus()
else:
    next = "only user commands"