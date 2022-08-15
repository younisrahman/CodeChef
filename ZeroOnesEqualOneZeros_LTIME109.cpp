#include <bits/stdc++.h>
//#include<iostream>
using namespace std;
int main()
{
    int n, a, b, c, d;
    vector<int> vector;
    set<int> set;
    cin >> n;
    while (n--)
    {
        cin >> a;
        if (a > 3)
        {
            for (int i = 0; i < a; i++)
            {
                if (i == 0 || i == (a - 1))
                {
                    cout << 1;
                }
                else
                {
                    cout << 0;
                }
            }
            cout << endl;
        }
        else
        {
            for (int i = 0; i < a; i++)
            {
                if (i == 0 || i == (a - 1))
                {
                    cout << 0;
                }
                else
                {
                    cout << 1;
                }
            }
            cout << endl;
        }
    }
    return 0;
}