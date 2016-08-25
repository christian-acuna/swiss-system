#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def connect(database_name="tournament"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("<error message>")

def registerPlayer(name):
    db, cursor = connect()

    query = "INSERT INTO players (name) VALUES (%s);"
    parameter = (name,)
    cursor.execute(query, parameter)

    db.commit()
    db.close()


def deleteMatches():
    """Remove all the match records from the database."""
    db, cursor = connect()
    cursor = db.cursor()
    cursor.execute("DELETE FROM matches;")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, cursor = connect()
    cursor = db.cursor()
    cursor.execute("DELETE FROM players;")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, cursor = connect()
    cursor = db.cursor()
    cursor.execute("SELECT Count(id) FROM players AS total_players;")
    count_players = cursor.fetchone()[0]
    db.close()
    return count_players


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, cursor = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM standings;")
    player_standings = cursor.fetchall()
    db.close()
    return player_standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, cursor = connect()
    cursor = db.cursor()
    cursor.execute("INSERT INTO matches (winner_id, loser_id) values (%s, %s);",
              (winner, loser))
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    swissPairings = list()

    for player_1, player_2 in zip(standings[0::2], standings[1::2]):
        swissPairings.append((player_1[0], player_1[1], player_2[0], player_2[1]))

    return swissPairings
