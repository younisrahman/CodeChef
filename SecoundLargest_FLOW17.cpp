#include <bits/stdc++.h>
using namespace std;

int main()
{
    // your code goes here
    int t, a, b, c, d;
    string ans;
    cin >> t;
    while (t--)
    {
        cin >> a >> b >> c;
        if (a > b && a > c)
        {
            if (b > c)
            {
                std::cout << b << std::endl;
            }
            else
            {
                std::cout << c << std::endl;
            }
        }
        else if (c > b && c > a)
        {
            if (b > a)
            {
                std::cout << b << std::endl;
            }
            else
            {
                std::cout << a << std::endl;
            }
        }
        else
        {
            if (c > a)
            {
                std::cout << c << std::endl;
            }
            else
            {
                std::cout << a << std::endl;
            }
        }
    }
    return 0;
}