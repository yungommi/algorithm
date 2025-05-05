#include<iostream>
#include<string>
using namespace std;

int main(){
    int n; 
    int result = 665; 
    string tmp;
    cin >> n ; 

    for (int i=0; i<n; i++){
        while(1){
            result ++; 
            tmp = to_string(result);
            if (tmp.find("666") != -1)
                break;
        }
    }
    cout << result << endl;
}