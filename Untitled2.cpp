// TO HOP
#include <iostream>
using namespace std;
void kq(const int*a,int k)
{
	for(int i=0;i<=k;i++)
	cout<< a[i];
	cout<< endl;
	}

void thuat_toan(int *a,int n,int k,int j)
{
	for(int i=a[j-1]+1;i<= n-k+j;i++){
		a[j]=i;
		if (j==k)
			kq(a,k);
		else
			thuat_toan(a,n,k,j+1);
	}
}
int main(){
	int k,n;
	cout<< "nhap n va k:";
	cin>>n>>k;
	int a[n];
	a[0]=0;
	thuat_toan(a,n,k,1);
	return 0;
	}
