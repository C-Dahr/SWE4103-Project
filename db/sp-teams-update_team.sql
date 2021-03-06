DELIMITER //

CREATE OR REPLACE PROCEDURE update_team (
    IN      teamID_in             INT,
    IN      leagueID_in     	    INT,
    IN      managerID_in          INT,
    IN      teamName_in   VARCHAR(32),
    IN      colour_in      VARCHAR(7),
    IN      leaguePoints_in       INT,
    IN      wins_in               INT,
    IN      losses_in             INT,
    IN      draws_in              INT
)
BEGIN
    UPDATE teams
        SET leagueID = leagueID_in,
            managerID = managerID_in,
            teamName = teamName_in,
            colour = colour_in,
            leaguePoints = leaguePoints_in,
            wins = wins_in,
            losses = losses_in,
            draws = draws_in
        WHERE teamID = teamID_in;
END

//

DELIMITER ;