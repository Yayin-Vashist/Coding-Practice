#include<iostream>

using namespace std;

int main(){
  int t;
  cin>>t;
  while(t--){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0; i<n; ++i)
      cin>>arr[i];
    int x=0;
    for(int i=0; i<n; ++i)
      x ^= arr[i];
    if(n%2==0 && x==0)
      cout<<"0"<<endl;
    else if (n%2==1)
      cout<<x<<endl;
    else 
      cout<<-1<<endl;
  }
}
