#!/bin/bash

read -p 'DB Username: ' uservar
read -sp 'DB Password: ' passvar

echo
echo Creating Database...
mysql -u $uservar --password=$passvar < tables-league_mngmt.sql

echo
echo Creating Stored Procedures...
mysql -u $uservar --password=$passvar leagues < sp-users-create_user.sql
mysql -u $uservar --password=$passvar leagues < sp-users-get_user.sql
mysql -u $uservar --password=$passvar leagues < sp-users-update_user.sql
mysql -u $uservar --password=$passvar leagues < sp-players-get_players.sql
mysql -u $uservar --password=$passvar leagues < sp-players-create_player.sql
mysql -u $uservar --password=$passvar leagues < sp-players-update_player.sql
mysql -u $uservar --password=$passvar leagues < sp-teams-create_team.sql
mysql -u $uservar --password=$passvar leagues < sp-leagues-create_league.sql
mysql -u $uservar --password=$passvar leagues < sp-privileges-get_privileges.sql

echo
echo Inserting Dummy Data...
mysql -u $uservar --password=$passvar leagues < dummy_data.sql

mysql -u $uservar --password=$passvar leagues