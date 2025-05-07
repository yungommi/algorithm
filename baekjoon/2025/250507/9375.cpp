#include<iostream>
#include<map> 
using namespace std;

int main()
{
    int N; cin >> N ; 
    for (int i=0; i<N; i++){
        int x; cin >> x; 
        map<string, int> m; 
        for (int j=0; j<x; j++){
            string s1,s2; 
            cin >> s1 >> s2; 
            m[s2]++; 
        }
        //for (auto& [a,b] : m){
        //    cout<< a<< ' '<< b << '\n';
        //}
        int sum = 1; 
        for (auto x:m){
            sum *= x.second+1; 
        }
        cout << sum-1 << '\n';
    }
    return 0;
}