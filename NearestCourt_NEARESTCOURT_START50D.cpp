#include <bits/stdc++.h>
//#include<iostream>
using namespace std;
int main()
{
    int t, x, y;
    cin >> t;
    while (t--)
    {
        cin >> x >> y;
        int val = abs(x - y);
        if (val == 1)
        {
            std::cout << val << std::endl;
        }
        else
        {
            cout << round(val / 2) + (val % 2) << endl;
        }
    }

    return 0;
}