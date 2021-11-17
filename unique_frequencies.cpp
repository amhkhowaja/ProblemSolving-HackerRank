/*
Problem :
When Eleven is trying to find contact with Will, the guys need to set the radio frequency to various values. Given the list of frequencies they tried, can you determine how many different values are in the list?

Input
The first line of the input contains n (1≤n≤100) – the number of frequencies. The second line contains n positive integers f1,f2,…,fn (1≤fi≤1000) – the frequencies that the guys tried.

Output
Your program should print a single number, the number of different values in the list.

Example
inputCopy
7
172 100 135 172 81 135 81
outputCopy
4
Note
Explanation: there are 4 different values in this sequence: 81, 100, 135 and 172.

*/
#include <iostream>
#include <vector>
#include <algorithm>
 
using namespace std;
 
int main(){
    int n; 
    cin>>n;
    vector <int> uniq;
    int freq [n];
    for (int i = 0; i < n; i++)
    {
        cin>>freq[i];
        if (!(find(uniq.begin(), uniq.end(), freq[i] ) != uniq.end())){
            uniq.push_back (freq[i]);
        }
    }
    cout<<uniq.size();
 
    // Logic
    
}
