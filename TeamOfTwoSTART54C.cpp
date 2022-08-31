#include <bits/stdc++.h>
//#include<iostream>
using namespace std;
int main()
{
    int n, a, b, c, d;
    // vector<int> vector;
    set<int> set;
    cin >> n;
    while (n--)
    {
        cin >> a;
        vector<vector<int>> vect;
        for (int i = 0; i < a; i++)
        {
            int val, j = 0;
            while (cin >> val)
            {
                vect[i][j] = val;
                j++;
            }
        }

        for (int i = 0; i < vect.size(); i++)
        {
            for (int j = 0; j < vect[i].size(); j++)
            {
                cout << vect[i][j] << " ";
            }
            cout << endl;
        }
    }
    return 0;
}