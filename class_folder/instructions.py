# This function displays the instruction

def display_instructions():

    #Title design
    instruction_art = """
    ██╗  ██╗ ██████╗ ██╗    ██╗  ████████╗ ██████╗    ██████╗ ██╗      █████╗  ██╗   ██╗                               
    ██║  ██║██╔═████╗██║    ██║  ╚══██╔══╝██╔═████╗   ██╔══██╗██║      ██╔══██╗╚██╗ ██╔╝
    ███████║██║██╔██║██║ █╗ ██║     ██║   ██║██╔██║   ██████╔╝██║      ███████║ ╚████╔╝
    ██╔══██║████╔╝██║██║███╗██║     ██║   ████╔╝██║   ██╔═══╝ ██║      ██╔══██║  ╚██╔╝ 
    ██║  ██║╚██████╔╝╚███╔███╔╝     ██║   ╚██████╔╝   ██║     ███████╗ ██║  ██║   ██║ 
    ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝      ╚═╝    ╚═════╝    ╚═╝     ╚══════╝ ╚═╝  ╚═╝   ╚═╝ 
    """

    instruction_text = """
    The player is the mayor of Ngee Ann City, and the goal of the game is to build the happiest and most
    prosperous city possible, i.e., score the most points. 
    This city-building game begins with 16 coins. In each turn, the player will construct one of two 
    randomly-selected buildings in the 20x20 city. Each construction costs 1 coin. For the first building, 
    the player can build anywhere in the city. For subsequent constructions, the player can only build on 
    squares that are connected to existing buildings. The other building that was not built is discarded. 
    Each building scores in a different way. The objective of the game is to build a city that scores as 
    many points as possible. 

    There are 5 types of buildings:
    • Residential (R): If it is next to an industry (I), then it scores 1 point only. Otherwise, it scores 1 
      point for each adjacent residential (R) or commercial (C), and 2 points for each adjacent park (O). 
    • Industry (I): Scores 1 point per industry in the city. Each industry generates 1 coin per residential 
      building adjacent to it. 
    • Commercial (C): Scores 1 point per commercial adjacent to it. Each commercial generates 1 coin 
      per residential adjacent to it. 
    • Park (O): Scores 1 point per park adjacent to it. 
    • Road (*): Scores 1 point per connected road (*) in the same row.
    """

    print(instruction_art)
    print(instruction_text)

if __name__ == '__main__':
    display_instructions()
