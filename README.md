## Readable Password Generator

RPG is Python port of Niceware implemented with help of Hades, with a few small modifications.
Hades is a complex hashing algorithm written in Python which makes use of the following algorithms to generate a **128-bit hex digest**.

*   Ares (Simple Hashing algorithm)
*   Zeus (Simple Encoding Agoritm)

RPG helps you generate random yet memorable passwords and even keys, which are just few words that are easy to remember.

### Usage

1. Generate the simple set of words by providing a simple seed word/sentence.
```
print(gen_pass_text('Guido van Rossum', 3))  # cyclizing hotfoot explode monthly prorogue benthal
print(gen_pass_text('Guido van Rossum', 4))  # cyclizing hotfoot explode monthly prorogue benthal faithed huh
```
2. The word list can be now converted to a hexadecimal password/key of variable length.
```
print(text_to_pass('cyclizing hotfoot explode monthly prorogue benthal')) #311a663c4a658a20ab541026
```
3. The hexadecimal password can be reversed back to the word list which can be used for validation.
```
print(pass_to_text('311a663c4a658a20ab541026')) # cyclizing hotfoot explode monthly prorogue benthal
```
