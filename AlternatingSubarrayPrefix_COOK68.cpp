#include <iostream>
using namespace std;
#define ll long long

void solution()
{
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    if (n < 2)
    {
        cout << 1 << endl;
        return;
    }
    int ans[n] = {0};
    ans[n - 1] = 1;
    for (int j = n - 2; j >= 0; j--)
    {
        if ((a[j] > 0 && a[j + 1] > 0) || (a[j] < 0 && a[j + 1] < 0))
        {
            ans[j] = 1;
        }
        else
        {
            ans[j] = ans[j + 1] + 1;
        }
    }
    for (int i = 0; i < n; i++)
    {
        cout << ans[i] << " ";
    }
    cout << endl;
}

int main()
{
    // your code goes here
    ll t, n, k;
    cin >> t;
    while (t--)
    {
        // solve();
        solution();
        cout << endl;
    }
    return 0;
}
