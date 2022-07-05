x=1
while (x==1):

    st_name: str = input("Enter student's name: ")

    abscent_or_not = input("For a normal absence type ENTER, if it is a regularly absent student, type 1: ")

    prefixes = ["Hey, ",
                "Olá, ",
                "Hey there, ",
                "Hi there, "]
    suffixes_normal_absence = [", senti sua falta na aula! Gostaria de tentar repor?",
               ", faltou na nossa aula, tudo certo por aí? Gostaria de tentar repor? ",
               ", faltou à aula, tudo certo por ai? Como posso te ajudar a frequentar nossas aulas?",
               ", gostaria de tentar repor a aula que faltou? Let me know. 😊",
               ", não conseguiu ver a nossa aula! Gostaria de repor? Let me know! 😊",
               ", faltou na nossa aula! Sentimos sua falta! Como posso te ajudar a frequentar nossas aulas?"]
    suffixes_absent_student = [", estou preocupado com suas faltas, o que posso fazer para te ajudar a frequentar nossas aulas? 🤔🤓😀",
                              ", notei que você tem faltado bastante, tudo certo por ai? Como posso fazer para te ajudar a frequentar nossas aulas? 🤔🤓😀",
                              ", você tem faltado bastante, será que podemos pensar numa estratégia para te ajudar a frequentar nossas aulas? Let me know! 🤔🤓😀",
                              ", estava dando uma olhada nas suas frequências e percebi que você tem faltado bastante. será que podemos pensar numa estratégia para te ajudar a frequentar nossas aulas? Let me know! 🤔🤓😀",
                              ", estou preocupado com suas faltas, estava dando uma olhada nas suas frequências e percebi que você tem faltado bastante. Como posso fazer para te ajudar a frequentar nossas aulas? 🤔🤓😀"]

    import random

    z = random.randint(0, len(suffixes_absent_student) - 1)

    n = random.randint(0, len(suffixes_normal_absence) - 1)

    i = random.randint(0, len(prefixes) - 1)

    chosen_suffix = "a"

    if abscent_or_not == "" :
       chosen_suffix = suffixes_normal_absence[n]
    elif abscent_or_not == "1" :
        chosen_suffix = suffixes_absent_student[z]
    else :
        print("Sorry, I couldn't understand your solicitation...")

        import sys
        sys.exit(1)

        # Função para criar o sufixo dependendo da escolha de abstenção
    #def get_chosen_suffix(is_regularly_abscent):
     #   if is_regularly_abscent == "1":
      #      z = random.randint(0, len(suffixes_absent_student) - 1)
       #     return suffixes_absent_student[z]
        #elif is_regularly_abscent == "0":
         #   n = random.randint(0, len(suffixes_normal_absence) - 1)
          #  return suffixes_normal_absence[n]
            #else:
            #print("Sorry")
            #import sys
            #sys.exit(1)

        #return "teste"

    #chosen_suffix = get_chosen_suffix(abscent_or_not)

    #clipboard_sentence = prefixes[i] + st_name + chosen_suffix

    print_list = prefixes[i] + st_name + chosen_suffix

    print(print_list)

    import pyperclip

    pyperclip.copy(print_list)

    spam = pyperclip.paste()
else:

    x = int(input("Do you wish to use the program again?: 1 for yes - 2 for no: "))
    print(" ")


    input()

