#include <bits/stdc++.h>
//#include<iostream>
using namespace std;
int main()
{
    int n, a, b, c, d;
    vector<int> v;
    vector<int> v2;

    cin >> n;
    while (n--)
    {
        cin >> a;
        vector<int> fa;
        vector<int> fb;
        for (int i = 0; i < a; i++)
        {
            int val;
            cin >> val;
            v.push_back(val);
        }
        if ((a & 1) == 0)
        {
            for (int i = 0; i < v.size(); i += 2)
            {

                if (std::count(fa.begin(), fa.end(), v[i]))
                {
                    if (std::count(fb.begin(), fb.end(), v[i]))
                    {
                        continue;
                    }
                    else
                    {
                        fb.push_back(v[i]);
                        if (std::count(fa.begin(), fa.end(), v[i + 1]))
                        {
                            continue;
                        }
                        else
                        {
                            fa.push_back(v[i + 1]);
                        }
                    }
                }
                else
                {
                    fa.push_back(v[i]);
                    if (std::count(fb.begin(), fb.end(), v[i + 1]))
                    {
                        if (std::count(fa.begin(), fa.end(), v[i + 1]))
                        {
                            continue;
                        }
                        else
                        {
                            if (std::count(fb.begin(), fb.end(), v[i]))
                            {
                                continue;
                            }
                            else
                            {
                                fa.pop_back();
                                fa.push_back(v[i + 1]);
                                fb.push_back(v[i]);
                            }
                        }
                    }
                    else
                    {
                        fb.push_back(v[i + 1]);
                    }
                }
            }
        }
        if (a % 2 == 0 && fa.size() != 0 && fb.size() != 0 && fa.size() == fb.size())
        {
            std::cout << "YES" << std::endl;
            std::cout << fa.size() << fb.size() << std::endl;
        }
        else
        {
            std::cout << "NO" << std::endl;
            std::cout << fa.size() << fb.size() << std::endl;
        }
    }
    return 0;
}