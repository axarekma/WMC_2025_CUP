import urllib.request
import re
from math import floor
from collections import defaultdict
from tqdm.auto import tqdm
from bs4 import BeautifulSoup


def result_dictionary(result_page_url):
    """Fetch and parse individual player's result page, returning lane scores grouped by course."""
    with urllib.request.urlopen(result_page_url) as response:
        soup = BeautifulSoup(response.read(), "html.parser")

    courselist = []
    datalist = []

    for td in soup.find_all("td"):
        text = td.get_text(strip=True)
        if re.match(r"[EF][1-9]+", text):
            courselist.append(text)
        elif re.match(r"^(1[0-8]|[1-9])$", text):
            datalist.append(int(text))

    if not datalist or not courselist:
        return {}

    num_columns = floor(len(datalist) / 18)
    round_tag = courselist[: num_columns - 1]
    datalist = datalist[: (num_columns) * 18]

    lane_results = defaultdict(list)
    for i, res in enumerate(datalist):
        c = i % num_columns
        l = (i // num_columns) + 1
        if c > 0:
            course_prefix = round_tag[c - 1][0]
            lane_results[f"{course_prefix}{l}"].append(res)

    return lane_results


class BamseScraper:
    def __init__(self, tournament_url):
        if not tournament_url.endswith("/"):
            tournament_url += "/"

        self.tournament_url = tournament_url
        self.DATA = dict()
        self.player2id = dict()

        results_url = tournament_url + "result.htm"
        with urllib.request.urlopen(results_url) as response:
            soup = BeautifulSoup(response.read(), "html.parser")

        # Find player names and their result page URLs
        names = soup.find_all("td", {"class": "namn"})
        for namerow in names:
            a_tag = namerow.find("a")
            if a_tag:
                player_name = a_tag.text.strip()
                player_href = a_tag.get("href")
                if player_href:
                    player_id = player_href.rstrip(".htm")
                    self.player2id[player_name] = player_id

        print(f"Found {len(self.player2id)} players.")

    def player_url(self, player_id):
        """Construct the result page URL for a given player ID."""
        return f"{self.tournament_url}{player_id}.htm"

    def __getitem__(self, player_name):
        """Fetch lane results for a given player name (lazily cached)."""
        if player_name not in self.player2id:
            raise KeyError(f"Player '{player_name}' not found.")

        if player_name not in self.DATA:
            print(f"Retrieving data for {player_name}")
            url = self.player_url(self.player2id[player_name])
            self.DATA[player_name] = result_dictionary(url)

        return self.DATA[player_name]

    def fetch_all(self):
        """Optional helper to prefetch all player data."""
        for player in tqdm(self.player2id.keys()):
            _ = self[player]


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

    def set_result(self, game_tag, playernum, score, hover_image_url=None):
        """
        Set the score for a specific player in a specific game
        game_tag: 1-8 (first round games)
        playernum: the number of the player (1,2)
        score: the score they achieved
        hover_image_url: URL/path to the hover image for this specific match
        """
        element = self.soup.find(id=f"{game_tag}_score{playernum}")
        if element:
            element.string = str(score)
            if hover_image_url:
                element["data-hover-image"] = hover_image_url
                element["class"] = element.get("class", []) + ["score-hover"]

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

    # def get_html_string(self):
    #     """Return the HTML as a string"""
    #     return str(self.soup)


from .matchplay_MC import Cup16, Cup32


def export(cup, tournament):
    tournament.set_players(cup.rank)
    tournament.set_bronze_match(cup.games["SF1"].loser, cup.games["SF2"].loser)
    for tag, game in cup.games.items():
        g1res = game.result
        winner = game.winner
        tournament.set_result(tag, 1, g1res[0], f"fig/{game.hash}.png")
        tournament.set_result(tag, 2, g1res[1], f"fig/{game.hash}.png")
        tournament.set_winner(tag, winner)
    # tournament.save_html(name)
    return tournament.soup


def export16(cup: Cup16):
    tournament = TournamentBracket("templates/cup16template.html")
    return export(cup, tournament)


def export32(cup: Cup32):
    tournament = TournamentBracket("templates/cup32template.html")
    return export(cup, tournament)


from string import Template


def build_result_page(title, header, w_table, m_table, output_file):
    with open("templates/result_template.html") as f:
        template = Template(f.read())

    result = template.substitute(
        title=title,
        header=header,
        w_table=w_table,
        m_table=m_table,
    )

    with open(output_file, "w") as f:
        f.write(result)
