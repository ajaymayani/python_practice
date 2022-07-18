def english_to_morse_code(morse_code, letters, user_input):
    morse_list = []
    for char in user_input:
        for index in range(len(letters)):
            if char == letters[index]:
                morse_list.append(morse_code[index])
    return morse_list


def morse_code_to_english(morse_code, letters, user_input):
    for code in user_input:
        for index in range(len(letters)):
            if code == morse_code[index]:
                print(letters[index], end="")


if __name__ == '__main__':
    letters = ['a', 'b', 'c', 'd', 'e', 'f',
               'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x',
               'y', 'z', '1', '2', '3', '4',
               '5', '6', '7', '8', '9', '0',
               '.', ',', '?', '@', "!", "&",
               "(", ")", '=', '+', '/', ':', '\'', '\"']

    morse_code = [".-", "-...", "-.-.", "-..", ".",
                  "..-.", "--.", "....", "..", ".---",
                  "-.-", ".-..", "--", "-.", "---",
                  ".--.", "--.-", ".-.", "...", "-",
                  "..-", "...-", ".--", "-..-", "-.--",
                  "--..", ".----", "..---", "...--",
                  "....--", ".....", "-....", "--..",
                  "---..", "----.", "-----", ".-.-.-",
                  "--..--", "..--..", ".--.-.", "-.-.--",
                  ".-...", "-.--.", "-.--.-", "-...-",
                  ".-.-.", "-..-.", "---...", ".----.", ".-..-."];

    except_letter = ['#', '$', '%', '^', '*', '`', '~', '[', ']', '{', '}', ';', '>', '<', ' ']

    user_input = input("Enter name to convert morse code : ")

    for char in user_input:
        for ex in except_letter:
            if char == ex:
                print(f"'{char}' Cannot translate into morse code ")

    morse_list = english_to_morse_code(morse_code, letters, user_input)
    print("English text to morse code : ")
    for code in morse_list:
        print(code, end=" ")
    print("\nMorse code to english text : ")
    morse_code_to_english(morse_code, letters, morse_list)
