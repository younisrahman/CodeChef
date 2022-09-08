#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<int> arrival(n);
        vector<int> departure(n);
        for (int i = 0; i < n; i++)
        {
            cin >> arrival[i];
        }
        for (int i = 0; i < n; i++)
        {
            cin >> departure[i];
        }
        sort(arrival.begin(), arrival.end());
        sort(departure.begin(), departure.end());

        int j = 0;
        int count = 0;
        int ans = 0;
        for (int i = 0; i < n; i++)
        {
            if (arrival[i] < departure[j])
            {
                count++;
            }
            else if (arrival[i] > departure[j])
            {
                j++;
                count--;
            }
            else
            {
                j++;
            }
            ans = max(ans, count);
        }
        cout << ans << endl;
    }
    return 0;
}
