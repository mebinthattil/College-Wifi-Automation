from setup import user_data_read, start_setup

json_data = user_data_read()
if json_data["username"] == "":
    start_setup()

import login