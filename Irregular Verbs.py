verbos = {"arise": ["arose", "arisen"], "awake": ["awake/awaked", "awaken"], "be": ["was/were", "been"],
          "bear": ["bore", "born/borne"], "beat": ["beat", "beaten"], "became": ["became", "become"],
          "begin": ["began", "begun"], "bend": ["bent", "bent"], "bet": ["bet", "bet"], "bind": ["bound", "bound"],
          "bite": ["bit", "bitten"], "bleed": ["bled", "bled"], "blow": ["blew", "blown"], "break": ["broke", "broken"],
          "bring": ["brought", "brought"], "build": ["built", "built"], "burn": ["burnt/burned", "burnt/burned"],
          "burst": ["burst", "burst"], "buy": ["bought", "bought"], "cast": ["cast", "cast"],
          "catch": ["caught", "caught"], "choose": ["chose", "chosen"], "cling": ["clung", "clung"],
          "come": ["came", "come"], "cost": ["cost", "cost"], "creep": ["crept", "crept"], "cut": ["cut", "cut"],
          "deal": ["dealt", "dealt"], "dig": ["dug", "dug"], "do": ["did", "done"], "draw": ["drew", "drawn"],
          "dream": ["dreamt/dreamed", "dreamt/dreamed"], "drink": ["drank", "drunk"], "drive": ["drove", "driven"],
          "dwell": ["dwelt", "dwelt/dwelled"], "eat": ["ate", "eaten"], "fall": ["fell", "fallen"],
          "feed": ["fed", "fed"], "feel": ["felt", "felt"], "fight": ["fought", "fought"], "find": ["found", "found"],
          "flee": ["fled", "fled"], "fling": ["flung", "flung"], "fly": ["flew", "flown"],
          "forbid": ["forbade/forbad", "forbidden"], "forget": ["forgot", "forgotten"],
          "forgive": ["forgave", "forgiven"]}


def lin(q):
    return "\033[0;30;43m~"*q


def msg(a):
    print(lin(40))
    print(f"\033[0;30;43m{a.upper():^40}")
    print(lin(40))


def ascii():
    print("\033[1;35m   /\ \/\ \                  /\ \               ")
    print("   \ \ \ \ \     __    _ __  \ \ \____    ____  ")
    print("    \ \ \ \ \  /'__`\ /\`'__\ \ \ '__`\  /',__\ ")
    print("     \ \ \_/ \/\  __/ \ \ \/   \ \ \L\ \/\__, `")
    print("      \ `\___/\ \____\ \ \_\    \ \_,__/\/\____/")
    print("       `\/__/  \/____/  \/_/     \/___/  \/___/ \033[m")


clear = "\n" * 1000
s = 0
while True:
    ascii()
    while True:
        d = str(input("\033[m\033[1;32m>>\033[m \033[1;33mDigite o verbo:\033[m [\033[1;32mINFINITIVO\033[m]\033[m \033[0;32mTo \033[m")).lower()
        if d in verbos:
            break
        else:
            s += 1
            print(clear)
            print(f"\033[0;30;41m [{s}] Palavra inválida! Tente novamente.", end="\n")
    print(clear)
    print(lin(60))
    print(f"{'INFINITIVE':<15}{'PAST TENSE':<18}{'PAST PARTICIPLE':}")
    print(lin(60))
    print(f"{f'To {d}':<14} {verbos[f'{d}'][0]:<17} {verbos[f'{d}'][1]}")
    print(lin(60))
    while True:
        r = str(input("\033[m\033[1;32m>>\033[m \033[1;33mDeseja continuar? [S/N]:\033[m ")).upper()[0]
        if r == "S" or r == "N":
            break
    if r == "N":
        break
    else:
        s = 0
        print(clear)
print(clear)
print("\033[0;30;42mObrigado, volte sempre! :D\033[m")