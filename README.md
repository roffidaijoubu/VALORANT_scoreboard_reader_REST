# VALORANT_scoreboard_reader

A Dockerized REST API tool using Tesseract to OCR a screenshot of a VALORANT end game scoreboard and turn it into a CSV or JSON file. Additionally, it includes agent recognition functionality.

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
![image](https://user-images.githubusercontent.com/57774007/220700904-34984cfc-61cd-4004-b12f-9393d50e6664.png)

### Dependencies

All dependencies are included in the Docker image. The main dependencies are:
- `flask`
- `numpy`
- `opencv-python`
- `Pillow`
- `pytesseract`