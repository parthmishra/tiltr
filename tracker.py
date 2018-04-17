"""Manual tracker for adding documenting surrender (FF) votes.

This module allows a user to supply information regarding surrender
votes for a single game of League of Legends.

Example:
    $ python tracker.py


Attributes:
    SUMMONER_NAME (string): In-game League name
    SUMMONER_REGION (string): Name of the League server. Valid values
        are:
            * NA
            * EUW
            * EUNE
            * KR
            * OCE
            * BR
            * LAS
            * LAN
            * JP
            * RUS
            * TR
        Note that Garena regions are not supported yet due to Riot API
        limitations.

Todo:
    * automate FF data generation
    * link to game data
"""
