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
        int ans = 0;
        cin >> a >> b >> c;
        ans = ((b - c) * a);
        std::cout << ans << std::endl;
    }
    return 0;
}