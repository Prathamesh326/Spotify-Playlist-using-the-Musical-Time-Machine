**Billboard Top 100 to Spotify Playlist**

This Python script retrieves the Billboard Hot 100 songs from a specified date and creates a private Spotify playlist with those songs.

## Prerequisites

Before running the script, make sure you have:

- Python 3.x installed
- Required Python packages installed (`requests`, `beautifulsoup4`, `spotipy`, `python-dotenv`)

## Setup

Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add your Spotify credentials and endpoint (see `.env.example` for reference).

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. Enter the date you want to travel to in the format `YYYY-MM-DD`.

3. The script will:
   - Scrape Billboard Hot 100 songs for the specified date.
   - Search for each song on Spotify and retrieve its URI.
   - Create a new private playlist on your Spotify account with the Billboard songs.

## Configuration

- Adjust the Spotify OAuth scope (`scope="playlist-modify-private"`) in `main.py` if necessary.
- Ensure your `.env` file contains correct Spotify API credentials and endpoint.

## Notes

- Songs not found on Spotify will be skipped, and you'll see a message indicating which songs were skipped.
- A token cache (`token.txt`) is used for Spotify OAuth, which is automatically managed by the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Make sure to adjust the details such as `yourusername`, project title, and specific setup instructions according to your actual project structure and preferences. This README provides a clear guide for users to set up, use, and understand your Billboard to Spotify playlist converter project on GitHub.
