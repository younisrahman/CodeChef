#include <bits/stdc++.h>
//#include<iostream>
using namespace std;
int main()
{
    int n, a, b, c, d, e;
    cin >> n;
    while (n--)
    {
        cin >> a >> b >> c >> d >> e;
        if (a > e && b > e && c > e)
        {
            cout << "NO" << endl;
            continue;
        }
        else
        {
            int fs = a + b, wi = c;
            if (fs <= d && (wi <= e) || (b + c <= d && a <= e) || (a + c <= d && b <= e))
            {
                cout << "YES" << endl;
            }
            else
            {
                cout << "NO" << endl;
            }
        }
    }
    return 0;
}