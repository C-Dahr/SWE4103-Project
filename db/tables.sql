DROP DATABASE IF EXISTS leagues;
CREATE DATABASE IF NOT EXISTS leagues;
USE leagues;

SELECT 'CREATING DATABASE STRUCTURE' as 'INFO';

DROP TABLE IF EXISTS gameMembers, teamMembers, players, games, teams, leagues, users, privileges;

CREATE TABLE privileges (
    privilegesID        INT             NOT NULL AUTO_INCREMENT,
    privilegesType      VARCHAR(16)     NOT NULL,
    cancelGame          BOOLEAN         NOT NULL,
    updateScore         BOOLEAN         NOT NULL,
    createPlayer        BOOLEAN         NOT NULL,
    createGame          BOOLEAN         NOT NULL,
    createUser          BOOLEAN         NOT NULL,
    createTeam          BOOLEAN         NOT NULL,
    createLeague        BOOLEAN         NOT NULL,
    assignPlayer        BOOLEAN         NOT NULL,
    assignManager       BOOLEAN         NOT NULL,
    assignCoordinator   BOOLEAN         NOT NULL,
    assignprivileges    BOOLEAN         NOT NULL,
    PRIMARY KEY (privilegesID)
);

CREATE TABLE users (
    userID              INT             NOT NULL AUTO_INCREMENT,
    privilegesID        INT             DEFAULT NULL,
    userType            VARCHAR(16)     NOT NULL,
    firstName           VARCHAR(32)     NOT NULL,
    lastName            VARCHAR(32)     NOT NULL,
    email               VARCHAR(64)     NOT NULL,
    hash                VARCHAR(256)    NOT NULL,
    lastLogin           DATE            DEFAULT NULL,
    UNIQUE (email),
    FOREIGN KEY (privilegesID) REFERENCES privileges (privilegesID),
    PRIMARY KEY (userID)
);

CREATE TABLE leagues (
    leagueID            INT             NOT NULL AUTO_INCREMENT,
    coordinatorID       INT             DEFAULT NULL,
    leagueName          VARCHAR(64)     NOT NULL,
    season              VARCHAR(16)     NOT NULL,
    FOREIGN KEY (coordinatorID) REFERENCES users (userID),
    PRIMARY KEY (leagueID)
);

CREATE TABLE teams (
    teamID              INT             NOT NULL AUTO_INCREMENT,
    leagueID            INT             NOT NULL,
    managerID           INT             DEFAULT NULL,
    teamName            VARCHAR(32)     NOT NULL,
    leaguePoints        INT             NOT NULL DEFAULT 0,
    wins                INT             NOT NULL DEFAULT 0,
    losses              INT             NOT NULL DEFAULT 0,
    draws               INT             NOT NULL DEFAULT 0,
    FOREIGN KEY (managerID) REFERENCES users (userID),
    FOREIGN KEY (leagueID) REFERENCES leagues (leagueID),
    PRIMARY KEY (teamID)
);

CREATE TABLE games (
    gameID              INT             NOT NULL AUTO_INCREMENT,
    leagueID            INT             NOT NULL,
    homeTeamID          INT             NOT NULl,
    awayTeamID          INT             NOT NULL,
    refereeID           INT             NOT NULL,
    fieldName           VARCHAR(32)     NOT NULL,
    canceled            BOOLEAN         NOT NULL DEFAULT 0,
    homeGoals           INT             NOT NULL DEFAULT 0,
    awayGoals           INT             NOT NULL DEFAULT 0,
    FOREIGN KEY (leagueID) REFERENCES leagues (leagueID),
    FOREIGN KEY (homeTeamID) REFERENCES teams (teamID),
    FOREIGN KEY (awayTeamID) REFERENCES teams (teamID),
    FOREIGN KEY (refereeID) REFERENCES users (userID),
    PRIMARY KEY (gameID)
);

CREATE TABLE players (
    playerID            INT             NOT NULL AUTO_INCREMENT,
    firstName           VARCHAR(32)     NOT NULL,
    lastName            VARCHAR(32)     NOT NULL,
    email               VARCHAR(64)     DEFAULT NULL,
    PRIMARY KEY (playerID)
);

CREATE TABLE teamMembers (
    teamID              INT             NOT NULL,
    playerID            INT             NOT NULL,
    loanedGames         INT             NOT NULL DEFAULT 0,
    FOREIGN KEY (teamID) REFERENCES teams (teamID),
    FOREIGN KEY (playerID) REFERENCES players (playerID),
    PRIMARY KEY (teamID, playerID)
);

CREATE TABLE gameMembers (
    gameID              INT             NOT NULL,
    teamID              INT             NOT NULL,
    playerID            INT             NOT NULL,
    goals               INT             NOT NULL DEFAULT 0,
    assists             INT             NOT NULL DEFAULT 0,
    cleanSheet          INT             NOT NULL DEFAULT 0,
    yellowCards         INT             NOT NULL DEFAULT 0,
    redCards            INT             NOT NULL DEFAULT 0,
    FOREIGN KEY (gameID) REFERENCES games (gameID),
    FOREIGN KEY (teamID) REFERENCES teams (teamID),
    FOREIGN KEY (playerID) REFERENCES players (playerID),
    PRIMARY KEY (playerID, teamID, gameID)
);

SELECT 'DATABASE STRUCTURE CREATED' as 'INFO';