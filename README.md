# ChooseElectric Bot

## Description

ChooseElectric is a Telegram bot designed to help users decide if switching to an electric vehicle is a viable option for them. Based on the information provided by the user, the bot utilizes the OpenAI API to analyze data about the user's current car model, monthly consumption, and other relevant factors to suggest electric alternatives. It also calculates potential savings in costs and emissions. The bot uses a fine-tuned language model to enable natural conversations and provide personalized recommendations.

The bot can be found on Telegram using the username: [@whyAnElectricCarBot](https://t.me/whyAnElectricCarBot).

---

## Features

- Automatically responds to user messages on Telegram.
- Analyzes information about vehicles and fuel consumption.
- Calculates monthly and annual costs for gasoline or electricity.
- Recommends electric vehicle alternatives with links for more information.
- Integrates OpenAI's fine-tuned language model for enhanced conversational abilities.

---

## Technologies Used

- **Programming Language:** Python
- **APIs Used:**
  - Telegram Bot API
  - OpenAI API (fine-tuned model)
- **Main Libraries:**
  - `openai`
  - `requests`
  - `time`

---

## Requirements

- Python 3.7 or higher
- Access keys for:
  - Telegram Bot API
  - OpenAI API

### Installing Dependencies
Run the following command to install the required dependencies:
```bash
pip install openai requests
```

---

## Configuration

1. **Create a bot on Telegram:**
   - Go to [BotFather](https://core.telegram.org/bots#botfather).
   - Create a new bot and obtain the **TOKEN**.

2. **Generate an OpenAI API Key:**
   - Go to [OpenAI API Keys](https://platform.openai.com/account/api-keys).
   - Generate a new API key and save it.

3. **Set up the keys in the code:**
   - Replace `TOKEN` with your Telegram bot token.
   - Replace `api_key` with your OpenAI key.

---

## Usage

1. Run the bot from the terminal:
   ```bash
   python data_analisys.py
   ```

2. Open Telegram and find your bot by searching for [@whyAnElectricCarBot](https://t.me/whyAnElectricCarBot).

3. Send a message to the bot with information such as:
   - Your current car model.
   - The number of kilometers you drive monthly.

4. The bot will respond with:
   - Costs of your current vehicle.
   - Estimated costs for an electric vehicle.
   - Potential savings.
   - Recommendations for electric vehicles.

---

## Project Structure

```
chooseElectric/
|-- data_analisys.py       # Main bot file
|-- README.md              # Project documentation
|-- requirements.txt       # Dependency list
```

---

## Example Conversation

**User:** I have an Audi A8 2020 and drive approximately 700 km per month.  
**Bot:** 
- The Audi A8 2020 consumes 8 liters of gasoline per 100 km.
- With your monthly commute, you would spend 56 liters.
- This equals €100.8 per month (with gasoline at €1.8/L).
- An electric vehicle like the Tesla Model 3 would consume 140 kWh per month (€42).
- Estimated monthly savings: €58.8 (€705.6 annually).
- [Learn more about the Tesla Model 3](https://www.tesla.com/model3).

---

## Notes

- Ensure your bot has internet access to interact with the APIs.
- Monitor OpenAI usage limits to avoid exceeding your budget.

---

## Contributions

Contributions are welcome. Please open an [issue](https://github.com/Sergio2205/public_chooseElectric/issues) or create a pull request to discuss changes.

---

## Repository

The code for this bot is available on GitHub: [ChooseElectric Repository](https://github.com/Sergio2205/public_chooseElectric).

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

