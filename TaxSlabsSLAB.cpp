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
        int taxAmount = 0, amount = a - 250000;
        float tax = 0.05;
        while (amount > 0)
        {
            if (tax > .25)
            {
                taxAmount += amount * .3;
                break;
            }
            if ((amount - 250000) > 0)
            {
                taxAmount += (250000 * tax);
                tax += 0.05;
                amount -= 250000;
            }
            else
            {
                taxAmount += (amount * tax);
                tax += 0.05;
                break;
            }
        }

        std::cout << a - taxAmount << std::endl;
    }
    return 0;
}