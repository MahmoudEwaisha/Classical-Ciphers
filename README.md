# Python implementation of some of the classical ciphering techniques

This library contains 5 classical ciphering techniques namely:
* Ceaser
* Hill
* Playfair
* Vernam
* Vigenere

If you run the python file, it'll first ask you to choose a ciphering technique, then takes the plaintext and the key as inputs (also takes other inputs like the choice of a 2x2 or a 3x3 matrix in Hill cipher, or the choice of repeating or auto mode in Vigenere cipher, etc), and finally outputs the ciphertext.

The library is robust to some potential issues, like entering spaces in the plaintext or key, using uppercase or lowercase letters, entering non-alphabet symbols, nonmatching matrices dimensions (in Hill cipher), entering characters instead of numbers and vice-versa, and other potential misuse by the user.
