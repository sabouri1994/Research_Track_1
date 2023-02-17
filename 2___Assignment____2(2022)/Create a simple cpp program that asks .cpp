//Create a simple cpp program that asks the user to insert a number, and then checks if the inserted number is equal to 3.

#include <iostream>
using namespace std;

int main() {
    int number;
    cout << "Insert a number: ";
    cin >> number;
    if (number == 3) {
        cout << "The number is equal to 3";
    }
    else {
        cout << "The number is not equal to 3";
    }
    return 0;
}

