#include<iostream>
using namespace std;

int main(void)
{
    int cnt = 0 ; 
    int n; 
    cin >> n; 
    for (long long power =5; power<=n; power*=5)
    {
        cnt += n/power;
    }
    cout << cnt; 
}