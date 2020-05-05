# cryptbrute
This program is designed to speed up ctf challenges that use ancient ciphers by looping through some of the most common ones. It assumes that you are using google chrome.

Requirements: pycipher,webbrowser, selenium

Before running the program, you must download the appropriate ChromeDriver file and type it's absolute path into the appropriate location in the script.

Then open a terminal and run 'sudo chmod +x cryptbrute.py' and then 'python3 stegbrute.py'.

The program will ask you to input the ciphertext. Follow the instructions. Google chrome will open to a site and utilze its recources to brute for that vigenere cipher. The other ciphers will completed on the terminal. The results for the non-vigenere ciphers will be saved to files within the same directory from where the program in run.

If you have any questions or comments, please feel free to comments.
