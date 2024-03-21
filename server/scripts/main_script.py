from py_add_users import Add_Users
from add_hunts import Add_Hunts
from add_teams import Add_Teams

Add_Users()

hunter = Add_Hunts()
hunt_id = hunter.do()

teams = Add_Teams()
#Replace this string with team leader id from front-end
teams.add(hunt_id, "65e8d7479bf978a5b7c2dfbb")



