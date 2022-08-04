#include <bits/stdc++.h>
using namespace std;

long long recursion(int a)
{
    if (a == 1)
    {
        return a;
    }
    return a * recursion(a - 1);
}
int main()
{
    // your code goes here
    int t, a, b, c, d;
    string ans;
    cin >> t;
    while (t--)
    {
        cin >> a;
        long long ans = 1;
        for (int i = a; i >= 1; i--)
        {
            ans *= i;
        }
        cout << ans << endl;
    }
    return 0;
}