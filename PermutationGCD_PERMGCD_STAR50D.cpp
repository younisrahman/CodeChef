#include <bits/stdc++.h>
//#include<iostream>
using namespace std;
int main()
{
    int t, a, b;
    cin >> t;
    while (t--)
    {
        cin >> a >> b;
        if (a > b)
        {
            std::cout << -1;
        }
        else
        {

            cout << (b - a + 1) << " ";
            for (int i = 1; i <= a; i++)
            {
                if (i == (b - a + 1))
                    continue;
                else
                {
                    cout << i << " ";
                }
            }
        }
        cout << endl;
    }
    return 0;
}