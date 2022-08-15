#include <bits/stdc++.h>
//#include<iostream>
// Chef wants to rent a car to travel to his restaurant which is NN kilometers away.He can either rent a petrol car or a diesel car.

// One litre of petrol costs XX rupees
// and one litre of diesel costs YY rupees.
// Chef can travel AA kilometers with one litre of petrol
// and BB kilometers with one litre of diesel.

// Chef can buy petrol and diesel in any amount,
//  not necessarily integer.For example, if X = 95X = 95,
// Chef can buy half a litre of petrol by paying 95 / 2 = 47.595 / 2 = 47.5 rupees.

using namespace std;
int main()
{
    int t, n, x, y, a, b;
    string ans;
    cin >> t;
    while (t--)
    {
        cin >> n >> x >> y >> a >> b;
        int patrolAmount = (x / a) * n;
        int diselAmount = (y / b) * n;
        if (patrolAmount < diselAmount)
        {
            ans = "PETROL";
        }
        else if (patrolAmount > diselAmount)
        {
            ans = "DIESEL";
        }
        else
        {
            ans = "ANY";
        }
        cout << ans << endl;
    }

    return 0;
}