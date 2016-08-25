-- Table definitions for the tournament project.
--

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

-- Players

CREATE TABLE players  ( id serial primary key,
                        name text not null,
                        date timestamp default current_timestamp );

-- Matches

CREATE TABLE matches  ( id serial primary key,
                        winner_id int,
                        loser_id int,
                        foreign key (winner_id) references players(id),
                        foreign key (loser_id) references players(id) );

-- Players Standings

CREATE VIEW standings AS
  SELECT players.id, players.name, count(matches_won.id) as wins, count(matches_played.id) as played
  FROM players
    LEFT JOIN matches as matches_won
         ON players.id = matches_won.winner_id
    LEFT JOIN matches as matches_played
         ON players.id = matches_played.winner_id OR players.id = matches_played.loser_id
  GROUP BY players.id, players.name
  ORDER BY wins DESC
