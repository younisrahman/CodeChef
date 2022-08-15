#include <bits/stdc++.h>
//#include<iostream>
using namespace std;
int main()
{
    int n, a, b, c, d;

    cin >> n;
    while (n--)
    {
        vector<int> vector;
        cin >> a >> b;
        for (int i = 0; i < a; i++)
        {
            cin >> c;
            if (b - c >= 0)
            {
                b -= c;
                vector.push_back(1);
            }
            else
            {
                vector.push_back(0);
            }
        }
        for (int i = 0; i < vector.size(); i++)
        {
            cout << vector[i];
        }
        cout << endl;
    }
    return 0;
}