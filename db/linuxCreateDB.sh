#!/bin/bash

mysql -u root < tables-league_mngmt.sql
mysql -u root leagues < sp-users-create_user.sql
mysql -u root leagues < sp-users-get_user.sql
mysql -u root leagues < sp-teams-create_team.sql
mysql -u root leagues < sp-leagues-create_league.sql
mysql -u root leagues < dummy_data.sql
mysql -u root leagues
