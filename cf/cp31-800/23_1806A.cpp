#include<iostream>

using namespace std;

int main(){
  int t;

  cin>>t;
  while(t--){
    int a,b,c,d;
    cin>>a>>b>>c>>d;

    if (d<b)
      cout<<-1<<endl;
    else if(a+d-b<c)
      cout<<-1<<endl;
    else 
      cout<<d-b+a+d-b-c<<endl;
  }

  return 0;
}
