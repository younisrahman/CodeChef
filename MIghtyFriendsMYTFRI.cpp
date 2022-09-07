#include <bits/stdc++.h>
//#include<iostream>
using namespace std;
int main()
{
    int n, a, b, c, d;
    cin >> n;
    while (n--)
    {
        vector<int> m, t;

        cin >> a >> b;
        for (int i = 0; i < a; i++)
        {
            cin >> c;
            if ((i & 1) != 0)
            {
                t.push_back(c);
            }
            else
            {
                m.push_back(c);
            }
        }
        sort(m.begin(), m.end());
        sort(t.begin(), t.end());
        if (b > 0)
        {
            int count = 0;
            int j = 0;
            int i = m.size() - 1;
            while (b--)
            {
                if (t.size() - 1 == j)
                {
                    break;
                }
                if (m[i] > t[j])
                {
                    swap(m[i], t[j]);
                }
                j++;
                i--;
            }
        }
        int motu = 0, tomu = 0;
        for (int i = 0; i < m.size(); i++)
        {
            motu += m[i];
        }
        for (int i = 0; i < t.size(); i++)
        {
            tomu += t[i];
        }
        if (tomu > motu)
        {
            std::cout << "YES" << std::endl;
        }
        else
        {
            std::cout << "NO" << std::endl;
        }
    }
    return 0;
}