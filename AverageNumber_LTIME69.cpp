#include <bits/stdc++.h>
//#include<iostream>
using namespace std;
int main()
{
    int n, a, b, c, d, e, f;
    cin >> n;
    while (n--)
    {

        cin >> a >> b >> c;
        cin >> d >> e >> f;
        int sum = d + e + f, total = (a + b) * c, restOfAmount = total - sum;
        if (restOfAmount % b == 0 && restOfAmount>= b)
            cout << restOfAmount / b << endl;
        else
            cout << -1 << endl;
    }
    return 0;
}