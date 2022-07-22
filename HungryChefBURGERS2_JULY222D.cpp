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
        if (money / premium >= need)
        {
            cout << "0 " << need << endl;
        }
        else if (money / normal < need)
        {
            cout << "-1\n";
        }
        else
        {
            int k = (money - (premium * need)) / (normal - premium);
            if ((money - (premium * need)) % (normal - premium) == 0)
            {
                cout << k << " " << (need - k) << endl;
            }
            else
            {
                cout << k + 1 << " " << (need - (k + 1)) << endl;
            }
        }
    }

    return 0;
}