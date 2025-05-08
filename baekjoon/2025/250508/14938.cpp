#include<iostream>
#include<vector> 
#include<queue> 
using namespace std;
#define INF 10000000 

int n,m,r,a,b,l; 
int item[101]; 
int dij[101];
vector<pair<int,int>> v[101]; 
int ans; 

void dijk(int X){
    for (int i=1; i<=n; i++){
        dij[i] = INF; 
    }
    queue <int> q; 
    dij[X]=0; 
    q.push(X); 
    while (!q.empty()){
        int node = q.front(); 
        int dist = dij[node];
        q.pop();
        for (int i=0; i<v[node].size(); i++){
            int next = v[node][i].first;
            int leng = v[node][i].second; 
            if (dij[next]>dist+leng){
                dij[next]=dist+leng;
                q.push(next);
            }
        }
    }
    int tmp = 0; 
    for (int i=1; i<=n; i++){
        if (dij[i]<=m){
            tmp += item[i];
        }
    }
    ans = max(ans, tmp);
}

int main()
{
    ios_base::sync_with_stdio(0);
	cin.tie(0);
    cin >> n >> m >> r ; 
    for (int i=1; i<=n; i++){
        cin >> item[i];
    }
    for (int i=0; i<r; i++){
        cin >> a >> b >> l ; 
        v[a].push_back({b,l});
        v[b].push_back({a,l}); 
    }
    for (int i=1; i<=n; i++){
        dijk(i);
    }
    cout << ans ; 
    return 0;
}
