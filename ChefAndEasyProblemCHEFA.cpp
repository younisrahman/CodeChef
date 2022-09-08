#include <bits/stdc++.h>
using namespace std;
#define int long long
int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL), cout.tie(NULL);
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int a[n];

        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }
        sort(a, a + n);
        if (n % 2 == 0)
        {
            int sum = 0;
            for (int i = 1; i < n; i += 2)
                sum += a[i];

            cout << sum << endl;
        }
        else
        {
            int sum = 0;
            for (int i = 0; i < n; i += 2)
                sum += a[i];

            cout << sum << endl;
        }
    }
    return 0;
}