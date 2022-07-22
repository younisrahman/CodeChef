#include <iostream>
using namespace std;

// Main() function: where the execution of program begins
int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int normal, premium, need, money;
        cin >> normal >> premium >> need >> money;
        if (money / normal < need)
        {
            cout << "-1\n";
        }
        else
        {
            int nor = need;
            int prem = 0;
            int mney = money - (need * normal);
            while (mney >= 0)
            {
                mney -= (premium - normal);
                if (mney < 0)
                {
                    break;
                }
                prem += 1;
                nor -= 1;
                if (nor == 0)
                    break;
            }
            cout << nor << ' ' << prem << "\n";
        }
    }

    return 0;
}