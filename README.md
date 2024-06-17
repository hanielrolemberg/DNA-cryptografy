Description
DNA Encryption Method

The DNA encryption method leverages the concept of mapping characters to unique pairs of characters, inspired by the way biological DNA sequences encode information. Each character in the message is encoded using a predefined dictionary that maps characters to two-character sequences. This method ensures that the original message is transformed into an encoded string, which can then be decoded back to the original message using the reverse mapping dictionary.

Encryption: Each character in the input message is replaced with a corresponding two-character sequence from the encoding dictionary.
Decryption: The encoded message is split into pairs of characters, and each pair is mapped back to the original character using the decoding dictionary.
This approach allows for secure and reversible transformation of messages, ensuring that the information can be safely encoded and later decoded.

Installation
To run the DNA encryption method on your local machine, follow these steps:

Install Python: Ensure you have Python installed on your machine. You can download it from python.org.

Set Up the Script:

Create a new directory for your project.
Inside this directory, create a new Python file, e.g., dna_encryption.py.
Copy the Code:

Copy the following code into your dna_encryption.py file:
python
Copy code
import random

Run the Script:

Open a terminal or command prompt.
Navigate to the directory where you saved dna_encryption.py.
Run the script using the command:
sh
Copy code
python dna_encryption.py
Enter the Message:

When prompted, enter the message you wish to encrypt.
The script will display the original message, the encrypted message, and the decrypted message.
