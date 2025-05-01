#include<iostream>
#include <string>
#include <algorithm> 
//#include <utility>
using namespace std;

string WB[8]={
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
};

string BW[8]={
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
};
string board[80];

int WB_cnt (int x, int y){
    int cnt = 0; 
    for (int i=0; i<8; i++){
        for (int j=0; j<8; j++){
            if(board[x+i][y+j] != WB[i][j])
                cnt ++ ; 
        }
    }
    return cnt;
}

int BW_cnt (int x, int y){
    int cnt = 0; 
    for (int i=0; i<8; i++){
        for (int j=0; j<8; j++){
            if(board[x+i][y+j] != BW[i][j])
                cnt ++ ; 
        }
    }
    return cnt;
}

int main(){
    int size[2];
    int cnt;
    int min_val = 65; 
    //pair<int, int> p1;
    cin >> size[0] >> size[1];
    for (int i = 0; i<size[0]; i++)
        cin >> board[i];
    for (int i=0; i+8 <=size[0]; i++){
        for (int j=0; j+8 <= size[1]; j++){
            min_val = min(min_val,WB_cnt(i,j));
            min_val = min(min_val,BW_cnt(i,j));
        }
    }
    cout << min_val; 
    return 0 ;
}

 
