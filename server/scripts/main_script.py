from py_add_users import Add_Users
from add_hunts import Add_Hunts
from add_teams import Add_Teams

Add_Users()

hunter = Add_Hunts()
hunt_ids = hunter.do()

teams = Add_Teams()

teams.add(hunt_ids)



