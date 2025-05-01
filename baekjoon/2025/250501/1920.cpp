#include<iostream>
#include <algorithm>
using namespace std;

int N,M;
int arr[100000];
int tmp; 

void binary_search(int x){
    int left = 0 , mid = 0, right = N-1; 
    while(left<=right){
        mid = (left+right)/2; 
        if (arr[mid]==x){
            cout << 1<< '\n';
            return ; 
        }else if(arr[mid]>x){
            right = mid-1;
        }else{
            left = mid+1;
        }
    }
    cout << 0 << '\n';
    return; 
}

int main()
{
    //입출력 시간 단축, 
    //buffer 시스템을 끊어 printf scanf등 사용할 수 없고
    //multi threading시에 충돌 생길 수 있지만 알고리즘에선 single thread 이므로 사용가능 
    ios_base::sync_with_stdio(0);
    cin.tie(0); 

    cin >> N; 
    for(int i=0; i<N; i++){
        cin >> arr[i];
    };
    sort(arr,arr+N); 

    cin >> M; 
    int x;
    for(int i=0; i<M; i++){
        cin >> x;
        binary_search(x);
    }
    return 0;
}

/*
#include <iostream>
#include <algorithm>
using namespace std;

int n, m;                       // a_array 배열의 길이, 찾고자하는 정수 x의 개수
int a_array[1000000];           // 정수 a를 저장한 배열
int temp;

void binary_search(int x) {
    int left = 0, mid = 0, right = n - 1;

    while (left <= right) {
        mid = (left + right) / 2;

        // 탈출 조건 : a_array에서 x를 찾은 경우
        if (a_array[mid] == x) {
            cout << 1 << "\n";
            return;
        } else if (a_array[mid] > x) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    // 이분 탐색이 끝날 때까지 x를 찾지 못했다면 0(false)를 출력한다.
    cout << 0 << "\n";

    return;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); 

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> a_array[i];
    }

    // 이분 탐색 알고리즘을 적용하기 위해 배열을 오름차순으로 정렬한다.
    sort(a_array, a_array + n);
    
    cin >> m;

    int x;
    for (int i = 0; i < m; i++) {
        cin >> x;
        binary_search(x);
    }

    return 0;
}
*/