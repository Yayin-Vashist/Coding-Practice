#include<iostream>

using namespace std;

int main(){
  int t;
  cin>>t;
  while(t--){
    int n;
    cin>>n;
    char arr[n];
    cin>>arr;
    int cnt=0;
    for(int i=0; i<n/2; ++i)
      if(arr[i]!=arr[n-1-i])
        ++cnt;
      else 
        break;
    cout<<n-2*cnt<<endl;
//    cout<<cnt<<endl;
  }
}
