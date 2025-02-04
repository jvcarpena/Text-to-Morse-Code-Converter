# Text to Morse Code Converter

## Description
This Python program converts user-provided text into Morse code. It provides a simple interface where users can input a word or phrase and see its Morse code equivalent. Users can continue encoding multiple words/phrases or exit the program when done.

---

## Features
- Converts text (including spaces) into Morse code using a predefined dictionary (`BOOK`).
- Handles minor spaces, major spaces, and twin spaces appropriately for Morse code formatting.
- Includes user-friendly prompts and exit options.

---

## Requirements
- Python 3.x
- A dictionary module named `dictionary.py` that contains a `BOOK` variable (mapping text characters to Morse code).

---

## How to Run the Program
1. Clone or download the repository.
2. Ensure the `dictionary.py` file is present and contains a `BOOK` dictionary mapping text characters to Morse code.
3. Run the `morse_encoder.py` file:
   ```bash
   python morse_encoder.py
   ```
4. Follow the prompts to input text and see the Morse code output.

---

## Program Flow
1. **Welcome Message**:
   Displays an ASCII art welcome message for the user.
2. **User Input**:
   Prompts the user to input a word or phrase to encode into Morse code.
3. **Encoding**:
   Converts the input into Morse code using the `BOOK` dictionary.
4. **Output**:
   Displays the converted Morse code.
5. **Exit Option**:
   Asks the user if they want to encode another word ("y" to continue, "n" to exit).
6. **Goodbye Message**:
   Displays an ASCII art goodbye message when the user exits.

---

## Key Functions
- **`get_morse(word)`**:
  Converts the input text into a list of Morse code characters, handling spaces and formatting.
- **`output(code)`**:
  Joins the Morse code list into a single string for output.
- **`user_input()`**:
  Prompts the user for a word or phrase to encode.
- **`exit_input()`**:
  Prompts the user to decide whether to continue or exit the program.
- **`main()`**:
  The entry point of the program, orchestrating input, encoding, and output.

---

## Example Usage
1. **Run the program**:
   ```
   Welcome to my Text to Morse Code Converter!!

   Enter a word you want to convert into Morse code: hello

   The result of the conversion is: .... . .-.. .-.. ---

   You want to convert another word? Please enter 'y' or 'n': y
   ```

2. **Exit the program**:
   ```
   You want to convert another word? Please enter 'y' or 'n': n

   Thank you for using my Text to Morse Code Converter

       +-+-+-+-+-+-+-+
       |G|o|o|d|B|y|e|
       +-+-+-+-+-+-+-+
   ```

---

## Customization
- Modify the `BOOK` dictionary in `dictionary.py` to include additional characters or symbols.
- Adjust the `WELCOME_MESSAGE` and `GOODBYE_MESSAGE` ASCII art for a personalized touch.

---

## License
This project is open source. Feel free to modify and distribute it as needed.

