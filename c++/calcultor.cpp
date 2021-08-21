#include <iostream>

using namespace std;

int main()
{
    /*calculator*/
    int a,b;
    int c;
    cout<<"Enter Number 1"<<endl;
    cin>>a;
    cout<<"Enter Number 2"<<endl;
    cin>>b;

    cout<<"Press 1 for Addition \n Press 2 for Multiplication \n Press 3 for Division  "<<endl;
    cin>>c;

    if(c==1){
        int z=a+b;
        cout<<"The addition od two number is :" <<z;
    }
    else if(c==2){
        int z=a*b;
    cout<<"The Multiplication of two number is:"<<z;
    }
    else if(c==3){
        int z=a/b;
        cout<<"The division of two number is :"<<z;
    }
    else {
         cout<<"Wrong Input"<<endl;
    }



}


