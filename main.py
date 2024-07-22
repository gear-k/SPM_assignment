from class_folder.board import Board
from class_folder.arcade import Arcade
from class_folder.freeplay import Freeplay
from class_folder.external import External


# ASCII art for the game title
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

TITLE = """
              *******************************
              *                             *
              *  Welcome to Ngee Ann City   *
              *       Building Game!        *
              *                             *
              *******************************
"""

def display_main_menu():
    # Main menu loop
    while True:
        try:
            print(ART)
            print(TITLE)
            print("1. Start New Arcade Game")
            print("2. Start New Free Play Game")
            print("3. Load Saved Game")
            print("4. Display High Scores")
            print("5. Exit Game")
            print("---------------------------------")
            choice = input("Enter your choice: ")
            choice = choice.replace(" ", "") # This feature allows the input to accept spacebars by auto removing them
            if choice == '1':
                Arcade.start_new_arcade_game()
            elif choice == '2':
                Freeplay.start_new_free_play_game()
            elif choice == '3':
                # The following 4 lines allow the player to cancel in the event they do not want to enter option 3
                confirm_load = input("You selected Load Saved Game. Type 'cancel' to abort or press Enter to continue: ").lower()
                confirm_load = confirm_load.replace(" ", "") # This allows the input to accept spacebars by auto removing them
                if confirm_load == 'cancel':
                    print("Load Saved Game aborted.")
                    continue
                game = External.load_saved_game()
                if game:
                    if game['mode'] == 'arcade':
                        Arcade(0, game['turn'], game['spec'], Board(game['board'])).play_arcade_game()
                    elif game['mode'] == 'freeplay':
                        Freeplay("Easy", 0, game['turn'], game['spec'], Board(game['board'])).play_free_play_game()
            elif choice == '4':
                high_scores = External.load_high_scores()
                External.display_high_scores(high_scores)
            elif choice == '5':
                exit_game()
                break
            else:
                print("Invalid choice, please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

def exit_game():
    # Exit the game
    print("Exiting the game. Goodbye!")

if __name__ == '__main__':
    display_main_menu()
