#include <bits/stdc++.h>
#include <algorithm>
//#include<iostream>
using namespace std;
int main()
{
    int a, b, c, d, n;
    cin >> n;
    while (n--)
    {
        cin >> a >> b >> c >> d;
        int max1 = std::max((a + c), (a + d));
        int max2 = std::max((b + c), (b + d));
        cout << std::max(max1, max2) << endl;
    }
    return 0;
}