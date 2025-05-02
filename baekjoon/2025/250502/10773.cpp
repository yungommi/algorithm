#include<iostream>
#include <stack>
using namespace std;

int main()
{
    int N; 
    int x ; 
    stack<int> L; 
    cin >> N; 
    for (int i=0; i<N; i++){
        cin >> x ; 
        if (x==0){
            L.pop();
        }
        else{
            L.push(x);
        }
    }
    int size = L.size();
    int ans = 0; 
    for (int i=0; i<size; i++){
        ans += L.top();
        L.pop();
    }
    cout << ans; 
    return 0;
}
