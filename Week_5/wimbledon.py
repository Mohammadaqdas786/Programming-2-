FILENAME = "wimbledon.csv"


def main():
    data = load_data(FILENAME)
    champion_to_wins = count_champions(data)
    countries = extract_countries(data)
    display_results(champion_to_wins, countries)


def load_data(filename):
    """Read the Wimbledon CSV file and store the data in a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip header line
        data = [line.strip().split(",") for line in in_file]
    return data


def count_champions(data):
    """Count how many times each champion has won."""
    champion_to_wins = {}
    for record in data:
        champion = record[2]
        if champion in champion_to_wins:
            champion_to_wins[champion] += 1
        else:
            champion_to_wins[champion] = 1
    return champion_to_wins


def extract_countries(data):
    """Extract all unique countries of champions in alphabetical order."""
    countries = {record[1] for record in data}
    return sorted(countries)


def display_results(champion_to_wins, countries):
    """Display champions and number of wins, and display sorted country codes."""
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(f"{champion} {wins}")
    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


if __name__ == "__main__":
    main()