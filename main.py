from class_folder.board import Board
from class_folder.arcade import Arcade
from class_folder.freeplay import Freeplay
from class_folder.external import External

ART = """
                            *##*                            
                         *##*  *##*                         
                     *###*        *##*                      
                  *###*        @@@   *##**                  
               *###*        @@@@@@@     *##**               
            *###         @@@@@@@@@          ###=            
         *##*         @@@@@@@@@@@-     @@@@    *##*         
      *##*         @@@@@@@  @@@@@   @@@@@@@       *##*      
      ####*     @@@@@@@    @@@@@ @@@@@@@        **####      
      #*  *##**  @@@      @@@@@@@@@@@        **##*  ##      
      #*     *##*         @@@@@@@@        =*##*     ##      
      #*        *###     @@@@@          ###-        ##      
      #*           *###*            *###            ##      
      #*        @@@   **##*      *##**  @@@@@@      ##      
      #*       @@@@@     *###**##**   @@@@@@@@@     *#      
      #*       @@@@@         ##      @@@@  @@@@     *#      
      #*      -@@@@@         ##     @@@    *@       *#      
      #*      @@@@@@@        ##    @@@              *#      
      #*      @@@%@@@        ##    @@@              *#      
      #*     @@@@ @@@        ##    @@@      @@@     *#      
      #*     @@@@@@@@#       ##    @@@     +@@@     *#      
      #*    @@@@@@@@@@       ##    @@@.    @@@      *#      
      ##*   +@@@  @@@@       ##    @@@@ .@@@@      *##      
        *##*       @@@       ##    @@@@@@@@-    ###*        
           *##*=   .@@@      ##     @@@@@   *###*           
              *###*  :@      ##          *###*              
                 *###*       ##       *###-                 
                     ###*    ##    *##*                     
                        *##*:## *##*                        
                           *####*                           
"""

def display_main_menu():
    while True:
        print(ART)
        print("Welcome to Ngee Ann City Building Game!")
        print("1. Start New Arcade Game")
        print("2. Start New Free Play Game")
        print("3. Load Saved Game")
        print("4. Display High Scores")
        print("5. Exit Game")
        choice = input("Enter your choice: ")
        if choice == '1':
            Arcade.start_new_arcade_game()
        elif choice == '2':
            Freeplay.start_new_free_play_game()
        elif choice == '3':
            game = External.load_saved_game()
            if game['mode'] == 'arcade':
                Arcade(0, game['turn'], game['spec'], Board(game['board'])).play_arcade_game()
            elif game['mode'] == 'freeplay':
                Freeplay(0, game['turn'], game['spec'], Board(game['board'])).play_free_play_game()
        elif choice == '4':
            high_scores = External.load_high_scores()
            External.display_high_scores(high_scores)
        elif choice == '5':
            exit_game()
            break
        else:
            print("Invalid choice, please try again.")

def exit_game():
    print("Exiting the game. Goodbye!")

if __name__ == '__main__':
    display_main_menu()
