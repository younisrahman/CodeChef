#include <bits/stdc++.h>
//#include<iostream>
using namespace std;
int main()
{
    int n;
    float a, b, c, d;
    vector<int> vector;
    set<int> set;
    cin >> n;
    while (n--)
    {
        cin >> a >> b >> c >> d;
        float f = d / b;
        float alic = a * f;
        if (alic < c)
            std::cout << "Bob" << std::endl;
        else if (alic > c)
            std::cout << "Alice" << std::endl;
        else
            std::cout << "Equal" << std::endl;
    }
    return 0;
}