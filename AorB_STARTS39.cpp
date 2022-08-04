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
        cin >> a >> b;
        c = 1500 - (a * 2) - ((b + a) * 4);
        d = 1500 - ((a + b) * 2) - (b * 4);
        if (c > d)
            std::cout << c << std::endl;
        else
            std::cout << d << std::endl;
    }
    return 0;
}
