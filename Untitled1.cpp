
#include <iostream>
using namespace std;
int main()
{
    int n;
    cout<<"Nhap vao do dai day nhi phan : ";
    cin>>n;
 
    int mang[n];
 
    int i;
    for(i = 0; i < n; i++)
    {
        mang[i] = 0;
    }
 
    for(i = 0; i < n; i++)
    {
        cout<<mang[i];
    }
    
 

    for(i = n - 1; i >= 0; i--)
    {
        if(mang[i] == 0)  
        {
            mang[i] = 1; 
 
            int j;
            for(j = i + 1; j < n; j++)  
            {
                mang[j] = 0;
            }
            for(j = 0; j < n; j++)
            {
               cout<<mang[j];
            }
            
            i = n;  
                    
        }
    }
 
    
    return 0;
}
