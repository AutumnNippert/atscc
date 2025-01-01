import json
import sys

# Function to generate HTML for a single year
def generate_html_for_year(year, standings, data):
    html = []
    html.append(f'<h1 class="h1 p-2">{year} Results</h1>')
    html.append('<table class="table table-striped">')
    html.append('<caption>Width of thickest point (mm)</caption>')
    html.append('<thead>')
    html.append('<tr>')
    html.append('<th scope="col">Place</th>')
    html.append('<th scope="col">Person</th>')
    html.append('<th scope="col">Width (mm)</th>')
    html.append('</tr>')
    html.append('</thead>')
    html.append('<tbody>')

    for place, person in enumerate(standings, start=1):
        cuts = ", ".join(map(str, data.get(person, {}).get("Cuts", ["Unknown"])))
        html.append('<tr>')
        html.append(f'<th scope="row">{place}</th>')
        html.append(f'<td>{person}</td>')
        html.append(f'<td>{cuts}</td>')
        html.append('</tr>')

    html.append('</tbody>')
    html.append('</table>')
    return "\n".join(html)

# Main function to read JSON and generate HTML
def main(json_file):
    try:
        with open(json_file, 'r') as f:
            json_data = json.load(f)

        standings = json_data.get("Standings", {})
        data = json_data.get("Data", {})

        output_html = []
        for year in sorted(standings.keys()):
            year_standings = standings[year]
            year_data = data.get(year, {})
            output_html.append(generate_html_for_year(year, year_standings, year_data))

        # Output the HTML
        print("\n".join(output_html))
    except FileNotFoundError:
        print(f"Error: File {json_file} not found.")
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON. Please check the input file.")

# Entry point
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 generate_archive.py <path_to_json_file>")
    else:
        json_file = sys.argv[1]
        main(json_file)