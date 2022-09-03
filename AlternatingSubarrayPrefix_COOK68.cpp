#include <bits/stdc++.h>
//#include<iostream>
using namespace std;
int main()
{
int n,a;
set<int> set;
cin>>n;
while(n--)
{
    cin>> a;
    int vec[a];
    for(int i=0;i<a;i++){
        int val;
        cin >> val;
        vec[i]=val;
    }
    for(int i=0;i< a;i++){

        int count =1;
        char c;
        if(vec[i] <0)
            c='-';
        else
            c='+';
        // cout <<c << endl;
        for (int j = i+1; j < a; j++)
        {
            if (vec[j] < 0 && c =='+')
                c = '-'; 
            else if (vec[j] > 0 && c == '-')
                c = '+';
            
            else
                break;
                count ++;
            }
        cout << count << " ";
        
    }
    cout << endl;
}
    return 0;
}