#include <bits/stdc++.h>
using namespace std;

int main()
{
    // your code goes here
    int t, a, b, c, d;
    cin >> t;
    while (t--)
    {
        cin >> a;
        vector<int> v(a);
        for (int i = 0; i < a; i++)
        {
            cin >> v[i];
        }
        int ans = 0;
        for (int i = 0; i < a; i++)
        {
            ans = ans ^ v[i];
        }
        cout << ans << endl;
    }
    return 0;
}