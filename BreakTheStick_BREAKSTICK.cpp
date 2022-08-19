#include <bits/stdc++.h>
//#include<iostream>
using namespace std;
int main()
{
    int n, a, b, c, d;

    cin >> n;
    while (n--)
    {
        cin >> a >> b;
        if (a % 2 == 0 && b <= a)
        {
            cout << "YES" << endl;
        }
        else if (b % 2 == 0)
        {
            cout << "NO" << endl;
        }
        else
        {
            cout << "YES" << endl;
        }
    }
    return 0;
}