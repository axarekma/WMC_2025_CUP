from bs4 import BeautifulSoup
import json


class TournamentBracket:
    def __init__(self, html_file_path):
        """Initialize with the HTML template file path"""
        self.html_file_path = html_file_path
        with open(html_file_path, "r", encoding="utf-8") as f:
            self.soup = BeautifulSoup(f.read(), "html.parser")

    def set_players(self, players_dict):
        """
        Set player names for each rank
        players_dict: {1: "John Doe", 2: "Jane Smith", ...}
        """
        for rank, name in players_dict.items():
            element = self.soup.find(id=f"player{rank}")
            if element:
                element.string = name

    def set_result(self, game_tag, playernum, score):
        """
        Set the score for a specific player in a specific game
        game_tag: 1-8 (first round games)
        playernum: the number of the player (1,2)
        score: the score they achieved
        """
        element = self.soup.find(id=f"{game_tag}_score{playernum}")
        if element:
            element.string = str(score)

    def set_winner(self, game_tag, winner_name):
        """
        Set the winner for quarter-finals, semi-finals, and finals
        game_num: 9-22 for advanced rounds
        winner_name: name of the winning player
        """
        element = self.soup.find(id=f"{game_tag}_winner")
        if element:
            element.string = winner_name

    def set_bronze_match(self, player1, player2):
        """Set the bronze medal match results"""
        # Set players
        elem1 = self.soup.find(id="Bronze_player1")
        elem2 = self.soup.find(id="Bronze_player2")
        if elem1:
            elem1.string = player1
        if elem2:
            elem2.string = player2

    def save_html(self, output_file_path):
        """Save the updated HTML to a file"""
        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(str(self.soup))

    def get_html_string(self):
        """Return the HTML as a string"""
        return str(self.soup)
