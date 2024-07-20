# HappyFox Backend Assignment

## Scope of the Application

This application is designed to integrate with the Gmail API to fetch emails, store them in a SQLite3 database, and process them based on a set of predefined rules specified in a JSON file. The application performs the following key functions:

1. **Authentication**: Uses OAuth2 to authenticate with the Gmail API.
2. **Email Fetching**: Retrieves emails from the user's Gmail inbox.
3. **Database Storage**: Stores fetched emails in a SQLite3 database.
4. **Rule-Based Processing**: Processes emails based on rules defined in a JSON file, applying specified actions to the emails.
5. **Logging**: Logs significant events and actions to facilitate debugging and monitoring.
6. **Testing**: Includes unit tests to verify the functionality of the rule processing logic.

## Demo Video

- **To see the installation setup and how to use the application, watch the demo video**: https://youtu.be/AhQl7VH_ITU

## Setup

1. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

2. Obtain and configure `credentials.json` for Gmail API:

   - **Go to the Google Cloud Console**: Visit [Google Cloud Console](https://console.cloud.google.com/).
   - **Create a new project**: If you don't have a project, create one by clicking on the project dropdown and selecting "New Project".
   - **Enable the Gmail API**:
     - Go to the API Library.
     - Search for "Gmail API".
     - Click on "Enable" to enable the API for your project.
   - **Create OAuth 2.0 Credentials**:
     - Go to the "Credentials" tab.
     - Click on "Create Credentials" and select "OAuth 2.0 Client IDs".
     - Configure the consent screen if you haven't done so already.
     - Select "Desktop app" as the application type.
     - Click "Create".
   - **Download the credentials**: Once created, you will be prompted to download the `credentials.json` file. Download and save it in your project directory.

3. Configure the application in `config.py`.

4. Authenticate to Gmail and fetch emails:

   ```sh
   python fetch_emails.py
   ```

5. Process emails based on rules:
   ```sh
   python process_emails.py
   ```

## Running Tests

```sh
python -m unittest discover tests
```

## Notes

- Ensure you have a valid Gmail API credential file and token file.
- Update the database URL in the config.py file as per your setup.
- Place your rules in a rules.json file in the root directory.
