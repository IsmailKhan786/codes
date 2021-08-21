#include <iostream>

using namespace std;

int main()
{
    int x;
    int y;
    int z;
    cout << "Enter the Number 1:"<<endl;
    cin>>x;
    cout<<"Enter the Number 2:"<<endl;
    cin>>y;
    cout<<"Enter the Number 3:"<<endl;
    cin>>z;

    if(x>y && x>z){
        cout<<"The Largest Number is" <<x;

    }

    else if(y>x && y>z){
            cout<<"The Largest Number is"<<y;
    }
    else{
        cout<<"The Largest Number is"<<z;
    }

}


