#include<iostream>
#include <string> 
#include <cstdlib>

using namespace std;
void rules();

int main(){

    string playername;
    int balance; 
    int bettingamount;
    int guess;
    int dice; 
    char choice;

    cout << "\n\t\t !======== WELCOME TO CASINO WORLD =======! \n\n";
    cout << "\n\n What's your Name : ";
    getline(cin, playername);

    cout << "\n Enter the starting balance to play game : $";
    cin >> balance ;

    do{
        cout << "\n\n Your current balance is $ " << balance << endl;

        system("cls");
        rules();

        do
        {
            cout << "Hey! " << playername<<", enter amount to bet : $";
            cin >> bettingamount;
            if(bettingamount > balance){
                cout << "Betting balance can't be more than current balance!" << endl;
                cout << "Re enter the betting amount!" << endl;
            }
                
        }while(bettingamount > balance);


         do
        {
            cout << "Guess any betting number between 1 & 10 : ";
            cin >> guess;
            if(guess <= 0 || guess > 10)
                cout << "\n Number should be between 1 to 10! " << endl;
                cout << "Re-enter number: \n ";
        }while(guess <= 0 || guess > 10);

        dice = rand()%10 + 1;
        if(dice == guess)
        {
            cout << "\n You are lucky!! You have won $ " << bettingamount * 10;
            balance = balance + bettingamount * 10;
        }
        else
        {
            cout << "Oops, better luck for the next time !! You lost $ " << bettingamount << endl;
            balance = balance - bettingamount;
        }
        cout << "\n The winning number was : " << dice << endl;
        cout << "\n"<<playername<< " You have balance of $ " << balance << endl;


        if(balance == 0)
        {
            cout << " SORRY! You have no money to play  -_-' ";
            break;
        }
        cout << "\n\n-->Do you want to play again (y/n)? ";
        cin >> choice;
    }while(choice =='Y'|| choice=='y');

    cout << "\n\nThanks for playing the game. Your balance is $ " << balance << "\n\n";
    return 0;
} 

void rules()
{
    system("cls");
    cout << "\t\t !======CASINO NUMBER GUESSING RULES!======! \n";
    cout << "\t  1. Choose a number between 1 to 10 \n";
    cout << "\t  2. Winner gets 10 times of the money bet \n";
    cout << "\t  3. Wrong bet, and you lose the amount you bet \n\n";
}