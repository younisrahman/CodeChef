#include <bits/stdc++.h>
//#include<iostream>
using namespace std;
int main()
{
    int n, a, b, c, d;
    set<int> set;
    cin >> n;
    while (n--)
    {
        cin >> a;
        vector<int> vec;

        for (int i = 0; i < a; i++)
        {
            cin >> b;
            vec.push_back(b);
        }
        sort(vec.begin(), vec.end());
        int amount = 0;
        for (int i = a - 1; i >= 0; i -= 2)
        {
            amount += vec[i];
        }
        std::cout << amount << std::endl;
    }
    return 0;
}