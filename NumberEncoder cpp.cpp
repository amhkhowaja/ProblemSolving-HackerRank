#include <iostream>
#include <string>
using namespace std;
string encode(int arr[],int n){
    string encoded="";
    for (int step = 0; step < n - 1; ++step) {
        for (int i = 0; i < n - step - 1; ++i) {

        // To sort in descending order, change > to < in this line.
            if (arr[i] > arr[i + 1]) {

                // swap if greater is at the rear position
                int temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
            }
        }
    }
    for (int i=0;i<n;i++){
        for(int i=0;i<arr[i];i++){
            encoded=encoded+to_string(1);
        }
        encoded=encoded+"-";
    }
    return encoded;
}
string decoder(string ones[], int n){
    //1111 11 11111
    int *numbers=new int[n];
    //decoder 
    for (int i =0;i<n;i++){
        int x=ones[i].length();
        
        numbers[i]=x;
    }
    //sorting
    for (int step = 0; step < n - 1; ++step) {
        for (int i = 0; i < n - step - 1; ++i) {

        // To sort in descending order, change > to < in this line.
            if (numbers[i] > numbers[i + 1]) {

                // swap if greater is at the rear position
                int temp = numbers[i];
                numbers[i] = numbers[i + 1];
                numbers[i + 1] = temp;
            }
        }
    }
    string decoded="";
    for (int i=0;i<n;i++){
        decoded+=to_string(numbers[i]);
		decoded+="-";
    }
    return decoded;
}
int main(){
    //INPUT
    cout<<"Enter your choice:"<<endl;
    cout<<"1. Encoder"<<endl;
    cout<<"2. Decoder"<<endl;
    int ch;
    cin>>ch;
    switch(ch)
    {
        case 1: 
        {
            cout<<"Enter the number of test cases: ";
            int number;
            cin>>number;
            int x=0;
            for (int i=0; i<number;i++){
                cin>>x;
                int *arr=new int[x];
                for(int i=0;i<x;i++){
                    cin>>arr[i];
                    //cout<<encode(arr,x);
                }
                cout<<encode(arr,x);
            }
        }
        break;
        case 2:
        {
            cout<<"Enter the number of the test cases"<<endl;
            int number;
            cin>>number;
            int x=0;
            for (int i=0; i<number;i++){
                cin>>x;
                string *arr=new string[x];
                for(int i=0;i<x;i++){
                    cin>>arr[i];
                    //cout<<encode(arr,x);
                }
                cout<<decoder(arr,x)<<endl;
            }
        }
        break;
        default:
        cout<<"Wrong Input"<<endl;
        break;
    }
    
    system("pause");
    return 0;
}
