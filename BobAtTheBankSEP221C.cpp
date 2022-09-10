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
        cin >> a >> b >> c >> d;
        std::cout << a + (b * d) - (c * d) << std::endl;
    }
    return 0;
}