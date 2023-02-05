def main():
    kanidaten = {"Scholz":0,"Laschet":0,"Baerbock":0}
    for _ in range(10):
        kanidaten[list(kanidaten)[int(input(construct_vote_str(list(kanidaten))))-1]] += 1
    print(construct_result_str(kanidaten))

def construct_vote_str(kanidaten: list):
    output = "Bitte Wählen sie ihren kanidaten:\n"
    for i, j in enumerate(kanidaten,1):
        output += f"{i}: {j}\n"
    return output

def construct_result_str(kanidaten: dict):
    output = "die resultate der Wahl sind: \n"
    for kanidat, stimmen in kanidaten.items():
        output += f"{kanidat}: {stimmen}\n"
    return output    
            
    
if __name__ == "__main__":
    main()