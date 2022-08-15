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
        int ans = 0;
        for (int i = 1; i <= a;)
        {
            ans += (a - i + 1) * (a - i + 1);

            i += 2;
        }
        cout << ans << endl;
    }
    return 0;
}