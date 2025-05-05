#include<iostream>
#include <stack>
using namespace std;

void test(string str){
    stack<string> S; 
    int l;
    string t;
    l = str.size(); 
    for (int i; i<l; i++){
        t = str[i]; 
        if (t =="("){
            S.push(t);
        }
        else{
            if (S.empty()){
                cout << "NO" << endl;
                return ; 
            }
            else if(S.top() == "("){
                S.pop();
            }
            else{
                cout << "NO" << endl;
                return ;
            }

        }
    }
    if(S.empty()){
        cout << "YES"<< endl;
    }
    else{
        cout<<"NO"<<endl;
    }
    return; 
}

int main()
{
    int N; 
    string x ; 
    cin >> N; 
    for (int i=0; i<N; i++){
        cin >> x ; 
        test(x);
    };
    return 0;
}
