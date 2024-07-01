# VALORANT_scoreboard_reader

A Dockerized REST API tool using Tesseract to OCR a screenshot of a VALORANT end game scoreboard and turn it into a CSV or JSON file. 

Additionally, it includes AGENT and TEAM recognition functionality.

Forked from [https://github.com/Apl0x/VALORANT_scoreboard_reader](https://github.com/Apl0x/VALORANT_scoreboard_reader)

## How to use
### Prerequisites

1. **Docker**: Ensure you have Docker installed on your machine. You can download it from [here](https://www.docker.com/products/docker-desktop).

### Running the API

1. **Build the Docker image**:
   ```sh
   docker build -t valorant_scoreboard_reader .
   ```

2. **Run the Docker container**:
   ```sh
   docker run -p 8080:8080 valorant_scoreboard_reader
   ```

3. **API Endpoints**:
   - **POST /process_image**: Process an uploaded image of the scoreboard.
     - **Parameters**:
       - `image`: The screenshot file of the scoreboard.
       - `output_format`: (Optional) The desired output format (`json` or `csv`). Default is `json`.
     - **Example**:
       ```sh
       curl -X POST -F "image=@screenshot.png" -F "output_format=json" http://localhost:8080/process_image
       ```

### Example

The first thing you need is a screenshot of a scoreboard like this:
![ss_1](https://user-images.githubusercontent.com/57774007/220695198-47f6b995-b1e4-4fc8-83f6-46325065e388.png)

The tool has been tested on English and Turkish language screenshots. It only works on screenshots in 16:9 aspect ratio currently. Unfortunately, more testing is required to work with stretched resolution screenshots.

The output should look something like this:

### CSV

| Agent | Team     | Name        | ACS | Kills | Deaths | Assists | Econ Rating | First Bloods | Plants | Defuses |
|-------|----------|-------------|-----|-------|--------|---------|-------------|--------------|--------|---------|
| iso   | attacker | Mierururu   | 394 | 26    | 119    | 2       | 1           | 1            | 1      |         |
| clove | attacker | Rynn        | 206 | 11    | 12     | 10      | 64          | 3            | 0      | 1       |
| omen  | attacker | awenka      | 197 | 12    | 11     | 3       | 44          | 2            | 1      | 1       |
| fade  | attacker | err         | 95  | 5     | 9      | 5       | 30          | 0            | 0      |         |
| cypher| attacker | ZueCallaise | 357 | 21    | 7      | 7       | 115         | 5            | 2      | 1       |
| neon  | defender | err         | 300 | 18    | 16     | 2       | 63          | 4            | 0      | 1       |
| reyna | defender | Gathika     | 114 | 8     | 16     | 2       | 28          | 0            | 0      | 0       |
| sage  | defender | caerulaaki  | 154 | 7     | 15     | 4       | 44          | 0            | 1      | 0       |
| gekko | defender | MengKasir   | 72  | 3     | 13     | 5       | 27          | 1            | 4      | 1       |
| omen  | defender | papoywil    | 195 | 15    | 8      | 55      | 0           | 0            | 0      | 0       |

### JSON
```json
{
    "attacker": [
        {
            "acs": "394",
            "agent": "iso",
            "assist": "2",
            "death": "119",
            "econ_rating": "1",
            "first_bloods": "1",
            "kill": "26",
            "name": "Mierururu",
            "team": "attacker"
        },
        {
            "acs": "357",
            "agent": "cypher",
            "assist": "7",
            "death": "7",
            "defuses": "1",
            "econ_rating": "115",
            "first_bloods": "5",
            "kill": "21",
            "name": "ZueCallaise",
            "plants": "2",
            "team": "attacker"
        },
        {
            "acs": "206",
            "agent": "clove",
            "assist": "10",
            "death": "12",
            "defuses": "1",
            "econ_rating": "64",
            "first_bloods": "3",
            "kill": "11",
            "name": "Rynn",
            "plants": "0",
            "team": "attacker"
        },
        {
            "acs": "197",
            "agent": "omen",
            "assist": "3",
            "death": "11",
            "defuses": "1",
            "econ_rating": "44",
            "first_bloods": "2",
            "kill": "12",
            "name": "awenka",
            "plants": "1",
            "team": "attacker"
        },
        {
            "acs": "95",
            "agent": "fade",
            "assist": "5",
            "death": "9",
            "econ_rating": "30",
            "first_bloods": "0",
            "kill": "5",
            "name": "err",
            "plants": "0",
            "team": "attacker"
        }
    ],
    "defender": [
        {
            "acs": "300",
            "agent": "neon",
            "assist": "2",
            "death": "16",
            "defuses": "1",
            "econ_rating": "63",
            "first_bloods": "4",
            "kill": "18",
            "name": "err",
            "plants": "0",
            "team": "defender"
        },
        {
            "acs": "195",
            "agent": "omen",
            "assist": "55",
            "death": "8",
            "econ_rating": "0",
            "first_bloods": "0",
            "kill": "15",
            "name": "papoywil",
            "plants": "0",
            "team": "defender"
        },
        {
            "acs": "154",
            "agent": "sage",
            "assist": "4",
            "death": "15",
            "defuses": "0",
            "econ_rating": "44",
            "first_bloods": "0",
            "kill": "7",
            "name": "caerulaaki",
            "plants": "1",
            "team": "defender"
        },
        {
            "acs": "114",
            "agent": "reyna",
            "assist": "2",
            "death": "16",
            "defuses": "0",
            "econ_rating": "28",
            "first_bloods": "0",
            "kill": "8",
            "name": "Gathika",
            "plants": "0",
            "team": "defender"
        },
        {
            "acs": "72",
            "agent": "gekko",
            "assist": "5",
            "death": "13",
            "defuses": "1",
            "econ_rating": "27",
            "first_bloods": "1",
            "kill": "3",
            "name": "MengKasir",
            "plants": "4",
            "team": "defender"
        }
    ]
}
```

### Dependencies

All dependencies are included in the Docker image. The main dependencies are:
- `flask`
- `numpy`
- `opencv-python`
- `Pillow`
- `pytesseract`