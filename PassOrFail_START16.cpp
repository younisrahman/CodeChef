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
        int score = (b * 3) + ((a - b) * -1);
        ans = score >= c ? "PASS" : "FAIL";
        cout << ans << endl;
    }
    return 0;
}
