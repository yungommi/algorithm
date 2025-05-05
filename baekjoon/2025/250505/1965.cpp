#include<iostream>
using namespace std;

int main()
{
    int N;
    cin >> N ; 
    int x;
    int arr [N];
    int dp[N];
    for (int i=0; i<N; i++){
        cin >> x; 
        arr[i]=x; 
    }
    dp[0]=1;
    for (int i=1; i<N; i++){
        dp[i]=1;
        for (int j=i; j>-1; j--){
            if (arr[j] < arr[i]){
                dp[i] = max(dp[i], dp[j]+1); 
            }
        }
    }
    int ans = 0 ; 
    for ( int i=0; i<N; i++){
        ans = max(ans, dp[i]);
    }
    cout << ans << endl;
    return 0;
}
