from googletrans import Translator
import time

trans = Translator()

file_path = "/Users/thanhlevan/Documents/code/FilmSub/Nayakan/Nayagan.srt"


def translate_text(text):
    trans_result = trans.translate(text, src="en", dest="vi")
    time.sleep(0.4)
    return trans_result.text


def cut_string(input_str):
    # Get the length of input string
    length = len(input_str)

    # Get the middle position
    mid_pos = length // 2

    # Check if the middle position is a space
    if input_str[mid_pos] == " ":
        return input_str[:mid_pos] + "\n" + input_str[mid_pos + 1 :]

    # Look for the closest space to the middle position
    for i in range(mid_pos, length):
        if input_str[i] == " ":
            return input_str[:i] + "\n" + input_str[i + 1 :]
        if input_str[length - i - 1] == " ":
            return input_str[: length - i - 1] + "\n" + input_str[length - i :]

    # If no space is found, just add a space in the middle
    return input_str[:mid_pos] + "\n" + input_str[mid_pos + 1 :]


result = ""


with open(file_path, "r", encoding="utf-8") as file:
    list_line = []
    for box in file.read().split("\n\n"):
        list_text = box.split("\n")
        speech = " ".join(list_text[2:])
        print(speech)

        translate_result = ""
        if speech.startswith("<i>"):
            new_speech = speech[3:-4]
            try:
                translate_result = translate_text(new_speech)
                translate_result = "<i>" + translate_result + "</i>"
            except:
                translate_result = new_speech

        else:
            try:
                translate_result = translate_text(speech)
            except:
                translate_result = speech

        try:
            if len(translate_result) >= 60:
                result += (
                    list_text[0]
                    + "\n"
                    + list_text[1]
                    + "\n"
                    + cut_string(translate_result)
                    + "\n\n"
                )
            else:
                result += (
                    list_text[0]
                    + "\n"
                    + list_text[1]
                    + "\n"
                    + translate_result
                    + "\n\n"
                )
        except:
            pass


with open(file_path[:-4] + "_vietsub.srt", "w", encoding="utf-8") as file:
    file.write(result)
